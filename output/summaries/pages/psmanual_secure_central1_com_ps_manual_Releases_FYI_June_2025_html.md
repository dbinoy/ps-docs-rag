# FYI – June 2025 Documentation Updates Summary

- **Purpose**: Release notes documenting June 2025 updates to Payment Solutions Manual across three operational volumes (Bill Payments, Central 1 Banking Services, Clearing and Deposits)

- **Bill Payments Integration Change**: Removed static biller trace-request lookup table; now requires dynamic queries against EBP (Electronic Bill Payment) Billers list to determine trace request acceptance—impacts trace request routing logic and eliminates batch reference data maintenance

- **Transaction Coding Reference**: Sections 6.4 and 7.2 (CAS Online) now mandate cross-reference to Form 3667 for transaction codes, charge codes, and reference number semantics—architects must ensure UI/reporting systems can link to or embed this form data

- **FX Drafts Vendor Consolidation**: Convera contact points consolidated to four email addresses (camfi@, customercare@, draftprocessing@, draftvoid@convera.com)—indicates potential API endpoint or webhook URL changes for draft processing workflows; verify Convera integration configurations

- **Support Escalation Path**: Central 1 Client Support (1-888-889-7878 Option 1, support@central1.com) serves as primary escalation point for questions—relevant for SLA definitions and incident routing

- **Data Structure Dependency**: Form 3667 (Transaction and Charge Codes) appears to be a critical reference schema; architects should assess whether this should be ingested into operational databases or remain external reference documentation