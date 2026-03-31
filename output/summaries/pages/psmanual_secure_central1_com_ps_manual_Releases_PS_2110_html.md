# PS 21:10 Release Summary – March 23, 2021

- **Overview**: Release added XML file specifications for qualified debit clearing items (CAD and USD cheques) to Central 1's File Specifications documentation library.

- **New File Specifications**: Two specification documents introduced:
  - XDREC (Document #9319) for CAD cheque clearing
  - XQREC (Document #9320) for USD cheque clearing
  - Both define XML schema and structure for qualified debit clearing workflows

- **Documentation Integration**: Specifications integrated into Access and Administration Volume under Section 5.3 (Qualified Debit Clearing Items) and referenced in Section 1.4 (File Specifications Document Library) on the secure Central 1 portal.

- **Data Flow Implication**: XML-based clearing items represent a structured data exchange mechanism for cross-currency debit processing (CAD/USD), suggesting potential downstream reconciliation, settlement, or GL integration points.

- **Architectural Dependency**: Systems interfacing with Central 1's qualified debit clearing must reference and comply with these XML specifications; updates indicate Central 1 standardized on XML for this clearing mechanism (migration from prior format likely).

- **Support & Access**: Specifications available exclusively on secure.central1.com; client implementations require secure portal access and should reference support contact (1-888-889-7878, Option 1) for clarification on schema compliance during integration design.