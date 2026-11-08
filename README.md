# Accessibility Programme Runbooks

**Double FW Ltd · Draft 0.2.0 · 8 November 2026 · For local review and pilot adoption**

Design and manage an accessibility programme using people and authorised AI, with two entry points and one shared process. The intended outcome is equitable participation, equivalent experience and satisfaction, supported by applicable obligations and evidence.

## Choose a runbook

| Programme | Start here | Main concern |
| --- | --- | --- |
| Employee-facing services and systems | [Employee runbook](runbooks/employee-services.md) | Complete work activities, cumulative barriers and confidential support. |
| Customer-facing services and systems | [Customer runbook](runbooks/customer-services.md) | End-to-end service journeys, meaningful choice, support and exit. |
| Both | Use both runbooks with one [programme plan](templates/programme-plan.md) | Shared components and resources; distinct outcomes and appropriate data boundaries. |

## Start in six actions

1. Choose one priority activity and use the [organisation profile](templates/organisation-profile.md) to capture known facts. An urgent barrier can start immediately through the agreed support route.
2. Confirm the human owner and next decision. Use [responsibilities](framework/human-ai-responsibilities.md) to bound AI support.
3. Follow the relevant runbook and [shared cycle](framework/programme-cycle.md). Enter at the current trigger; return to earlier stages when evidence changes.
4. Retrieve the relevant owning guidance through the [source catalogue](sources/README.md). Record the exact revision used and its limitations.
5. Use the [programme plan](templates/programme-plan.md), [decision/evidence record](templates/decision-and-evidence.md) and [report](templates/report.md). Keep live records in approved organisational systems.
6. Review the evidence, make an authorised decision, hand over to operations and use feedback to improve.

People can use every document without software. For an AI-assisted planning session, use the [programme-design prompt](prompts/design-programme.md). [AGENTS.md](AGENTS.md) governs contribution and AI interpretation in this repository; it grants no organisational permissions.

## Required system capabilities

Both programmes must plan for accessible UX design systems and accessible branding systems, with QA traceability for foundations, patterns/components and complete journeys. Plan guidance, manual and meaningful automatable checks, design requirements, techniques, methodologies, reference implementations and user ACT-style scripts through the [system process](framework/design-and-brand-systems.md) and [assurance plan](templates/system-assurance-plan.md). Preserve brand purpose and evaluate accessible usability as well as conformance. Detailed assets stay in their owning systems.

## What belongs where

| Owner | Material |
| --- | --- |
| This framework | Stage structure, routing, responsibilities, record relationships, templates and examples. |
| Specialist Double-FW repositories | Detailed regulatory explanations, design guidance, test procedures and content production practices. |
| Adopting organisation | Verified scope, adopted policy, budgets, delegation, applicable obligations, real evidence and decisions. |

The [source-change process](framework/source-use-and-change.md) separates current discovery links from the revisions supporting previous decisions. No detailed guidance is mirrored here. The 33 source entry points were retrieved at the revisions in the catalogue; this is not an audit of all linked material or a legal determination.

## Contents

- [Decision routing](framework/decision-routing.md)
- [Reporting and learning](framework/reporting-and-learning.md)
- [Machine-readable workflow definitions](workflows/programme.yaml)
- [Employee synthetic example](examples/employee-synthetic.md) and [customer synthetic example](examples/customer-synthetic.md)
- [Acceptance scenarios](validation/acceptance-scenarios.md) and [validation report](validation/report.md)
- [Adoption and maintenance](ADOPTION.md), [contributing](CONTRIBUTING.md), [rights status](RIGHTS.md) and [changelog](CHANGELOG.md)

## Adoption state

The files and structural checker are implemented. The YAML is a data definition, not an agent runner, integration or enforcement service. Structural checks cannot establish evidence truth, authenticate approvals, establish legal compliance or demonstrate practical programme effectiveness. Independent review and an organisational pilot are pending. No live organisation's authority, funding or staffing is asserted.
