# FYI – April 2023 Release Summary

- **Purpose**: Documentation update log for Payment Solutions Manual clarifications and contact information corrections (April 2023)

- **AFT (Agreement for Transfer) Volume**: Central 1-provided AFT agreements are non-binding convenience documents and do not constitute legal counsel—important for liability and compliance scope definitions

- **FX Drafts Processing**: Two distinct external service endpoints via Convera for draft lifecycle management:
  - `camfi@convera.com` — transaction cancellation requests
  - `draftprocessingna@convera.com` — new draft ordering channel

- **Clearing and Deposits subsystem**: FX Draft operations depend on external email-based integration points with Convera; no API documented, suggesting manual or SMTP-based request handling

- **Support escalation path**: Central 1 Client Support Services (1-888-889-7878 Option 1, support@central1.com) is the primary contact for Payment Solutions issues

- **Architect implications**: Email-based integrations with Convera represent potential single points of failure and lack of real-time validation; consider automation/API feasibility for draft ordering and cancellation workflows in future enhancements