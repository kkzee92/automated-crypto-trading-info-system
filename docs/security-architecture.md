# Cyber and Data Security Architecture

## Threat Model for Automated Crypto Information Systems

| Threat | Impact | Mitigation |
|--------|--------|------------|
| API key theft | Unauthorized trading or fund loss | Least privilege (no withdrawals), IP allow-list, rotation, secrets manager, dedicated sub-account |
| Data leakage of strategy logic | Competitive disadvantage | Code access controls, private repos for sensitive variants |
| Compromised host | Full control of bot | Isolated environments, containerization, minimal privileges, monitoring |
| Man-in-the-middle | Altered signals or data | TLS 1.3+, certificate pinning where feasible |
| Insider / agent misuse | Bad signals or config changes | Audit logs, human review gates, least-privilege agents |
| Supply chain | Malicious dependencies | Pin versions, licence & vulnerability scanning |

## Core Security Principles

1. **Least Privilege**
   - API keys: read + trade only (or read-only for pure info systems). **Never** enable withdrawals.
   - Process isolation: dedicated containers or VMs.

2. **Secrets Management**
   - Environment variables for development.
   - Production: HashiCorp Vault, AWS Secrets Manager, or equivalent.
   - Never commit `.env` files.

3. **Network & Access**
   - IP allow-listing on exchange API keys.
   - Zero-trust: authenticate and authorize every internal call.
   - Separate networks for data ingestion vs. signal generation.

4. **Audit & Monitoring**
   - Immutable logs of all signals, data sources, and configuration changes.
   - Anomaly detection on order sizes, frequency, or unexpected API calls.
   - Alerting on key usage from unknown IPs.

5. **Data Security**
   - Encryption in transit (TLS) and at rest (AES-256).
   - Minimal data retention.
   - No personal data stored.

6. **Key & Credential Hygiene**
   - Rotate API keys every 60-90 days.
   - Separate keys per service/environment.
   - Hardware security keys or authenticator apps for human access.

## Recommended Architecture Layers

```
[External Data Sources] --TLS--> [Ingestion Service (isolated)]
                                      |
                                      v
                               [Feature Store / Cache]
                                      |
                                      v
                               [Strategy Engine (least privilege)]
                                      |
                                      v
                               [Signal Output / Alerting]
                                      |
                                      v
                               [Human Review / Paper Portfolio]

All components: Audit Log --> Centralized SIEM / Monitoring
Secrets: External Vault (never in process memory longer than needed)
```

## Implementation Checklist

- [ ] API keys stored only in secrets manager
- [ ] Withdrawal permissions disabled on all keys
- [ ] IP allow-list configured
- [ ] Dedicated sub-account with limited capital for any live testing
- [ ] Audit logging enabled
- [ ] Dependency scanning in CI
- [ ] Regular security review of strategy changes

**Note:** This system is designed primarily as an *information* system. Any transition to live automated execution requires additional controls (pre-trade risk checks, kill switches, human override, professional custody review).
