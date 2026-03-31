# FYI – June 2023 Summary

- **Purpose**: June 2023 release notes documenting clarifications and additions to the Payment Solutions Manual across three product lines (Bill Payments, Currency Volume, Document Library).

- **Bill Payments reconciliation clarification**: The "Closed – Settled" report in Online Tracing Part (OLT) serves as the reconciliation mechanism between transaction records and Central 1 Banking System (CBS) Online postings—critical for settlement verification workflows.

- **FX integration point**: Exchange Bank of Canada (EBC) is the settlement inquiry contact for Currency Volume services; unified contact routing (payments@ebcfx.com / 1-877-786-3084) for settlement, draft, and cheque clearing inquiries indicates potential service consolidation or shared backend processing.

- **Interac e-Transfer schema update**: Introduction of Limit Group 18 (Document Library status code 9369) adds new transfer constraint tier—functionally similar to Group 2 but with enhanced no-delay transfer capability at $250 maximum per transaction; requires configuration updates in systems managing transfer limits.

- **Data structure impact**: Limit Group logic now spans at least 18 discrete configurations; architects should verify existing limit group enumeration/lookup tables support this expansion without collision or performance degradation.

- **Support escalation path**: Client Support Services (1-888-889-7878 Option 1 / support@central1.com) is the single point of contact for implementation questions—relevant for support SLAs in enhancement design.