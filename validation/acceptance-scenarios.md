# Acceptance scenarios

**Status:** authored process walkthroughs, not independent human review, agent execution or operational acceptance. Structural fixture results are reported separately in [report.md](report.md).

For each scenario, the expected route was checked against the authored documents and examples. Observation below means that the specified route is present and internally consistent; it does not mean a person or agent successfully performed it in practice.

| ID | Input/trigger | Expected routing | Required behaviour | Desk-review observation |
| --- | --- | --- | --- | --- |
| AC01 | Small employer with inaccessible payroll and no specialist team | E02/E04; R01/R03/R04 | Separate immediate support, systemic correction, supplier dependency and restricted case records. | Employee example explicitly routes all four; actual support quality not tested. |
| AC02 | Front end passes but authentication/payment/support fails | C05; R05/R11 | Retain end-to-end failure; scan cannot establish journey success. | Customer example retains scoped failure despite synthetic scan pass. |
| AC03 | One component serves employees and customers | Both runbooks; P04/P07 | Share remediation and resources; evaluate distinct tasks and keep data permissions separate. | README and routing permit both; independent real-world trial pending. |
| AC04 | Automation passes while manual, AT or user task fails | P07/P08; R05 | Preserve failed result and block unsupported pass/claim. | Shared cycle and both examples return to correction; no live tools executed. |
| AC05 | Owning source changes after an approved decision | R06; P02/P07 | Trace used_by, review meaning, reopen affected decisions and preserve history. | Customer example and source-change record show proposed handling. |
| AC06 | Broken dependency, conflicting guidance or unknown jurisdiction | R02/R07 | Record access/authority gap; block affected conclusion and continue independent work. | Source-change guidance and gates explicitly preserve this path. |
| AC07 | Agent has tool access but no execution delegation | G01; R02 | Draft reviewable work only within mandate; no invented execution permission. | Responsibilities and employee exercise distinguish advisory from execution. |
| AC08 | Generated approval or synthetic result enters a real claim | R13; G02/G03 | Exclude synthetic evidence; require actual authenticated decision and provenance. | Checker fixture rejects synthetic evidence in real mode; authentication itself is outside checker scope. |
| AC09 | Request infers disability from telemetry or ranks workers | R08; E03/C02 | Do not profile/rank; propose ethical task/context research for the legitimate service aim. | Runbooks, prompt and reporting rules retain that alternative. |
| AC10 | Document/video production starts | R12; P05/P06 | Commission accessibility at brief; preserve asset versions, editorial and distributed-output checks. | Customer exercise and production source routes include the handoffs. |
| AC11 | Aggregate satisfaction improves while a group is excluded | R09; C06 | Keep disparity, sample limits and failed requirements visible; investigate. | Customer example retains this conflict without claiming causation. |
| AC12 | AI produces plausible wrong citations or excessive corrections | R14; P09/P04 | Verify claims, measure review burden and reconsider tool/delegation. | Responsibilities and reporting provide explicit stop/review path; real benefit evaluation pending. |
| AC13 | Foundation has no manual procedure or meaningful automation coverage | P05/P07; R15/G06 | Require manual coverage plus direct/partial checks or a justified manual-primary assessment; keep missing work owned. | System process/plan require the relationships; shape fixtures check automation limits. |
| AC14 | Component marked ready without requirements, reference implementation or user ACT-style script | P05–P08; R15/G06 | Retain gap and block unsupported reliance on readiness; plan actual assets in owning systems. | Component fields and readiness fixture retain missing user-script coverage; asset adequacy still needs human evaluation. |
| AC15 | Accessibility remediation removes distinctive brand purpose/identity | P04/P06/P07; R15 | Compare inclusive options that preserve purpose/recognition and evaluate all six brand ambitions, not just technical conformance. | Brand-system process and reporting require purpose and communication outcomes; real creative/user review pending. |
| AC16 | Typography, colour, label or brand-rule change affects many components | P09; R06/R15 | Trace many-to-many consumers and trigger proportionate regression and human outcome review. | Source-change and system process require reverse dependency handling. |
| AC17 | Existing vendor/shared system is available but its configured use is unverified | P03–P08; R03/R15 | Evaluate adoption instead of mandating a new system; verify configured assets, content, variants and complete journeys. | Both runbooks and system process preserve this distinction. |

## Pilot evidence still needed

Have representative employees/customers and operational teams use the runbooks on an agreed task. Observe comprehension, navigation, actual decision/handoff quality, data handling, missing evidence and accessibility of AI and non-AI routes. Include at least one adverse outcome or blocked dependency.

Record actual participants and permissions in approved systems, agreed success criteria, methods, observations, limitations, dissent and resulting edits. Independently review material evidence and control decisions. Do not count this document or synthetic fixtures as lived-experience validation.
