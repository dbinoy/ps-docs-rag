# FYI – November 2025 Summary

- **Purpose**: Documentation of November 2025 updates to Payment Solutions Manual spanning Bill Payments and Clearing & Deposits volumes

- **Bill Payments Module – Online Tracing System**: Trace reason enumeration restricted to three values: "Duplicate Payment," "Fraudulent Transaction," or "Other" (constrain validation logic accordingly)

- **Clearing & Deposits Module – FX Drafts**: Updated contact point for Convera integration—draft voids, stop payment requests, and refund inquiries now route to `customercare@contact.convera.com` (verify API endpoints or webhook handlers referencing legacy contact information)

- **External Dependency**: Convera system handles draft lifecycle operations (void, stop payment, refund); email-based communication suggests potential asynchronous notification patterns or manual intervention workflows that may require escalation logic

- **Documentation Refresh**: Screenshot updates across both modules indicate UI/UX changes; ensure any embedded UI documentation or API response examples reflect current state to prevent architect/developer confusion

- **Support Escalation Chain**: Central 1 Client Support (1-888-889-7878 Option 1 or `support@central1.com`) owns technical inquiries; clarify if this is the SLA owner for Convera integration issues or if escalation paths differ by subsystem