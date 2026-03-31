# wwparcel.html Summary for Solutions Architect

- **Purpose**: Comprehensive documentation portal for Payment Solutions manual covering user management, security, file exchange, and Central 1 clearing file specifications—this page displays the table of contents across multiple domains rather than specific technical content.

- **Key Domains Covered**:
  - CPS Admin Application (Security Officer management, Client Centre user lifecycle)
  - User Management (account provisioning, 2-Step Security token assignment, application access permissions)
  - File Exchange and Report Distribution (SFTP and Client Centre-based file transport)
  - Central 1 File Specifications (clearing files, AFT, bill payments, cheque returns, NOC, deposits)

- **Critical Integration Points**:
  - Central 1 clearing system (AFT files, bill payment batches, cheque returns, deposit files)
  - Client Centre portal (web-based file/report exchange, user authentication)
  - SFTP direct connections for enterprise file exchange
  - PaymentStream suite (multiple modules: Direct, AFT, bill payments, CRA, e-statements)
  - Multiple third-party applications requiring permission management (Forge OpenText, Interac e-Transfer OAS, Lock-N-Block, MTS, Treasury Connect)

- **User Access Control Model**: Multi-tiered hierarchy—Security Officers → User Management admins → Client Centre users, with role-based application access permissions and 2-Step Security token enforcement (hard and soft tokens).

- **File Specifications Dependency**: Outgoing files from Central 1 include AFT clearing, PREC/OREC (regional), bill payment remittance data (EDI/flat file), HREC, deposit files, and wires data extract—all with specific naming conventions and null file handling requirements.

- **Security Constraints**: Password policies, account inactivity reviews, 2-Step Security token lifecycle management, and internal control policies must be established before user provisioning.

- **Architectural Consideration**: No specific data models or API contracts documented on this TOC page—detailed specifications exist in child pages (referenced sections 8.1-8.44 for application-specific permission rules, and sections 3.1-3.6 for file technical specs).