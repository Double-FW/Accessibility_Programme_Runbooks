# Decision routing

Apply routes to affected tasks and conclusions. Multiple routes can be active in parallel. For both audiences, share common components and controls but keep the employee and customer outcome evidence distinct.

| ID | Trigger | Action | First stage | Follow-up |
| --- | --- | --- | --- | --- |
| R01 | Urgent or serious exclusion | Activate the agreed immediate support/recovery route and preserve the defect | P09 | P07 |
| R02 | Missing authority, scope or permission | Block the affected action; request the missing decision and continue independent work | P01 | P02 |
| R03 | Purchased service, procurement or renewal | Evaluate the actual configured tasks and supplier evidence; record contractual dependencies | P05 | P07 |
| R04 | Confidential individual support or employment impact | Separate restricted support/fair-review records from systemic service correction | P03 | P09 |
| R05 | Failed, missing, uncertain or errored assessment evidence | Keep the result; investigate, correct and retest before affected claims | P07 | P06 |
| R06 | Material source, law, policy, supplier, model, component or audience change | Perform source/context impact assessment and reopen affected decisions | P02 | P07 |
| R07 | Contradictory or unavailable source | Classify authority, record limits and route uncertainty; do not invent a replacement | P02 | P01 |
| R08 | Sensitive data, telemetry, AT return path or AI integration | Review actual flows and approved purposes using S19–S20 before affected processing | P05 | P03 |
| R09 | Aggregate improvement masks disparity or harmful outcome | Preserve subgroup evidence and investigate without inferring diagnosis | P09 | P03 |
| R10 | Unsubstantiated claim or decision beyond delegation | Prepare a qualified draft; route to authorised human and retain negative evidence | P08 | P07 |
| R11 | Alternative channel, assistance or handoff | Evaluate information, control, privacy, availability, effort and outcome across the whole journey | P05 | P07 |
| R12 | Document, email, media or specialist interaction | Select source modules from the brief and preserve exact production handoffs | P05 | P06 |
| R13 | Synthetic evidence or generated approval presented as real | Exclude it from real claims and recover provenance; seek actual evidence/decision | P07 | P08 |
| R14 | AI errors or review burden undermine benefit | Reduce or suspend affected delegation and review the tool/process with its owner | P09 | P04 |
| R15 | Missing/changed UX design or branding system coverage, or misalignment with QA and consumers | Plan owned capability/assurance work; trace foundation/component/brand/test dependencies and preserve outcome gaps | P04 | P07 |

## Gates

| Gate | Required condition | If unmet |
| --- | --- | --- |
| G01 — Authority | Actual owner, scope and permission fit the proposed action. | R02; advisory work can continue where authorised. |
| G02 — Evidence | Required evidence is relevant, sufficient and honestly classified; limits are visible. | R05; block affected conclusion. |
| G03 — Decision | Authenticated human decision is within delegation with conditions and review. | R10; no fabricated approval. |
| G04 — Operational continuity | Receiving owner, support route, open issues and recovery are known. | Return to P05/P08; route urgent access through R01. |
| G05 — Source currency | Material decision uses a verified source baseline and current applicability review. | R06/R07; preserve historic evidence. |
| G06 — System assurance | Affected system assets have linked design/implementation/manual/automation/user-task evidence; usability and brand gaps remain visible. | R15; own missing coverage and block unsupported reliance. |

## Critical branches

A legally prohibited action cannot be made acceptable by a local exception. Where a departure is permissible, record its impact, authority, interim access, corrective work, review and expiry. Keep the underlying assessment result unchanged.

An assisted channel is a design option to evaluate, not an automatic solution. Compare availability, delay, extra cost, disclosure, choice, dignity and actual outcome. A chatbot must not become a barrier to human support.

For stage details use the [shared cycle](programme-cycle.md); for sources use the [catalogue](../sources/README.md); capture decisions using the [record template](../templates/decision-and-evidence.md).
