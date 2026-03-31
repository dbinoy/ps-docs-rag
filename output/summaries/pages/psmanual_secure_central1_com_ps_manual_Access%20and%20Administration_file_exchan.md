# Summary: File and Report Exchange Folder Structure

- **Purpose**: Documents the three-level hierarchical folder structure of Central 1's File and Report Exchange system, defining where reports are stored and how users access them based on authorization.

- **Access Control Model**: Users see only folders they are authorized to access; folder visibility is independent of access method (web, API, etc.). Authorization is granular to the folder level, not individual files.

- **Consolidated Report Delivery**: Text-format reports (MERGmmdd.DAT, ONDLmmdd.DAT, DAILmmdd, ONBLmmdd.DAT, OMNMmmdd.DAT) combine multiple reports into single files with report codes embedded at position 20 in headers—enables automated downstream processing and archiving without PDF parsing.

- **Bidirectional File Exchange**: System supports both inbound (Returns folders, RETP for I&J files BC-only, Agrinvest Activity Files) and outbound (report distribution); financial institutions actively upload files alongside receiving reports.

- **Multi-Currency and Product Segregation**: Folder structure partitions by currency (CAD, USD, GBP, EUR) and product domains (AFT, Bill_Pmt, Clearing, ETFR, M2M, IFRS9LL, Trustservices, Securitization)—integration points must respect these boundaries for data routing.

- **Report Code Schema**: Four-character codes (e.g., AIBC, CHGS, BPRE, CCMC) identify report types and enable programmatic routing; codes follow naming conventions that encode currency prefix (C/U/N prefix for CAD/USD/NOC) and report category.

- **Unqualified Report Handling**: "Report Default" folder is fallback destination for reports without explicit folder association—architects should define exception handling for misrouted or unclassified reports.

- **External Dependency**: References Payment Solutions Manual volumes (AFT, Bill Payments, Clearing/Deposits, Electronic Transactions) for detailed report specifications; folder structure is stable but report content definitions live elsewhere.