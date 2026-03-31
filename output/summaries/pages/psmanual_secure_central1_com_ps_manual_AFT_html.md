# Summary: AFT (Automated Funds Transfer) Documentation Portal

- **Purpose**: Comprehensive reference documentation for originating, processing, settling, and managing Automated Funds Transfer transactions across Canadian credit unions, covering PADs (Pre-authorized Debits), Direct Deposits, recalls, returns, and error corrections.

- **Core Process Flows**: Three origination methods—PaymentStream AFT (web-based), File Transmission (FTP-based for BC), and manual processing—feed into Central 1's clearing and settlement infrastructure with defined file delivery deadlines and record entry limits per transaction type.

- **Key Data Structures**: AFT transactions include originator/payor/payee records, transaction codes (CPA-defined), serviceability codes for posting status, and offsetting entry options; PaymentStream requires 2-step security and permission-based user management for transaction release.

- **Critical Constraints**: Recall deadlines and recourse periods vary by transaction type (business vs. consumer PADs); unpostable transactions require re-routing; rejected files trigger exception handling workflows; dormant periods and service cancellation have defined procedures.

- **Integration Dependencies**: Central 1's clearing settlement system, File and Report Exchange (BC), ServiceNow for recalls/trace requests, FINTRAC reporting for suspicious transactions/terrorist financing, and CPA rules governance; bi-directional data flow includes incoming returns, NOC (Notice of Change) transactions, and batch return services.

- **Reporting and Compliance**: 25+ standardized reports (ICPS settlement, CCD/UCS summaries, PADB business PAD listings) track transaction volumes, billing, and exception items; PCMLTFA compliance and restricted entity screening required at enrollment.

- **Architect Considerations**: Dual approval workflows for high-risk transactions, configurable originator limits, data purge schedules for PaymentStream, and contingency procedures (email fallback, manual submission) indicate need for robust reconciliation, audit logging, and failover mechanisms in any enhancement.