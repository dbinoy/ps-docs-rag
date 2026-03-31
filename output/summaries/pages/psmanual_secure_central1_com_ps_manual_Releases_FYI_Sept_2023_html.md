# FYI – September 2023 Release Summary

- **Purpose**: Release notes documenting September 2023 updates to Payment Solutions Manual across five operational volumes (AFT, Central 1 Banking Services, Electronic Transactions, and Document Library)

- **Terminology Migration**: Systematic replacement of "secure site" references with "Client Centre" across all documentation—indicates UI/portal rebranding that may affect client-facing integration documentation and API endpoint references

- **AFT Module Updates**: Five AFT subsystems updated (origination, exception handling, returns/NOC, settlement, reporting), suggesting interdependent transaction processing workflows requiring coordinated changes

- **ATM Transaction Processing Change**: Section 7.3 reflects modified CUPS response deadlines for ATM adjustments/trace requests—indicates timing constraints and SLA dependencies on external switch (CUPS) integration that architects must account for in retry logic and reconciliation processes

- **SFTP Connectivity Requirement**: Restored "IP(s) must be static" constraint in FTP User Request form—critical architectural requirement for secure file transfer integration; impacts network configuration and firewall rules for clients

- **File Exchange System**: Form 3430 updates to Client Centre access procedures with new troubleshooting section—suggests the File and Report Exchange Online system is a key integration point for business members; added diagnostic capabilities may indicate known operational issues

- **CEBA and CBS System Scope**: Central 1 Banking Services volume covers loan repayment settlement, reconciliation, current accounts, and online banking—indicates multiple financial product lines with distinct data flows and settlement requirements