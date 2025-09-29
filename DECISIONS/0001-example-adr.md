
# 0001 — Example ADR: Choose Deployment Strategy

**Status:** Proposed  
**Date:** <YYYY‑MM‑DD>

## Context
We need a safe, reversible deployment for user‑visible changes.

## Decision
Adopt **feature flags** for all user‑visible changes and use **blue‑green deploys** for services in <env>.

## Consequences
- Faster rollbacks and lower CFR.
- Requires discipline to remove flags post‑validation.

## Alternatives Considered
- Direct deploy without flags (higher risk)
- Canary without flags (partial mitigation)
