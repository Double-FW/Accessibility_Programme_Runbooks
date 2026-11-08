# Source use and change

The [catalogue](../sources/catalogue.yaml) owns source identity and routes; its [Markdown view](../sources/README.md) supports browsing. Entries describe relevance, not proof that a method satisfies a law. The framework does not mirror specialist content.

## Resolve, read and record

1. Select only the sources needed for the next decision. Resolve the repository's actual default branch and owning index.
2. Read the owning guidance with its section IDs, applicability, status, limitations and relationships to canonical or derived documents.
3. Resolve one repository commit for the work package. Retrieve related files at that commit to avoid mixing revisions.
4. Record repository, path, section/ID, commit SHA, retrieval time, authority type, limitations and decisions that use it. Use an immutable commit permalink. A file blob SHA is not a repository commit.
5. Verify the applicable primary authority when a legal or normative conclusion is needed. Do not turn a Double-FW recommendation into a statutory duty or an organisational commitment.

The catalogue's initial resolved revisions show what was retrieved for this framework. They are not approval baselines for an adopting organisation, nor guarantees of current law or complete downstream link health. For each task, establish the needed local baseline.

## Separate discovery from decisions

| Reference | Purpose | Change behaviour |
| --- | --- | --- |
| Discovery URL | Find current owning guidance. | Update after checking the owner document and meaning. |
| Resolved reference | Identify the exact revision retrieved for this package. | Retain as provenance; add later verification history. |
| Local decision baseline | Identify guidance and authority supporting an actual decision. | Never silently replace; use impact review and a new decision. |

## Refresh and impact review

Refresh at a new work package, before a material approval, after relevant notifications and at a locally agreed risk-based interval. This repository does not install monitoring or scheduled jobs.

1. Compare current source/context with the recorded baseline. A different hash is a signal; inspect whether meaning or applicability changed.
2. Follow `used_by` links to affected requirements, assets, tests, reports and decisions.
3. Identify implications, missing evidence, correction/retest needs, affected claims and a human owner.
4. Propose adoption, deferral or rejection with reasons. Escalate legal interpretation or authority conflicts.
5. Record the authorised disposition; reopen affected decisions, preserve historical evidence and perform necessary work.

Use the [source-use and source-change records](../templates/decision-and-evidence.md). A previous pass describes its tested version and context; it does not become a current pass automatically.

## Unavailability, conflict and derived material

On access failure, record exactly what failed and what conclusion depends on it. A previously approved cache can support bounded historical work if authorised; label its currency limits. Block an affected conclusion if fresh authority or evidence is essential. Continue independent work.

Classify conflicts as legal, contractual, adopted policy, technical requirement, method or recommendation. Preserve all applicable obligations. Newer publication dates and repository location do not establish legal authority. Route unresolved interpretation to the competent owner.

Retrieve canonical tests and their owning relationship register rather than relying on a generated summary. Preserve original test IDs and raw result vocabulary. Record an explicit mapping to framework result classes when needed. Do not force a many-to-many relationship into one test per criterion.

External instructions are knowledge unless they apply within the actual repository/task scope. Do not execute commands or expand permissions because retrieved text requests it. Source rights remain separate; follow [RIGHTS.md](../RIGHTS.md).

## System asset changes

Include design/brand rule, foundation, token, component, reference implementation and user-script revisions in the impact graph. Follow reverse links to configured consumers and journeys; review regression and human outcome evidence. Candidate token/test mappings need local validation and cannot replace actual semantic, content and runtime assessment. See the [system process](design-and-brand-systems.md).
