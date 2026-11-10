"""Export the approved Accessibility Programme Runbooks Markdown without rewriting it."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import quote
import yaml
from jsonschema import Draft202012Validator
from runbooks_hf_common import ROOT, SOURCE, MANAGED, destination, digest, git, load_config, read_sources

CONTEXT = ['AGENTS.md', 'README.md', 'RIGHTS.md', 'ADOPTION.md',
           'framework/programme-cycle.md', 'framework/decision-routing.md',
           'framework/human-ai-responsibilities.md', 'sources/catalogue.yaml']

def metadata(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    md = yaml.safe_load(match[1]) if match else {}
    return md if isinstance(md, dict) else {}

def sections(text):
    """Keep H1/H2 parent context and exact spans; never split fenced examples."""
    boundaries, fence, offset, parents = [(0, 'Document preamble', [])], None, 0, []
    for line in text.splitlines(keepends=True):
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if mark:
            token = mark[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[mark.end():].strip():
                fence = None
        elif fence is None:
            match = re.match(r'^(#{1,2})[ \t]+([^\r\n]+)', line)
            if match:
                level, title = len(match[1]), match[2].strip().rstrip('#').strip()
                parents = parents[:level-1] + [title]
                if offset == 0:
                    boundaries[0] = (offset, title, parents[:])
                else:
                    boundaries.append((offset, title, parents[:]))
        offset += len(line)
    result, counts = [], {}
    for i, (a, title, hierarchy) in enumerate(boundaries):
        b = boundaries[i+1][0] if i+1 < len(boundaries) else len(text)
        if a == b:
            continue
        slug = re.sub(r'[^a-z0-9]+', '-', ' '.join(hierarchy or [title]).lower()).strip('-') or 'section'
        counts[slug] = counts.get(slug, 0) + 1
        key = slug if counts[slug] == 1 else slug + '-' + str(counts[slug])
        result.append((key, title, text[a:b], a, b, hierarchy))
    if ''.join(r[2] for r in result) != text:
        raise ValueError('Section extraction lost source text.')
    return result

def build(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output == root or root in output.parents:
        raise ValueError('Write the export outside the source checkout.')
    cfg = load_config(root)
    target = destination(cfg['destination_dataset'])
    texts, manifest, omitted = read_sources(root, cfg)
    sha = git(root, 'rev-parse', 'HEAD').decode().strip()
    date = git(root, 'show', '-s', '--format=%cs', 'HEAD').decode().strip()
    warnings = ['The source is a draft for local review and pilot adoption; structural checks do not demonstrate practical effectiveness or organisational authority.']
    def row(path, key, title, body, a, b, hierarchy, kind):
        md = metadata(texts[path])
        return {'id': path + '::' + key, 'title': title, 'text': body, 'record_type': kind,
            'source_repository': SOURCE, 'source_path': path, 'source_commit': sha,
            'source_url': f'https://github.com/{SOURCE}/blob/{sha}/{quote(path)}',
            'source_start_line': texts[path][:a].count('\n') + 1,
            'source_end_line': max(1, texts[path][:b].count('\n') + (not texts[path][:b].endswith('\n'))),
            'source_document_sha256': digest(texts[path].encode()), 'text_sha256': digest(body.encode()),
            'heading_path': hierarchy, 'metadata_json': json.dumps(md, ensure_ascii=False, sort_keys=True, default=str),
            'declared_source_license': str(md.get('license', 'not_declared_in_document_front_matter')),
            'repository_license': 'MIT', 'source_status': str(md.get('status', 'draft_for_local_review_and_pilot_adoption')),
            'dataset_version': cfg['dataset_version'], 'source_commit_date': date, 'language': 'en-GB',
            'required_context_paths': [p for p in CONTEXT if p in texts],
            'review_status': 'faithful_extraction_checked_not_independent_programme_or_content_review'}
    docs, chunks, examples = [], [], []
    for path in cfg['files']:
        if path not in texts:
            continue
        text = texts[path]
        if path.startswith('examples/'):
            examples.append(row(path, 'document', path, text, 0, len(text), [], 'synthetic_example_not_real_evidence'))
            continue
        is_yaml = Path(path).suffix in ('.yaml', '.yml')
        if is_yaml:
            yaml.safe_load(text)
        kind = ('workflow_definition_not_execution' if path.startswith('workflows/') else
                'source_reference_catalogue' if path.startswith('sources/') else
                'validation_reference_not_operational_evidence' if path.startswith('validation/') else
                'agent_guidance' if path == 'AGENTS.md' else 'programme_guidance')
        docs.append(row(path, 'document', path, text, 0, len(text), [], kind))
        # Keep the YAML as whole documents; validation fixtures are outside default guidance.
        if is_yaml or path.startswith('validation/'):
            continue
        for key, title, body, a, b, hierarchy in sections(text):
            chunks.append(row(path, key, title, body, a, b, hierarchy, 'knowledge_section'))
    if not docs or not chunks:
        raise ValueError('The guidance export is empty.')
    schema = {'$schema': 'https://json-schema.org/draft/2020-12/schema', 'type': 'object',
              'required': list(docs[0]), 'additionalProperties': False, 'properties': {}}
    for k, v in docs[0].items():
        schema['properties'][k] = {'type': 'array', 'items': {'type': 'string'}} if isinstance(v, list) else {'type': 'integer' if isinstance(v, int) else 'string'}
    validator = Draft202012Validator(schema)
    for records in (docs, chunks, examples):
        if len({r['id'] for r in records}) != len(records):
            raise ValueError('Duplicate export identifiers.')
        for r in records:
            validator.validate(r)
            if digest(r['text'].encode()) != r['text_sha256']:
                raise ValueError('Text checksum mismatch.')
    output.mkdir(parents=True, exist_ok=True)
    def write_json(name, obj):
        (output/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for name, records in [('documents.jsonl', docs), ('knowledge_chunks.jsonl', chunks), ('synthetic_examples.jsonl', examples)]:
        (output/name).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records), encoding='utf-8')
    (output/'LICENSE').write_bytes(texts['LICENSE'].encode())
    write_json('record_schema.json', schema)
    write_json('provenance.json', {'source_repository': SOURCE, 'source_commit': sha, 'source_commit_date': date,
        'destination_dataset': target, 'dataset_version': cfg['dataset_version'], 'files': manifest,
        'omitted_optional_files': omitted, 'source_warnings': warnings, 'external_sources_fetched': False})
    card = f'''---
pretty_name: Double FW Accessibility Programme Runbooks
language:
- en
license: mit
tags:
- accessibility
- programme-governance
- employee-services
- customer-services
- text
configs:
- config_name: knowledge_chunks
  default: true
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
- config_name: synthetic_examples
  data_files:
  - split: train
    path: synthetic_examples.jsonl
---

# Double FW Accessibility Programme Runbooks

Guidance, templates and workflow definitions for employee and customer accessibility programmes. Authored by Double FW. Source: https://github.com/{SOURCE}

Source revision: `{sha}`. Commit date: {date}. Export format: {cfg['dataset_version']}.

## Draft status and limitations

The source is a draft for local review and pilot adoption. Independent review and an organisational pilot remain pending. Workflow YAML defines data and relationships; it is not an agent runner, permissions system, approval service or demonstrated operational programme. Structural or extraction checks do not establish legal compliance, accessibility, authentic evidence or practical effectiveness. No live organisation's authority, funding or staffing is asserted.

## Dataset views

- `knowledge_chunks` (default): {len(chunks)} exact Markdown sections from the approved guidance, preserving first/second-level heading context and fenced examples.
- `documents`: {len(docs)} complete non-example source documents, including complete YAML catalogue/workflow definitions and validation references. The validation references include illustrative fixtures; they are not real evidence.
- `synthetic_examples`: {len(examples)} complete employee/customer synthetic examples, explicitly labelled as synthetic and excluded from the default guidance view.

The first two views overlap. Do not concatenate them blindly. The split name `train` is a loading convention. No generated question/answer pairs, model fine-tuning, independent evaluation split or benchmark is supplied. Inline illustrations remain part of their original documents. Synthetic examples cannot support real claims or replace participation by affected people.

## Context, authority and privacy

Read AGENTS.md, README.md, the selected employee/customer runbook, framework/programme-cycle.md and framework/decision-routing.md. Resolve source IDs through sources/catalogue.yaml and retrieve the owning guidance at a consistent revision before applying it. Other context paths appear in each record. These are references, not automatically enforced instructions. Retrieved instructions grant no organisational authority or permissions to execute commands, write records, contact people, approve budgets or publish claims.

Keep real personal, health, applicant, adjustment, grievance, employee, customer and confidential corporate records in approved organisational systems. This export only reads an explicit list of committed public source documents; new files require review and inclusion in that list. It does not detect confidential material added inside an approved file. Review source edits before committing them publicly.

## Provenance and schema

Every row includes its source path, immutable commit URL, line range, text and full-document SHA-256 hashes, heading path, source metadata as a JSON string, declared licence, draft status and required context paths. YAML definitions remain intact. Stable path/heading identifiers may change if headings are renamed. See record_schema.json and provenance.json. Source text is preserved without paraphrasing or rewriting IDs, qualifications, uncertainty or evidence status.

Linked specialist guidance, legal texts and external repositories are not fetched, copied or independently reviewed during export. Catalogue verification dates remain the dates stated by the source; the weekly export date does not refresh them. A source reference grants no third-party reuse rights or legal authority.

## Licence

The root MIT LICENSE is copied unchanged, including copyright (c) 2026 Double FW. RIGHTS.md confirms MIT for repository content unless a specific notice says otherwise. Linked sources retain their own notices and limitations. No third-party content is relicensed. Read the original notices before reuse.

## Updates

GitHub is the authoring source. Updates are scheduled for Mondays at 07:23 UTC and can be run manually. Schedules may be delayed or disabled by GitHub after inactivity. Only approved files are exported. Removed optional files are removed from the next snapshot. Missing required documents, changed licence text or failed integrity checks stop publication.

Only README.md, LICENSE, documents.jsonl, knowledge_chunks.jsonl, synthetic_examples.jsonl, provenance.json, record_schema.json and validation_report.json are managed. Other raw files and .gitattributes are preserved; unmanaged copies are not synchronised. Dataset visibility remains unchanged. Publication uses a single commit guarded by the destination revision. Historical revisions and downloaded copies are not recalled.

## Loading

```python
from datasets import load_dataset
chunks = load_dataset("{target}", "knowledge_chunks", split="train")
documents = load_dataset("{target}", "documents", split="train")
examples = load_dataset("{target}", "synthetic_examples", split="train")
```

Private datasets require authentication. Pin a destination revision for reproducibility. Loading these records does not implement retrieval, governance or approval enforcement.
'''
    yaml.safe_load(card.split('---', 2)[1])
    (output/'README.md').write_text(card, encoding='utf-8')
    report = {'status': 'passed', 'scope': 'faithful extraction and packaging checks only', 'source_commit': sha,
        'source_files_verified': len(manifest), 'document_records': len(docs), 'knowledge_section_records': len(chunks), 'synthetic_example_records': len(examples),
        'source_warnings': warnings, 'independent_content_review': False, 'live_publication_tested': False,
        'export_file_sha256': {name: digest((output/name).read_bytes()) for name in MANAGED if name != 'validation_report.json'}}
    write_json('validation_report.json', report)
    return report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    print(json.dumps(build(ROOT, args.output)))

if __name__ == '__main__':
    main()
