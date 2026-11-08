# Accessible UX design systems, branding systems and QA

Both runbooks must plan for accessible UX design systems and accessible branding systems as connected organisational capabilities. Their purpose includes accessible usability, equivalent experience and effective brand communication as well as applicable conformance. This file specifies what the programme must organise and evidence; detailed rules, techniques, implementations and test scripts stay in their owning systems or source repositories.

## Plan the systems before dependent delivery

At P03, inventory existing systems, owners, versions, adopters and evidence gaps, including vendor-supplied or shared systems. At P04, explicitly plan adoption, creation, remediation or extension with owners, capacity, priorities and evidence. An organisation need not build its own system if an existing one meets its needs; it must verify that choice and its configured use.

At P05, require a linked assurance plan before dependent design, code, content or procurement commitments. At P06, preserve traceability through implementation and content production. At P07, evaluate the actual foundations, patterns/components and complete journeys. At P08, retain gaps and departures in the authorised decision. At P09, maintain ownership, adoption, versioning, regression and outcome review.

Use the [system-assurance plan](../templates/system-assurance-plan.md). Missing guidance or reference assets become owned gaps with planned work, not invented sources or fabricated evidence. Do not block unrelated authorised delivery or urgent access while capability is improved.

## Foundations and design practices

For **every in-scope foundation or practice**, require a versioned record linking:

1. Its intended user/communication outcome and scope, including relevant contexts, themes and variants.
2. Owning best-practice guidance, applicable requirements and usability rationale, with authority types kept distinct.
3. Manual inspection, AT and/or human evaluation procedures appropriate to the outcome.
4. Automatable checks where meaningful, linked to actual methods and test IDs, with a coverage statement and residual manual checks.
5. A classification of direct automation, partial automation or manual-primary. Record a reason when no meaningful automated assessment exists; never create a token test just to fill a column.
6. Dependencies on other foundations, tokens, content, components, templates and journeys; actual results, limitations, owner and review trigger.

The inventory must explicitly consider typography, colour, labelling/naming, alternative text, content/reading order and the other foundations relevant to the service. This is a scope prompt, not their detailed specification. Relevant areas may also include structure, focus, interaction, motion, spacing, language and multimodal communication.

Automation may check whether a property exists without establishing its quality. Manual-primary classification is not a missing-test exemption: it requires an appropriate human method and evidence. A tool reporting no errors does not establish meaningful alternative text, understandable labelling, coherent reading order or effective brand communication.

## Patterns and components

For **every in-scope pattern or component**, plan linked, versioned references for:

| Required asset | Programme responsibility |
| --- | --- |
| Design requirements | Identify intended tasks, states, variants, contexts, accessible usability and conformance expectations. |
| Technical techniques | Identify implementation approaches, semantics, interaction, platform constraints and applicable technical references without copying them here. |
| Delivery and evaluation methodologies | Define how design, engineering, content and QA collaborate and what each handoff demonstrates. |
| Reference implementations | Identify working versioned implementations, supported environments, evaluated states and known limitations. If unavailable, assign creation/evaluation work. |
| Manual and automatable tests | Link applicable foundation checks, component checks and residual human evaluation; document automation limits. |
| User-oriented ACT-style scripts | Link objective, applicability, setup/context, input or AT mode, task steps, expected observable outcomes, recovery/negative cases and evidence recording in the owning test system. |
| Adoption and change evidence | Identify actual consumers, local variations, departures, defects, retests and retirement/replacement decisions. |

Use [S13](../sources/README.md#s13), [S14](../sources/README.md#s14) and [S32](../sources/README.md#s32) for QA routes. Preserve the source's ACT-style status; a local user-task script is not automatically a formal approved ACT conformance rule. Technical conformance rules and user-oriented task scripts are complementary, and neither replaces research with affected people.

Reference implementations demonstrate only their evaluated version and scope. Reusing a component is not sufficient evidence that its configured content, integrations or complete journey are accessible. Maintain many-to-many traceability: a foundation affects multiple components; a component uses multiple foundations; a test can support several scoped outcomes.

## Branding that fulfils the purpose of a brand

The branding-system workstream must optimise accessible communication while preserving recognisability, distinctiveness, positioning, purpose and values. Accessibility is part of making brand intent effective across ways of perceiving, understanding and interacting. Do not default to removing brand character or imposing a generic visual style.

| Brand purpose | Required planning and outcome question |
| --- | --- |
| Help **everyone identify organisations, products and services** | Plan recognisable identity across relevant formats/modalities. Can people identify who is communicating and what is offered? |
| Build trust with **everyone** | Plan credible, usable communication and consistent service behaviour. What evidence shows confidence and reliability, and where is trust undermined? |
| Set **everybody's expectations** | Plan understandable promises, terms, actions and consequences. Do communications accurately prepare people for the service? |
| Create value for **everyone** | Plan equitable access to the benefit, relevant information and choice. Who remains excluded from the value and why? |
| Reinforce values in **everyone's minds** | Plan consistent expression in communication and actual experience. Are values recognisable and supported by service behaviour? |
| Resonate with **every customer** | Plan inclusive research and creative evaluation across relevant people, languages and contexts. Does the communication feel relevant and respectful? |

These are inclusive ambitions, not a claim that a finite study proves a universal response. Define evaluated audiences and contexts, preserve missing perspectives, and assess recognition, comprehension, trust, expectations, value and resonance separately from technical results. Do not assume a visual identity alone communicates the brand or that WCAG conformance proves brand effectiveness.

Use [S17](../sources/README.md#s17) for brand/CX reasoning, [S18](../sources/README.md#s18) for typography, [S16](../sources/README.md#s16) for cognitive usability and [S19](../sources/README.md#s19) for research/data ethics. Apply the programme's participation and evidence controls. Brand outcomes matter in employee communications and systems as well as customer services.

## Connect QA and maintenance

Maintain references from brand purpose and user outcome to foundations/practices, patterns/components, design requirements, techniques, reference implementation revisions, test/script IDs, actual evidence and consuming journeys. Use [S33](../sources/README.md#s33) only as a candidate dependency map: tokens alone do not determine semantic correctness, content meaning or runtime behaviour.

When a foundation, token, brand rule, component, content practice or reference implementation changes, follow reverse dependencies to affected consumers, perform impact assessment and proportionate regression/research, and reopen affected decisions. Keep unresolved usability and brand outcomes visible even when technical checks pass.

AI can help inventory assets, identify missing links, draft candidate requirements/scripts, propose implementations and organise authorised results. Human design, brand, content, engineering, QA and research owners validate their contributions; actual participants establish experience evidence. Generated documentation, tests or reference code are not evidence of their own effectiveness.
