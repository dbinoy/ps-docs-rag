# Appendix A-17: ORS Troubleshooting Guide Summary

- **Purpose**: Diagnostic reference for Online Return System (ORS) issues affecting cheque clearing, returns, and notices of change workflows within the Central 1 payment infrastructure.

- **User Permission Model**: ORS functionality is role-based (ORS User Type); missing menu elements (Summary, Preference, Upload, Reports links) indicate incorrect security configuration managed by User Management Security Officer—architectural implication: RBAC controls feature visibility at UI level.

- **Cheque Image Availability Constraints**:
  - Status-dependent rendering: yellow status with OOP/OOR (out-of-pocket/out-of-region) indicates cheques not yet arrived at Central 1
  - "Image Unavailable" subdocuments are generated when cheques fail to arrive from OOP/OOR or mis-sort; these cannot be processed through ORS and require manual escalation to Tracing Department
  - Unclear images require Clearing Department intervention (external fax-based resolution)

- **Temporal Business Rules**: E-link availability for cheque returns expires after 6:00 pm PT; AFT returns operate within three processing windows (10:00 am, 3:30 pm, 11:00 pm PT)—architectural requirement: system must enforce time-based link availability and process window gating.

- **Return Status State Machine**: RI column (AFT Returns) and N column (AFT Notice of Change) track completion status (C = Complete); once Complete, corresponding action links (E, N) become unavailable because items have been transmitted to originating FI—architectural implication: link/action rendering must respect downstream system state.

- **Integration Dependencies**: Central 1 Client Support Services, Clearing Department, and Tracing Department are external escalation points; system design must accommodate manual intervention workflows for image failures and routing exceptions.