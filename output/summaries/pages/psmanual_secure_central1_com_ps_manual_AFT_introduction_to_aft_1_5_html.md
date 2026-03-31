# AFT Service Enrollment Process Summary

- **Purpose**: Documents the 11-step enrollment workflow for financial institutions and business member Originators to establish AFT (Automated Funds Transfer) service capabilities, with typical provisioning time of two weeks from document receipt.

- **Service Delivery Models**: Two primary transaction origination pathways—(1) PaymentStream AFT platform with manual/automatic release options, and (2) File Transmission via File and Report Exchange (BC and Atlantic regions only), creating distinct integration requirements and validation workflows.

- **Transaction Type Classification & Constraints**: Four PAD variants (Personal, Business, Cash Management, Funds Transfer) plus Direct Deposits; business members explicitly prohibited from issuing Funds Transfer PADs; PAD type selection drives required agreement forms and downstream CPA compliance validation.

- **Role-Based Input Authority**: For business member Originators, enrollment requires explicit decision on transaction input party (financial institution vs. business member), which cascades into lead time requirements, reporting distribution, rejection handling, and account correction workflows—no standard default model.

- **Agreement & Form Dependencies**: Multi-party signature requirements (institution-to-member agreements, Payor PAD Agreements, Direct Deposit Applications) create blocking dependencies; forms vary by transaction type (Forms 1904, 2007, 2043, 1696, 2000, 5966) with optional vs. mandatory status—affects enrollment validation logic.

- **User Access & Testing Integration**: User Management system creates temporary credentials for PaymentStream AFT access; test file validation occurs on-platform before production release; separate FTP User Request process required for File and Report Exchange access—distinct identity/permission management contexts.

- **Reporting & Settlement Output**: Business member Originators download settlement reports from PaymentStream AFT; financial institution Originators use File and Report Exchange—bi-modal reporting architecture requires conditional report distribution rules based on Originator classification.

- **CPA Regulatory Checkpoint**: Business member PAD Originators require explicit Rule H1 notification (Pre-authorized Debits compliance)—suggests downstream audit/compliance logging requirements for enrollment audit trails.