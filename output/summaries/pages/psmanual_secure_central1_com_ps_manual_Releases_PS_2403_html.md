# Summary: PS 24:03 Release (January 4, 2024)

- **Release scope**: Documentation updates to Enterprise Fraud Management (EFM) module clarifying alert management workflows, Auto Risk flag handling, and transaction processing rules.

- **Key distinction**: Alerts and Auto Risk flags are functionally different constructs; alerts are manually created only on `paymentRT` events (not `paymentNRT` events), while Auto Risk flags are system-generated risk indicators.

- **Critical workflow constraint**: Once transactions are classified (alerted transactions marked as Risk/No Risk, or fraudulent Auto Risk transactions marked as Risk), customers regain ability to resubmit transactions—this is a state-dependent operational gate.

- **Data field constraint**: Comment fields across transaction alert management have a 420-character limitation; architects must enforce this in form validation and data models.

- **New capability**: Section 8.8 introduces funds recovery request functionality as a documented process—likely a new integration point or workflow requiring backend support.

- **No-action requirement for legitimate transactions**: Auto Risk-flagged transactions classified as legitimate require no manual intervention, implying a passive monitoring model separate from alert-driven workflows.

- **Support routing**: EFM inquiries route to `efm@central1.com` (distinct from general support), indicating specialized domain ownership for architecture questions.