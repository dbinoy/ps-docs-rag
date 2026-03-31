# Release 25:06 Summary for Solutions Architect

- **Purpose**: Release notes documenting updates to Enterprise Fraud Management (EFM) transaction alert handling and mobile deposit processing as of March 17, 2025.

- **Mobile Deposit Ingestion**: EFM now captures mobile deposits via Data Ingestion mode (effective March 16, 2025), but does **not** auto-trigger alerts for suspicious activity—manual alert creation and risk classification required by end users.

- **Auto Risk Transaction Workflow Change**: Legitimate transactions previously marked "No Action" must now be explicitly classified as "No-risk" in sections 8.1 and 8.3; this eliminates implicit handling and requires active user designation.

- **Risk Classification States**: System distinguishes between transaction states: "Auto Risk" (system-flagged), "No-risk" (user-confirmed legitimate), and "Risk" (user-confirmed suspicious)—all require explicit user action.

- **Data Flow Constraint**: Mobile deposits flow through Data Ingestion mode without rule-based alerting, creating a detection gap that depends on user vigilance and manual alert protocols; architects must account for this async, human-in-the-loop validation layer.

- **Documentation Scope**: Changes affect alert management UI/workflow documentation (sections 8.1, 8.3, 8.9), suggesting potential API or database schema implications for transaction state transitions.

- **Support Contact**: Client Support Services (1-888-889-7878 Option 1 or support@central1.com) for implementation questions.