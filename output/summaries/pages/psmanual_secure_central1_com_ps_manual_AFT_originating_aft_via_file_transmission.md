# Summary: AFT File Upload Process & Validation

- **Scope**: Defines the procedural and technical requirements for Originators to upload AFT files to Central 1's File and Report Exchange, including business rules, submission deadlines, and validation workflows.

- **File Format & Standards**: AFT files must comply with CPA Standard 005 specifications (see Section 2.4); file creation date cannot exceed 7 days before processing; files must be submitted in consecutive sequential order starting at 0001.

- **Submission Constraints**: Hard deadline of 2 PM PT, two business days before due date; exceeding this shifts processing to following business day. File value must not exceed Originator's maximum dollar amount limit.

- **Dating Rules (Critical Business Logic)**:
  - Credit records: post-date limit 45 days (CPA allows 14 days), backdate limit 30 calendar days
  - Debit records: post-date limit 45 days from transaction forwarding date (CPA allows 2 days), backdate limit 173 calendar days
  - Central 1 warehouses transactions up to 45 days regardless of CPA limits

- **Validation & Response Flow**: Three auto-generated response files (.LST, .ERR, .BAK) created within minutes in AFT subdirectory; Originator responsible for checking .LST confirmation file. Initial upload validation differs from mainframe validation—rejects at mainframe stage trigger Central 1 notification; individual transaction rejects (not whole file rejects) reported via Recalled/Rejected PAP Items Report (ICRR/UCRR).

- **Integration Dependencies**: Requires prior setup of AFT subdirectory by Central 1; depends on separate File Exchange and Report Distribution system for access provisioning and FTP connectivity; links to downstream Processing Direct Clearer for debit transaction forwarding.

- **Pre-requisites**: Completed agreements/application forms and sporadic debit authorization required per instance before file submission.