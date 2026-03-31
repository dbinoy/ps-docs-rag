# FYI – August 2023 Summary for Solutions Architect

- **Purpose**: August 2023 release notes documenting updates to Payment Solutions Manual terminology, processes, and document specifications across AFT and Electronic Bill Payments System modules.

- **Terminology Migration**: "Secure site" references replaced with "Client Centre" across AFT documentation—affects user-facing messaging and portal navigation in customer-facing systems.

- **AFT Service Enrollment**: Step 8 of the enrollment process (Section 5.1) was clarified; review enrollment flow documentation if designing onboarding integrations or API workflows.

- **Routing Rule Change for Credit Unions**: Manitoba, Alberta, and Saskatchewan credit unions now route modification requests (forms 2424 and 9116) directly to Central 1 via ServiceNow ticket or email instead of provincial centrals—impacts internal workflow orchestration and ticket management system configuration.

- **Transaction Code Correction**: OF code corrected to "43" in Transaction and Charge Codes (document 3667)—validate any code mappings or validation rules in transaction processing engines.

- **File Specification Constraints**: 
  - Cheque Return File names limited to 15 characters (excluding extension)
  - DCPA file uses zero-filled Data Element 12 in 'B' Record; QCPA file supports transaction codes 0065 or others—critical for file parsing and format validation logic.
  - Cross-references exist between QREC, DCPA, and QCPA files in detail records.

- **Contact/Escalation**: Central 1 Client Support Services (1-888-889-7878, Option 1; support@central1.com) owns Payment Solutions documentation—establish this as the authoritative source for specification clarifications during design reviews.