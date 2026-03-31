# Release 23:28 Summary – EFM Decision Mode Updates

- **Overview**: Documentation updates to Enterprise Fraud Management (EFM) decision-making workflows and activity filtering, effective November 10, 2023.

- **Key Process Changes**: 
  - Activity Filter "Under investigation" status now explicitly excludes Central 1 and credit union entities; filter requests unaffected by this selection
  - Legitimate transaction identification now requires potential sender communication for Interac e-Transfer Auto Risk flagged items
  - Manual alert creation workflows expanded with situational guidance; revision workflows clarified with updated visual documentation

- **Auto Risk Transaction Handling**: Separate alerting logic for Auto Risk transactions vs. manual alerts; system distinguishes between auto-flagged and manually-created alerts with specific identification procedures per section 8.4-8.5.

- **Critical Integration Point**: OAS-to-EFM connection is fully automated for investigation result reporting; manual email reporting to Central 1 no longer required or supported (section 8.8 deleted).

- **Scope Constraint**: Changes apply only to Enterprise Fraud Management Part; Electronic Transactions Volume documentation area also updated but treated as separate concern.

- **Deprecated**: Document "Reporting Risk or No Risk on EFM Alerts" (ID: 9696) marked obsolete—architects should verify no dependent processes reference this artifact.

- **Support/Governance**: Questions escalate to Client Support Services (1-888-889-7878 Option 1 or support@central1.com); indicates vendor-managed system with controlled change communication.