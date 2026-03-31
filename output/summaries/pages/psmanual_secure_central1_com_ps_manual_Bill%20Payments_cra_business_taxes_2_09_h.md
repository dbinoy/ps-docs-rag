# Summary: Processing Remittance Vouchers Manually

- **Purpose**: Defines manual processing procedures for CRA remittance vouchers that lack electronic availability, requiring same-day completion by front-line staff upon receipt from customers.

- **Core Process Flow**: Account debit/GL credit → physical stamping → stub separation → bundling (max 25 vouchers) → tape listing generation → photocopying → secure storage (12 months) → mail/courier to CRA.

- **Key Data Elements**: Form number, tax program identifier, remittance voucher amount, member account identifier, GL account code (tax program-specific), tape listing sequence, grand total draft amount, and dated stamps (legibility requirement is critical).

- **Pre-Processing Validation Gate**: Form must pass three checks before manual processing begins: (1) form number matches corresponding tax program, (2) all form fields complete, (3) voucher confirmed unavailable in Business Taxes system—this is a critical integration dependency.

- **Physical-to-Financial Reconciliation**: Tape listing serves as the reconciliation control document; voucher ordering must match tape listing sequence exactly to ensure accurate GL posting and CRA matching at destination.

- **Constraints & Compliance**: Max 25 vouchers per bundle; photocopies must be retained 12 months in secure storage (audit trail requirement); date stamps on originals and copies must be legible; draft must be payable to "Receiver General" (specific payee requirement).

- **External Integration Point**: Process terminates with physical mail/courier delivery to fixed CRA address (875 Heron Road, Ottawa)—no electronic submission pathway; this creates a manual reconciliation dependency between institution records and CRA receipting.

- **Architectural Implication**: Manual voucher processing creates a parallel data path outside Business Taxes system; any enhancement should consider automated form validation, GL account mapping, and tape listing generation to reduce human error in the pre-mailing steps.