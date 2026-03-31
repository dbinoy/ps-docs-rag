# Summary: AFT Deadlines and Record Entry Limits

- **Purpose**: Defines file delivery deadlines and record entry (backdating/future-dating) limits for Automated Funds Transfer (AFT) transactions processed through Central 1.

- **File Delivery Deadlines vary by service type**: Recommended deadline is 2:00 pm PT two business days before Due Date; optional deadline is one business day before Due Date (3:00-4:00 pm PT depending on service). PaymentStream AFT Automatic Release operates on fixed intervals (seven release windows daily starting 2:00 am PT) with no manual deadline control.

- **Critical constraint on late file delivery**: Files delivered by the optional deadline (one day before Due Date) may prevent Central 1 from resolving validation errors and block AFT Originators from requesting Credit Transaction or file recalls—creates operational risk and degraded error recovery capability.

- **Serviceability Code dependency**: Financial institutions must have CPA Serviceability Code "0" or "1" to accept files via optional (later) delivery deadlines. This field is defined in the Financial Institutions File and constrains delivery window flexibility.

- **Record entry limits (backdating/future-dating) are transaction-type and release-method specific**:
  - PADs: backdatable up to 173 calendar days; future-datable up to 14 days (manual) or 45 days (file upload)
  - Direct Deposits: backdatable up to 30 calendar days; future-datable up to 14 days (manual) or 45 days (file upload)
  - Automatic release types ignore future-dating limits (system extracts three business days prior to Due Date)

- **Time limit calculation basis**: Limits are computed from record creation/modification timestamp in PaymentStream AFT, or from file creation date if uploaded as batch—impacts audit trail and compliance requirements.

- **Integration dependencies**: PaymentStream AFT validation engine, Financial Institutions File (Serviceability Code lookup), and financial institution business hour processing windows create coupling points; automatic release scheduler depends on three-business-day offset calculation.