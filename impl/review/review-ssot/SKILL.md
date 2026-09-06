---
name: review-ssot
description: Review uncommitted changes for duplicated logic, data, configuration, and single-source-of-truth issues.
---

# Review Single Source of Truth

Review uncommitted changes without changing code, configuration, tests, or documentation. The user decides whether to apply findings.

If there are no uncommitted changes, report that and stop. Start with the diff, then trace only the relevant definitions, consumers, contracts, and tests. Report a finding only when two locations own the same semantic fact or rule and can be changed independently, or when a new source competes with an established owner. Cite file paths and line numbers, explain the divergence risk, separate facts, inferences, and unknowns when material, and name one concrete canonical owner plus how other uses should derive from it. Do not report repeated syntax, copied presentation data, independent local values, or intentional snapshots unless evidence shows meaningful maintenance or correctness risk.

## Decision procedure

Evaluate each suspected duplicate in this order:

1. Do the locations represent the same semantic fact, business rule, persisted data, configuration, or derived state?
   - No or unknown: no finding. Repeated syntax, copied presentation data, harmless literals, and independent local values are excluded.
2. Is one location mechanically generated or derived from the other?
   - Yes or unknown: no finding. Generated output, intentional snapshots, and aliases are excluded.
3. Can the locations be independently changed or updated?
   - No or unknown: no finding.
4. Is there concrete evidence that independent changes can diverge?
   - No or unknown: no finding. Evidence may include distinct values or logic, separate update paths or consumers, a new copy, or bypassing a shared API.
5. Can a concrete canonical owner be identified?
   - No or unknown: no finding. Do not infer ownership from naming alone.
6. Classify the impact:
   - Inconsistent externally visible behavior, security decisions, data integrity, or lifecycle behavior: `Must`.
   - Clear maintenance divergence risk without `Must` impact: `Recommended`.
   - Small impact where safe consolidation removes the evidenced risk without needless abstraction: `Optional`.
   - No concrete impact: no finding.

Each finding must cite both locations, evidence that they mean the same thing, evidence that independent changes can diverge, the concrete canonical owner, and the smallest fix for other uses to derive from or consume that owner.

## Must

- Two independently mutable or independently updated locations represent the same semantic fact, business rule, persisted data, configuration, or derived state, concrete evidence shows they can diverge, and the divergence can affect externally visible behavior, security decisions, data integrity, or lifecycle behavior. Cite both locations, the divergence evidence, canonical owner, and affected consumers or contract.

## Recommended

- Independently updated copies of the same business rule, configuration, schema, mapping, default, or derivation have concrete evidence of maintenance divergence and a clear canonical owner, but no `Must` impact.
- Changed code adds a competing source or bypasses an existing canonical API, with evidence that independent updates could produce inconsistent behavior.
- Flag constants, schemas, mappings, or defaults only when they are authoritative or likely to be edited independently; do not flag repeated syntax, harmless literals, one-use local calculations, copied presentation data, generated output, intentional snapshots, or aliases.

## Optional

- Small-impact duplication may be reported only when one owner is clearly authoritative, the evidence above establishes a real divergence risk, and safe consolidation removes that risk without introducing needless abstraction. Otherwise report no finding.

## Output

Group findings by `Must`, `Recommended`, then `Optional`. For each finding include Location, Problem, Impact, Recommended change, and Evidence. Evidence must identify the competing definitions or consumers and why independent updates can diverge. Recommend the smallest concrete fix: name the canonical owner and state how other uses should consume or derive from it. Avoid duplicate findings for one ownership problem. Return `No findings` when the changes pass this review. Do not ask questions or edit files.
