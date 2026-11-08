#!/usr/bin/env python3
"""Offline structural and record-shape checks; not a workflow/approval engine."""
from pathlib import Path
import argparse, json, re, sys, unicodedata
from urllib.parse import unquote, urlsplit
import yaml

ROOT=Path(__file__).resolve().parents[1]
catalogue=yaml.safe_load((ROOT/'sources/catalogue.yaml').read_text())
workflow=yaml.safe_load((ROOT/'workflows/programme.yaml').read_text())

def source_index():
    lines=['# Double-FW knowledge routes',
        '**Generated from [catalogue.yaml](catalogue.yaml).** Edit the YAML, then run `python3 validation/check.py --write-source-index` from the repository root.',
        'Select only the relevant sources, read the owning guidance and retain its limitations. Discovery links find current guidance; resolved links identify the exact entry points retrieved on 8 November 2026. These revisions are provenance for this package, not local organisational approval baselines. No detailed guidance is copied here.',
        f'The {len(catalogue["sources"])} entry-point files across {len({s["repository"] for s in catalogue["sources"]})} repositories were retrieved. Review covered routing and selected governance content; it was not a complete audit of downstream guidance, external links, legal claims or source rights. Local use must verify the authority, currency and applicability needed for the decision.',
        'For current-source handling use [source use and change](../framework/source-use-and-change.md).']
    for s in catalogue['sources']:
        lines += [f'## {s["id"]}', f'**{s["title"]}** — {s["purpose"]}',
            f'[Discover owning guidance]({s["discovery_url"]}) · [Retrieved revision]({s["resolved_url"]})',
            f'**Owning repository:** `{s["repository"]}`. **Path:** `{s["path"]}`.',
            f'**Verification:** {s["last_verified"]}; {s["access_status"]}; {s["review_status"]}. **Authority classification:** {s["authority_type"]}. **Local adoption:** {s["local_adoption_status"]}.',
            f'**Used by:** {", ".join(s["used_by"])}. **Limitations:** {s["limitations"]}']
    return '\n\n'.join(lines)+'\n'

def slug(text):
    text=re.sub(r'[`*_]','',text).lower()
    return ''.join(c for c in text if c.isalnum() or c in '-_ ').replace(' ','-')

def record_errors(kind, record, real=False):
    """Check declared shape and guard presence only; never authenticate content."""
    errors=[]
    for key in workflow['record_contracts'][kind]:
        if key not in record or record[key] is None or record[key]=='':
            errors.append('missing:'+key)
    if kind=='source_use':
        if not re.fullmatch(r'[0-9a-f]{40}',str(record.get('resolved_commit_sha',''))):
            errors.append('invalid_commit_shape')
    if kind=='evidence':
        if record.get('actual_result') not in workflow['assessment_classes']:
            errors.append('invalid_result')
        if real and record.get('synthetic') is not False:
            errors.append('synthetic_evidence_in_real_context')
        if record.get('actual_result')=='not_applicable' and not record.get('scope_reason'):
            errors.append('not_applicable_without_reason')
    if kind=='decision':
        # Drafts can leave approval pending; the required field must exist.
        errors=[e for e in errors if e!='missing:authenticated_approval_reference']
        if 'authenticated_approval_reference' not in record:
            errors.append('missing:authenticated_approval_reference')
        if record.get('workflow_state')=='approved' and not record.get('authenticated_approval_reference'):
            errors.append('approved_without_reference')
        if real and record.get('synthetic') is not False:
            errors.append('synthetic_decision_in_real_context')
    if kind in ('foundation_coverage','component_coverage'):
        # Draft assets can be missing only with a declared owned work plan.
        errors=[e for e in errors if e not in ('missing:gap_plan','missing:automation_limits')]
        if record.get('readiness') not in ('draft','ready'):
            errors.append('invalid_readiness')
        if record.get('readiness')=='draft' and not record.get('gap_plan'):
            errors.append('draft_without_gap_plan')
        if record.get('readiness')=='ready':
            fields=(['guidance_refs','manual_test_refs'] if kind=='foundation_coverage' else
                ['design_requirement_refs','technical_technique_refs','methodology_refs','reference_implementation_refs','manual_test_refs','automation_assessment_ref','user_act_script_refs'])
            for field in fields:
                if not record.get(field):errors.append('ready_without:'+field)
        if kind=='foundation_coverage':
            mode=record.get('automation_class')
            if mode not in workflow['system_requirements']['automation_classes']:
                errors.append('invalid_automation_class')
            elif mode=='manual_primary':
                if not record.get('automation_limits'):errors.append('manual_primary_without_reason')
            elif record.get('readiness')=='ready' and not record.get('automation_test_refs'):
                errors.append('automation_claim_without_test_refs')
    return errors

def fixtures():
    ev={k:'fixture_value' for k in workflow['record_contracts']['evidence']}
    ev.update(actual_result='fail',synthetic=False)
    decision={k:'fixture_value' for k in workflow['record_contracts']['decision']}
    decision.update(synthetic=False,workflow_state='approved')
    tests=[
        ('real-shaped failed evidence accepted', 'evidence',ev,True,[]),
        ('synthetic evidence rejected for real use','evidence',{**ev,'synthetic':True},True,['synthetic_evidence_in_real_context']),
        ('not-applicable needs scope reason','evidence',{**ev,'actual_result':'not_applicable'},True,['not_applicable_without_reason']),
        ('tool error preserved as own class','evidence',{**ev,'actual_result':'tool_error'},True,[]),
        ('approved decision needs reference','decision',{**decision,'authenticated_approval_reference':None},True,['approved_without_reference']),
        ('synthetic decision excluded from real use','decision',{**decision,'synthetic':True},True,['synthetic_decision_in_real_context']),
        ('unknown result rejected','evidence',{**ev,'actual_result':'all_accessible'},True,['invalid_result']),
        ('qualified not-applicable shape accepted','evidence',{**ev,'actual_result':'not_applicable','scope_reason':'Fixture scope excludes this feature'},True,[])]
    foundation={k:'fixture_value' for k in workflow['record_contracts']['foundation_coverage']}
    foundation.update(readiness='ready',automation_class='manual_primary',automation_test_refs=[],gap_plan=None)
    component={k:'fixture_value' for k in workflow['record_contracts']['component_coverage']}
    component.update(readiness='ready',gap_plan=None)
    tests += [
        ('manual-primary coverage with reason accepted','foundation_coverage',foundation,False,[]),
        ('manual-primary coverage needs reason','foundation_coverage',{**foundation,'automation_limits':None},False,['manual_primary_without_reason']),
        ('automation claim needs test references','foundation_coverage',{**foundation,'automation_class':'direct'},False,['automation_claim_without_test_refs']),
        ('ready component needs user ACT-style references','component_coverage',{**component,'user_act_script_refs':[]},False,['ready_without:user_act_script_refs'])]
    results=[]
    for name,kind,record,real,expected in tests:
        actual=record_errors(kind,record,real)
        results.append({'name':name,'pass':sorted(actual)==sorted(expected),'expected':expected,'observed':actual})
    return results

def check():
    errors=[];counts={}
    sources=catalogue['sources']; source_ids={s['id'] for s in sources}
    counts['sources']=len(sources);counts['repositories']=len({s['repository'] for s in sources})
    if len(source_ids)!=len(sources):errors.append('duplicate source IDs')
    all_steps=workflow['stages']+sum(workflow['variants'].values(),[])
    ids=[x['id'] for x in all_steps]
    if len(ids)!=len(set(ids)):errors.append('duplicate stage IDs')
    known=set(ids); route_ids={r['id'] for r in workflow['routes']}
    for s in sources:
        if not re.fullmatch('[0-9a-f]{40}',s['resolved_commit_sha']):errors.append(s['id']+': commit shape')
        if '/blob/'+s['resolved_commit_sha']+'/' not in s['resolved_url']:errors.append(s['id']+': resolved URL mismatch')
        if not set(s['used_by'])<=known:errors.append(s['id']+': undefined consumer')
        expected={p['id'] for p in all_steps if s['id'] in p['source_ids']}
        if set(s['used_by'])!=expected:errors.append(s['id']+': stale used_by')
    required=['id','trigger','prerequisites','activities','human_owner','ai_action','permission_reference','evidence_required','exit_condition','next_route','return_route','source_ids']
    for p in all_steps:
        for key in required:
            if not p.get(key):errors.append(p['id']+': missing '+key)
        if not set(p['source_ids'])<=source_ids:errors.append(p['id']+': undefined source')
        if p['next_route'] not in known:errors.append(p['id']+': unknown next stage')
        if not set(p.get('stage_ids',[]))<={s['id'] for s in workflow['stages']}:errors.append(p['id']+': unknown shared stage')
        owner=ROOT/(workflow['stage_owner'] if p['id'].startswith('P') else workflow['variant_owner'][p['runbook']])
        text=owner.read_text()
        if not re.search(r'^#{2,3} '+p['id']+r' — '+re.escape(p['title'])+r'$',text,re.M):errors.append(p['id']+': heading mismatch')
        # Per-section source lists should agree with the machine representation.
        section=text.split(p['id']+' — '+p['title'],1)[1].split('\n##',1)[0]
        if set(re.findall(r'\[(S\d+)\]',section))!=set(p['source_ids']):errors.append(p['id']+': source list mismatch')
    routing=(ROOT/'framework/decision-routing.md').read_text()
    for r in workflow['routes']:
        if r['stage'] not in known or r['follow_up'] not in known:errors.append(r['id']+': bad route stage')
        if f'| {r["id"]} |' not in routing:errors.append(r['id']+': missing Markdown route')
    for gate in workflow['gates']:
        if gate['failure_route'] not in route_ids:errors.append(gate['id']+': undefined failure route')
    systems=workflow['system_requirements']
    if not set(systems['source_ids'])<=source_ids:errors.append('systems: undefined source')
    if systems['scope']!=['employee','customer']:errors.append('systems: both runbooks required')
    if len(systems['brand_purposes'])!=6:errors.append('systems: six brand purposes required')
    for kind in ('foundation','component'):
        if systems[kind+'_fields']!=workflow['record_contracts'][kind+'_coverage']:
            errors.append('systems: '+kind+' record contract mismatch')
    for key in ('owner_document','template'):
        if not (ROOT/systems[key]).is_file():errors.append('systems: missing '+key)
    index=(ROOT/'sources/README.md')
    if not index.exists() or index.read_text()!=source_index():errors.append('source Markdown view differs from catalogue')
    local_links=0
    for p in ROOT.rglob('*.md'):
        content=p.read_text()
        if content.count('```')%2:errors.append(str(p.relative_to(ROOT))+': unbalanced fences')
        if re.search(r'(?m)^\|.*\|\n\n\|',content):errors.append(str(p.relative_to(ROOT))+': interrupted Markdown table')
        if re.search(r'<!-- SOURCE_CATALOGUE -->|\bTODO\b|\.\.\.\s*\)',content):errors.append(str(p.relative_to(ROOT))+': unresolved placeholder/truncated link')
        for link in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',content):
            if urlsplit(link).scheme:continue
            dest,_,anchor=link.partition('#');target=(p.parent/unquote(dest)).resolve() if dest else p
            local_links+=1
            if not target.is_relative_to(ROOT):errors.append(str(p.relative_to(ROOT))+': outside-root link '+link)
            elif not target.exists():errors.append(str(p.relative_to(ROOT))+': missing link '+link)
            elif anchor and target.suffix=='.md':
                headings={slug(m) for m in re.findall(r'^#{1,6}\s+(.+)$',target.read_text(),re.M)}
                if unquote(anchor) not in headings:errors.append(str(p.relative_to(ROOT))+': missing anchor '+link)
    counts.update(stages=len(workflow['stages']),variant_steps=len(all_steps)-len(workflow['stages']),routes=len(route_ids),local_links=local_links,files=len(list(p for p in ROOT.rglob('*') if p.is_file())))
    return counts,errors

def report(counts,errors,tests):
    ok=not errors and all(t['pass'] for t in tests)
    lines=['# Validation report','**Run date:** 8 November 2026. **Package:** '+workflow['framework_version']+' draft.','## Executed structural checks',f'**Result:** {"PASS" if ok else "FAIL"}. The checker parsed both YAML files, checked IDs, required stage fields, transitions/references, source-consumer relationships, source index parity, Markdown stage/source parity, system-assurance contracts and local links/anchors.', '| Check | Observed |','| --- | --- |']
    lines += [f'| {k.replace("_"," ")} | {v} |' for k,v in counts.items()]
    lines += ['## Executed synthetic record-shape fixtures','These fixtures exercise the checker, not an agent or workflow runtime. Values are invented and never evidence for a real service.','| Fixture | Expected condition | Observed result |','| --- | --- | --- |']
    lines += [f'| {t["name"]} | {", ".join(t["expected"]) or "shape accepted"} | {"PASS" if t["pass"] else "FAIL"} |' for t in tests]
    lines += ['## Source retrieval and review',f'All {counts["sources"]} catalogue entry-point files across {counts["repositories"]} repositories were retrieved through the connected GitHub service at the recorded commits on 8 November 2026. Current default branch metadata was resolved before retrieval. The catalogue retains actual commit and blob identifiers separately. No external downstream link audit, primary-law verification or exhaustive source-content review is claimed.','## Manual desk review','The authored routes were compared with the 17 [acceptance scenarios](acceptance-scenarios.md), the two runbooks and synthetic examples. This establishes that the specified handling is described; no independent person or executing agent was tested against the scenarios.','## Limits and open adoption work','The checker cannot authenticate approvals, verify evidence truth, distinguish a real approval reference from a plausible string, establish legal applicability, validate source rights, enforce runtime permissions or prove programme/user outcomes. It checks reference presence and declared shape only, including declared system coverage; a referenced asset may still be inadequate. It performs no live external link fetches.','Independent accessibility/usability review, affected-person participation in a real pilot, local role/delegation and data-control adoption, actual source baselines for local decisions, named maintenance and licence selection remain pending. See [adoption](../ADOPTION.md). No production system or remote repository was changed.']
    if errors:lines+=['## Errors']+['- '+e for e in errors]
    output='\n\n'.join(lines)+'\n'
    while re.search(r'(?m)^\|.*\|\n\n\|',output):
        output=re.sub(r'(?m)(^\|.*\|)\n\n(?=\|)',r'\1\n',output)
    return output

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write-source-index',action='store_true');parser.add_argument('--write-report',action='store_true');args=parser.parse_args()
    if args.write_source_index:(ROOT/'sources/README.md').write_text(source_index())
    if args.write_report and not (ROOT/'validation/report.md').exists():(ROOT/'validation/report.md').write_text('# Validation report\n\nPending execution.\n')
    counts,errors=check();tests=fixtures()
    if args.write_report:(ROOT/'validation/report.md').write_text(report(counts,errors,tests))
    result={'counts':counts,'errors':errors,'fixtures_passed':sum(t['pass'] for t in tests),'fixtures_total':len(tests)}
    print(json.dumps(result,indent=2));sys.exit(1 if errors or not all(t['pass'] for t in tests) else 0)
