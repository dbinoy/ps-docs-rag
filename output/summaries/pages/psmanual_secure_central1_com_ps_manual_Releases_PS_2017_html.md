# Payment Solutions 20:17 Release Summary

- **Release scope**: Documentation update (May 29, 2020) reflecting operational changes to Provincial Concentrator Account Deposits handling for British Columbia, specifically chargeback and dishonoured item processing workflows.

- **Primary integration change**: Chargebacks for BC are now processed through CIBC's transit system rather than previous internal routing—requires updated procedures in Section 3.3 of the Provincial Concentrator Account Deposits (BC) Part.

- **Exception handling rules**: 
  - Misdirected chargebacks must be returned to CIBC (Section 3.4)
  - Dishonoured items routed to CIBC's transit (Sections 3.4 and 4.3)

- **Operational process affected**: Branch Capture deposit workflow for Provincial Concentrator Account cheques—documentation includes updated endorsement stamp image and routing logic for dishonoured items.

- **Key constraint**: This update is BC-specific; other provincial concentrator accounts may retain different chargeback/exception routing—confirm scope before applying to multi-province implementations.

- **Documentation dependency**: Manual updates span multiple sections (3.3, 3.4, 4.3) across a single part; architects should verify all interdependent sections are current before designing integration solutions.

- **External dependency**: CIBC operates the transit system for chargeback and exception item processing—treat as authoritative downstream system with SLA implications for clearing timelines.