# Release 24:16 Summary – BPRP Settlement and Tracing Updates

- **Overview**: Documentation update to Bill Payment Remittance Processing (BPRP) settlement and tracing procedures, effective April 19, 2024

- **Key Process Change – Trace Request Routing**: Trace requests for electronic payments now follow a dual-path model based on enrollment type:
  - Direct BPRP enrollees can initiate traces only for payments originating from Central1
  - Institutions with BPRP clients must route trace/return requests directly to the Direct Clearer using Form 10015 (no internal trace initiation)

- **Critical Constraint**: This introduces a dependency on the Direct Clearer as an external integration point for client-initiated trace requests; architects must account for potential latency and asynchronous handling

- **New/Updated Artifacts**:
  - BPRP training video added to Section 1.3 (knowledge base, not technical integration)
  - Form 10015 now documented as the formal mechanism for Direct Clearer communication
  - BPRP Traces or Returns Contact List published (reference data for routing logic)

- **Data Flow Implication**: Design must distinguish between Central1-originated payments vs. client-sourced payments to determine trace eligibility; this requires payment origin metadata to be captured and queryable

- **Support/Escalation**: Client Support Services (1-888-889-7878 Option 1, support@central1.com) owns questions—relevant for SLA definitions and ticket routing rules