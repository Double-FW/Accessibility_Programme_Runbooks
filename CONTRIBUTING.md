# Contributing

Improve routing and process clarity without importing detailed guidance from its owning repository. Suggest specialist changes in the owning source; keep this framework's links and impact relationships aligned.

1. Identify the affected P/E/C/R/S IDs and explain the problem and intended behaviour.
2. Preserve source provenance and distinguish actual evidence, recommendation and hypothesis.
3. Update the owning shared document and corresponding YAML when a process changes. Runbooks should link to shared stages, not copy them.
4. Keep live confidential information out of examples and issues. Label all synthetic examples; no fabricated participants or approvals.
5. Run python3 validation/check.py. After catalogue edits, run python3 validation/check.py --write-source-index first.
6. Revisit affected acceptance scenarios and document what was and was not evaluated. Human review is needed for material policy/evidence/AI-control implications.

Use clear headings, meaningful links, plain language and a textual explanation for each diagram. Public-facing content and generated reports need appropriate accessible production review. Do not claim validation beyond the checks actually performed.

For UX/branding changes, keep the system-assurance fields, stage activities, source links and consumer impacts aligned; do not add detailed system rules to the framework.

For a source move, retain stable S IDs where the same knowledge ownership continues. Update discovery location, resolved revision, review date and limitations after actual retrieval. Add a new ID when meaning or ownership genuinely differs; document migration. Never silently retarget previous decision baselines.

Maintainers and licence terms must be confirmed before public release; see ADOPTION.md and RIGHTS.md.
