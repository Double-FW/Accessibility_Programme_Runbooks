# Validation

The package includes an offline structural checker. It requires Python 3.10 or later and PyYAML; install the dependency in your normal approved environment if needed. The delivery run used Python and PyYAML already available in the workspace.

From the repository root:

```bash
python3 validation/check.py
```

After editing the source catalogue, regenerate its Markdown view and check:

```bash
python3 validation/check.py --write-source-index
```

To write a structural validation report for this draft package:

```bash
python3 validation/check.py --write-report
```

The report text includes this package's original source-retrieval and desk-review scope. For a later release, update those dated narrative statements to describe work actually performed; running the checker does not refresh source retrieval or perform desk review.

## What is checked

- YAML parsing, stable ID uniqueness, required stage fields and valid referenced routes.
- Matching stage headings/source lists in Markdown and YAML.
- Source revision format, resolved URL consistency and forward/reverse consumer relationships.
- Generated source-index parity, Markdown file links/anchors, fence balance and obvious unfinished link markers.
- Twelve synthetic record-shape fixtures covering synthetic evidence, missing approval-reference presence, not-applicable reasoning, unsupported results and explicit tool-error classification, manual-primary coverage reasons, automation references and component user ACT-style coverage.

The checker does not operate services, authenticate approvals, verify evidence truth, fetch external links or establish legal compliance. Its reference and record-shape checks are not an execution engine or runtime gate enforcement.

See [acceptance scenarios](acceptance-scenarios.md) for the separate behavioural expectations and [report](report.md) for actual observations and limits. A real pilot with affected people and operational owners is still required before claims of practical effectiveness.
