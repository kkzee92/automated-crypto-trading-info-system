# Operational Security Checklist

## Before any API key is created
- [ ] Dedicated exchange sub-account created
- [ ] Only the capital intended for automation is funded
- [ ] Withdrawal permissions will be **disabled**
- [ ] IP allow-list prepared (static IP of the host)

## Key management
- [ ] Keys stored in secrets manager or encrypted environment
- [ ] Separate keys for each environment (dev / paper / live)
- [ ] Rotation schedule defined (60-90 days)
- [ ] No keys in git history or logs

## Runtime
- [ ] Process runs with least OS privileges
- [ ] Container or VM isolation in place
- [ ] Audit logging of all external API calls and generated signals
- [ ] Daily loss / anomaly alerts configured
- [ ] Manual kill-switch documented and tested

## Review gates
- [ ] Strategy parameter changes reviewed for risk impact
- [ ] Dependency updates scanned
- [ ] Human sign-off required before any live capital is connected
