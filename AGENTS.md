# AGENTS.md - Rules for AI coding agents

Adapted from secure harness practices (inspired by zeekiankok92/aixtech-agent-harness-demo).

## Scope
- Work only on defined tasks. Keep changes small.
- Never push to main without review. Never weaken security gates.

## Data & Privacy
- Prefer synthetic or public open market data.
- Never include real personal data, private keys, seed phrases, or production API secrets in the repo.
- Label all fixtures clearly as SYNTHETIC.

## Secrets
- No API keys, private keys, or credentials in code, docs, or commits.
- Use environment variables or a secrets manager.
- Trading API keys must have **no withdrawal permissions**.

## Engineering
- Python 3.10+. Prefer stdlib + minimal vetted dependencies.
- Tests for all new behavior. No live network calls in unit tests (inject clients).
- Security reviews for any component touching external APIs or keys.

## Disclosure
- Mark AI-assisted commits with `AI-Assisted: yes`.
- Human review required for security-sensitive changes.

## Definition of Done
CI green (when configured) + human review of security and risk implications.
