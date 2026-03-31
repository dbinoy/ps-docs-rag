# Payment Solutions Release 25:16 Summary for Solutions Architects

- **Overview**: July 21, 2025 release consolidating Branch Capture and Corporate Capture documentation into the unified Deposit Processing Part, obsoleting six standalone user guides and revising Form 8996.

- **Documentation Consolidation**: Six form-based user guides (Forms 5914, 5925, 5926, 5927, 5936, 5941) have been deprecated and their content integrated into Chapters 6-13 of Deposit Processing Part, indicating a shift from role-specific guides to consolidated process documentation.

- **Branch Capture Process Architecture**: New chapters (7-13) document discrete workflows: scanner procurement/testing (Ch. 6-7), user management (Ch. 8), deposit operations (Ch. 9), approval/disapproval (Ch. 10), transmission (Ch. 11), assignment/aging (Ch. 12), and reporting (Ch. 13)—suggesting modular backend services supporting these distinct phases.

- **Corporate Capture Integration Point**: Section 15.3-15.4 defines Corporate Capture workflows with business customer enrollment via Form 8996 through ServiceNow; architecture must support multi-tenant customer management with fee-based licensing constraints and prerequisite implementation requirements.

- **Fraud Monitoring Dependency**: Mobile Deposits feed into Central 1's Enterprise Fraud Management System (EFM)—architects must design deposit workflows with hooks for real-time fraud event transmission and assume EFM is a critical external integration dependency.

- **Item Eligibility Rules**: Sections 5.2-5.3 document acceptability criteria for deposits (including non-US foreign cheques), and Chapter 6 notes Canon CR-80 scanner deprecation—architects should abstract item validation logic and maintain hardware compatibility matrices.

- **Operational Data Models**: Implicit data entities include deposits, deposit items, user roles/permissions, scanner configurations, and aged open deposits; transmission and approval workflows suggest state machines with audit trails for compliance.