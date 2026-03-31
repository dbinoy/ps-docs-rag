# Payment Solutions - Payments Forms Summary

- **Purpose**: Comprehensive catalog of 150+ standardized forms and file specification documents for payment processing operations across national, BC-specific, and PaymentStream service lines

- **Key Service Lines & Integration Points**:
  - Automated Funds Transfer (AFT) – includes dormant period requests, service agreements, clearing file specifications (CAD/USD, regional variants), and trace/recall mechanisms
  - Electronic Bill Payment (EBP) – bill payment reversal, batch file specs, biller enrollment, transaction limits
  - Wire transfers – outgoing requests, contingency requests, wire trace/recall/amendment, currency-specific routing instructions (EUR, GBP, JPY, AUD, CHF, MXN, PLN, NZD)
  - Pre-authorized Debits (PAD) – agreements, reimbursement claims, stop requests, undertakings for cash management

- **Critical Data Structures & File Formats**:
  - Multiple file specification documents (clearing files, return files, batch files, EDI/flat file specs) with region-specific variants (BC/Atlantic vs. All Other Regions)
  - ISO 8583 and ISO 20022 integration message specifications with response code mappings
  - Currency and country-specific payment codes (20+ countries) and routing instructions by currency
  - Mobile Deposit and Corporate Capture XML deposit file specifications

- **Access Control & Constraints**:
  - Forms marked with asterisk (*) restricted to Operations Manual Program subscribers only – non-subscribers receive error messages
  - PaymentStream AFT User Request (6257) designated "for financial institutions' internal use only"
  - Region-specific forms (BC only) and role-based user request forms (Capture Analyst, Supervisor, etc.)

- **Compliance & Risk Management Forms**:
  - Statutory declarations (unauthorized transactions, intended payee not paid)
  - Indemnity agreements (lost/stolen/destroyed documents, bond sales)
  - Politically Exposed Foreign Person Statement
  - Foreign Exchange transaction documentation

- **Dependencies on External Systems**:
  - Central 1 Client Centre and SFTP/Direct Connection access for file exchange
  - RBC cash services integration (business deposit investigation checklist)
  - Receiver General/CRA interactions (warrant reimbursements, bank truncation guide)
  - Third-party payment processing (Interac e-Transfer limit groups, biller agreements)