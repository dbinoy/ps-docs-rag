# Summary: Contingency Procedures for Incoming and Outgoing Wires

- **Purpose**: Defines fallback procedures for wire processing when a financial institution loses access to the Wires application; the designated contingency processor acts as intermediary to send/receive wires on behalf of the institution during localized outages only. Note: automatic failover to backup servers handles Wires service failures—contingency procedures are not applicable for infrastructure failures.

- **Contingency Processor Model**: Four distinct processor chains by region (Central 1 for BC/Ontario, CUCM for Manitoba credit unions, Caisse Groupe for Manitoba caisses populaires, Atlantic Central for Atlantic credit unions). Each processor requires **two authorized signing officers** to authorize outgoing wire requests; processors forward incoming wires to receiving institutions and outgoing wires to intermediaries.

- **Form 1799 Data Structure**: Contingency Outgoing Wire Request form captures four main sections across 4 pages: (1) Wire Amount/Currency, Sender Info, PEP/HIO declaration; (2) Beneficiary Info, Intermediary Financial Institution Info (critical for CAD-to-USD wires); (3) FINTRAC EFT Report metadata (phone, DOB, occupation, ID type/number for individuals; third-party involvement detection); (4) Dual signing authorization. Required fields flagged with asterisk (*).

- **Regulatory/Compliance Integration Points**: 
  - FINTRAC reporting thresholds: wires ≥$10,000 CAD equivalent (international) or multiple wires totaling ≥$10,000 CAD within 24 hours require EFT Report; suspicious transactions trigger Suspicious Transaction Report
  - PEP/HIO determination required for wires >$100,000 CAD equivalent within 14 days
  - IBAN requirements for IBAN-regulated countries; intermediary data mandatory for USD wires (sourced from sender, not Central 1)

- **Critical Data Dependencies**: Exchange rate (if applicable), wire currency type (CAD/USD/EUR/other), receiving commission amounts, pass-through charges, and sender source-of-funds information must be captured. Account documentation can satisfy identity verification for account holders ≥$1,000 CAD wires. Third-party involvement must be detected and documented with relationship context.

- **Process Constraints & Handoff Requirements**: Fax transmission to processor with mandatory confirmation receipt within 2 hours; financial institution owns responsibility for delivery verification. Form retention period R5 code = 5 years. Contingency processing subject to all rules in Chapters 14–15 (Outgoing Wire Considerations/