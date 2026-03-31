# Card Capture Summary

- **Purpose**: Defines mandatory card capture and destruction procedures for ATMs connected to Interac® or THE EXCHANGE® networks, covering both requested and accidental capture scenarios.

- **Requested Capture Flow**: Financial institutions must capture any card flagged for capture by the issuing bank; captured cards are destroyed in dual custody and logged per internal policy—no cards are returned to Central 1.

- **Accidental Capture Flow**: ATMs may accidentally capture cards; cardholders can retrieve via satisfactory ID verification during the business day following capture; if unclaimed by end of next business day, cards are destroyed in dual custody with audit logging.

- **Dual Custody Destruction Requirement**: All card destruction (credit, chip, debit/ATM) must follow dual custody procedures—a critical control requiring two authorized personnel involvement with audit trail documentation.

- **Audit Logging Mandate**: Institutions must maintain searchable logs of all destroyed cards per internal policy; these logs are audit-critical and likely subject to regulatory review for compliance with payment network requirements.

- **Network Dependencies**: Capture requests originate from Interac® and THE EXCHANGE® issuer systems; no integration with Central 1 exists for returned cards—institutions manage the full lifecycle independently.

- **Architectural Constraint**: ATM systems must distinguish between requested capture (issuer-initiated via network) and accidental capture (system-triggered), with differentiated workflows and timing rules (business day window for accidental capture claims).