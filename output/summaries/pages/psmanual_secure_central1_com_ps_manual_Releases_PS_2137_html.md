# Payment Solutions 21:37 Release Summary

- **Release scope**: October 15, 2021 update introducing two new fraud-related response codes to ISO 8583 and ISO 20022 payment message standards for EFM (Enterprise Fraud Management) integration.

- **New response codes**:
  - **995**: EFM Rejection — indicates transaction rejected by Central 1's Enterprise Fraud Management system
  - **996**: EFM Transaction on Hold — indicates transaction flagged as suspicious and queued for fraud analyst investigation
  - Both codes enable asynchronous notification flow to financial institutions of fraud detection outcomes

- **Integration points**: Updates affect both ISO 8583 (legacy, field-based) and ISO 20022 (modern, XML/structured) message formats, requiring dual-format support in payment processing pipelines.

- **System dependency**: Tight coupling with Central 1's Enterprise Fraud Management (EFM) system — response codes are generated downstream of fraud detection rules; architects must design for potential latency in analyst-driven holds (code 996).

- **Documentation artifacts**: Response code specifications documented in separate revision-controlled documents (IDs 9346 and 9347); architects should reference these for exact field mappings and usage rules.

- **Operational consideration**: Code 996 introduces a human-in-the-loop workflow (fraud analyst investigation); system design must account for transaction state management and potential async callbacks.