# Decision and evidence records

**Templates — complete in approved local systems. Blank fields are not approvals.**

Use stable local IDs. Link each requirement/outcome to source use, assets and evidence, then to a decision, action and outcome review. Avoid copying source content or sensitive operational evidence into this public repository. The structured field contract is in [programme.yaml](../workflows/programme.yaml).

## Stage/task record

```yaml
id: null
runbook: null # employee, customer or shared
stage_id: null # P01-P09, E01-E06 or C01-C06
trigger: null
scope: null
prerequisites: []
source_ids: []
human_owner: null
ai_action: null
permission_reference: null
evidence_required: []
exit_condition: null
next_route: null
workflow_state: draft
```

## Source-use record

```yaml
id: null
source_id: null
repository: null
path: null
section_or_id: null
resolved_commit_sha: null
retrieved_at: null
authority_type: null
source_review_status: null
limitations: null
used_by: []
resolved_url: null
```

Resolve owning source and actual default branch, read qualifications, then pin the repository commit used. Primary legal/standard references may need additional local authority records alongside Double-FW routing guidance.

## Evidence record

```yaml
id: null
requirement_or_outcome_id: null
method: null
actual_result: null # framework class; raw vocabulary retained below
raw_result: null
source_vocabulary: null
mapping_reason: null
environment: null
date: null
coverage: null
limitations: null
evidence_location: null # approved secure location
collector: null
review_status: null
synthetic: false # only false for actual evidence; never relabel synthetic data
```

Framework assessment classes are `pass`, `fail`, `not_assessed`, `blocked`, `not_applicable`, `inconclusive`, `tool_error`. Retain the source result and reason for mapping. Not applicable needs scope reasoning; cannot tell and tool error must not become passes. An evidence class is not a compliance or release decision.

## Decision and handoff record

```yaml
id: null
scope: null
options: []
evidence_ids: []
source_use_ids: []
decision_owner: null
decision: null
authenticated_approval_reference: null
conditions: null
receiving_owner: null
review_trigger: null
synthetic: false
workflow_state: draft
```

Capture the actual decision and authority exercised, affected versions, known failures, dissent and open questions. Reference the authenticated organisational record; a string in this file cannot authenticate it. Handoff is accepted by the actual receiving owner, not merely generated.

## Exception record

```yaml
id: null
barrier: null
affected_people_and_tasks: null
impact: null
interim_access: null
owner: null
authority: null
corrective_action: null
expiry_or_review: null
retest_needed: null
```

Check whether a departure is legally/contractually permissible and within delegation before recording approval. Keep underlying failures unchanged. Time-limited exceptions need expiry as well as review and corrective action; escalate above authority or risk limits. This is not an exemption-creation mechanism.

## Delegation record

```yaml
id: null
purpose: null
human_owner: null
level: null # A0, A1, A2 or A3
permitted_actions: []
targets: []
data_access: null
environment: null
delegation_reference: null
limits: null
verification: null
stop_conditions: null
recovery: null
```

## Source-change record

```yaml
id: null
source_id: null
old_baseline: null
new_candidate: null
changed_meaning: null
affected_records: []
impact: null
evidence_needed: null
owner: null
disposition: pending
approval_reference: null
review_trigger: null
```

Trace `used_by` from source to requirements, assets, evidence, reports and decisions. Preserve earlier records and limitations. Follow [source change](../framework/source-use-and-change.md) rather than overwriting the approved baseline.

## System coverage records

Use the [system-assurance plan](system-assurance-plan.md). The workflow defines `foundation_coverage` and `component_coverage` fields for references, ownership, evidence and gaps. `readiness: draft` can retain missing assets only with an owned gap plan; readiness is not a test result or approval. Before relying on a record as `ready`, verify the actual referenced assets, applicable checks and outcome evidence. Manual-primary foundations still require manual procedures and a substantive automation-limit explanation.
