# Release 21:27 Summary — AFT via FTP Forms Update

- **Release scope**: Documentation update for AFT (Automated Funds Transfer) via FTP service targeting B.C. financial institutions only; removed CAFT-related information from operational forms

- **Affected forms and document IDs**:
  - Document 1378: "Application for AFT Service via FTP (BC Only)" — revised form with legacy naming ("Application for AFT Service")
  - Document 1641: "File Limit Change Request AFT Service via FTP (BC Only)" — revised form with legacy naming ("Maximum Dollar Limit Change Request — AFT Service")

- **Key constraint**: AFT via FTP service is geographically restricted to British Columbia; forms explicitly designate BC-only scope, indicating regional regulatory or operational requirements

- **Data field impact**: CAFT-related fields/information removed from forms; architects should verify downstream systems (provisioning, compliance, reporting) don't depend on CAFT metadata previously captured through these forms

- **Integration consideration**: Forms are entry points for service onboarding and limit modification requests; ensure form submission workflows and document routing remain functional post-revision

- **Support escalation**: Client Support Services (1-888-889-7878, Option 1; support@central1.com) handles client inquiries regarding revised forms and AFT service configuration

- **Architect action item**: Review form schema changes in Document Library to identify any deprecated fields and update validation logic or downstream processing accordingly