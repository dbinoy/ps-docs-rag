# Summary: Reconstructing Lost CRA Remittance Voucher Bundles

- **Purpose**: Documents the process for resubmitting CRA (Canada Revenue Agency) remittance voucher bundles that were lost in mail transit when the original draft remains uncashed after one month or CRA reports missing funds.

- **Key Process Flow**: Stop-payment on original draft → photocopy remittance vouchers → create tape listing (maintains voucher sequence) → issue replacement draft to Receiver General → send letter on institutional letterhead → mail reconstructed bundle to CRA (875 Heron Road, Ottawa, Ontario K1A 1B1).

- **Critical Data Structure**: Tape listing serves as the control document; must include all remittance vouchers in identical sequence as photocopies to ensure CRA reconciliation and prevent duplicate processing.

- **Date Preservation Rule**: CRA uses the date on remittance voucher photocopies as official payment date, which prevents customer penalty/interest accrual and triggers reversal of previously assessed penalties/interest—architect must ensure date fields on vouchers are immutable through reconstruction workflow.

- **Dependency on Manual Processing**: This process is a fallback for remittance vouchers that "cannot be processed in Business Taxes" (Chapter 9 reference); indicates Business Taxes module has validation or processing limitations requiring postal submission as alternative channel.

- **Communication Requirement**: Institutional letter must include contact name/phone and explicitly state "original bundle lost in mail"—suggests CRA has manual verification workflow requiring human-readable context rather than system-to-system integration.

- **No Automated Recovery Integration**: Process requires manual stop-payment execution, photocopying, and postal delivery; no indication of API/EDI reconciliation with CRA or automated status tracking—architect should note this represents a gap for real-time bundle tracking and loss prevention.