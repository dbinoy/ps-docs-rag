# Summary: Preparing Outgoing Wires (Section 15)

- **Purpose**: Defines regulatory compliance procedures and data collection requirements for outgoing wire processing in the Wires application, using Form 1171 as the primary data capture instrument.

- **Regulatory Thresholds & Identification Requirements**:
  - Identity verification mandatory for domestic/international wires ≥$1,000 CAD equivalent or foreign exchange wires ≥$3,000 CAD
  - PEP/HIO determination required for wires ≥$100,000 CAD within 14 days of transmission
  - FINTRAC reporting triggered for aggregated transfers ≥$10,000 CAD within 24 hours
  - Suspicious transaction reporting exempt from identification requirements to avoid "tipping off" sender

- **Form 1171 Data Structure** (multi-section capture):
  - Wire metadata: amount (CAD), currency, priority flag, future-date flag, timestamp
  - Sender details: account/customer number, full address, occupation/DOB for non-account holders
  - Beneficiary details: account number or IBAN (mandatory for IBAN-regulated countries per Section 14.3)
  - Intermediary institution routing: SWIFT ID required; for USD-to-US transfers, sender-provided intermediary must be specified; for non-domestic currency wires, selection from system-suggested intermediary list
  - FX transaction details: purchase currency, medium of exchange, exchange rate at time of creation
  - Wire funding source and consent acknowledgments (disclosure, privacy, loss liability, accuracy, finality, no-refund guarantees)

- **Critical Integration Constraints**:
  - Wire recalls/amendments/traces are best-efforts only; receiving bank voluntary cooperation required post-release
  - Intermediary fees deducted by third-party institutions outside Central 1 control
  - Special characters cannot be entered; form data must be sanitized before Wires application import
  - Exchange rates are live/transactional—recorded at creation time, not standardized lookup codes

- **Compliance & Risk Dependencies**:
  - PCMLTFA regulations govern identification procedures; face-to-face vs. non-face-to-face transaction rules differ (per FINTRAC)
  - Non-account holder wires flagged as high-risk; Central 1 discourages this transaction type
  - Form 1171 data feeds FINTRAC EFT reporting pipeline; financial institution responsible for aggregation analysis and reporting decision logic

- **System-Level Considerations for Architects**:
  - Form 1171 is both