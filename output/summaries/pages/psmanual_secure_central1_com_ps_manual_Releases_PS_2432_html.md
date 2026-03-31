# Payment Solutions 24:32 Release Summary

- **Release scope**: Documentation update to Online Tracing System (OTS) component addressing biller eligibility for trace request processing (September 6, 2024)

- **Key process change**: Maintenance list of financial institutions that reject or do not support trace requests originating from Central 1, indicating this is a managed allowlist/blocklist maintained in OTS configuration

- **Critical data structure**: "Billers that Don't Accept Trace Requests from Central 1" — a reference dataset in Section 1.3 that OTS queries during trace request validation to prevent failed transactions and improve routing logic

- **Integration point**: OTS depends on this biller exclusion list to enforce pre-flight validation; trace requests targeting blocked billers should fail gracefully or route to alternative processing paths

- **Constraint to architect around**: Biller support status is dynamic and requires periodic maintenance updates; systems consuming OTS must handle the case where a previously accepted biller becomes unsupported mid-deployment

- **Data flow implication**: Bill payment submission → OTS eligibility check against biller blocklist → accept/reject decision; architects should assume this check is synchronous and latency-sensitive

- **Support/governance**: Updates published through Payment Solutions manual with support escalation to Central 1 Client Support Services — suggest monitoring release notes for biller list changes that may affect downstream billing integrations