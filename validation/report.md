# Validation report

**Run date:** 8 November 2026. **Package:** 0.2.0 draft.

## Executed structural checks

**Result:** PASS. The checker parsed both YAML files, checked IDs, required stage fields, transitions/references, source-consumer relationships, source index parity, Markdown stage/source parity, system-assurance contracts and local links/anchors.

| Check | Observed |
| --- | --- |
| sources | 33 |
| repositories | 28 |
| stages | 9 |
| variant steps | 12 |
| routes | 15 |
| local links | 333 |
| files | 29 |

## Executed synthetic record-shape fixtures

These fixtures exercise the checker, not an agent or workflow runtime. Values are invented and never evidence for a real service.

| Fixture | Expected condition | Observed result |
| --- | --- | --- |
| real-shaped failed evidence accepted | shape accepted | PASS |
| synthetic evidence rejected for real use | synthetic_evidence_in_real_context | PASS |
| not-applicable needs scope reason | not_applicable_without_reason | PASS |
| tool error preserved as own class | shape accepted | PASS |
| approved decision needs reference | approved_without_reference | PASS |
| synthetic decision excluded from real use | synthetic_decision_in_real_context | PASS |
| unknown result rejected | invalid_result | PASS |
| qualified not-applicable shape accepted | shape accepted | PASS |
| manual-primary coverage with reason accepted | shape accepted | PASS |
| manual-primary coverage needs reason | manual_primary_without_reason | PASS |
| automation claim needs test references | automation_claim_without_test_refs | PASS |
| ready component needs user ACT-style references | ready_without:user_act_script_refs | PASS |

## Source retrieval and review

All 33 catalogue entry-point files across 28 repositories were retrieved through the connected GitHub service at the recorded commits on 8 November 2026. Current default branch metadata was resolved before retrieval. The catalogue retains actual commit and blob identifiers separately. No external downstream link audit, primary-law verification or exhaustive source-content review is claimed.

## Manual desk review

The authored routes were compared with the 17 [acceptance scenarios](acceptance-scenarios.md), the two runbooks and synthetic examples. This establishes that the specified handling is described; no independent person or executing agent was tested against the scenarios.

## Limits and open adoption work

The checker cannot authenticate approvals, verify evidence truth, distinguish a real approval reference from a plausible string, establish legal applicability, validate source rights, enforce runtime permissions or prove programme/user outcomes. It checks reference presence and declared shape only, including declared system coverage; a referenced asset may still be inadequate. It performs no live external link fetches.

Independent accessibility/usability review, affected-person participation in a real pilot, local role/delegation and data-control adoption, actual source baselines for local decisions, named maintenance and licence selection remain pending. See [adoption](../ADOPTION.md). No production system or remote repository was changed.
