# Summary: 4 Workflow Options for Business Taxes

- **Purpose**: Documents two operational workflows for financial institutions to process CRA (Canada Revenue Agency) remittance vouchers through the Business Taxes system—Single Workflow (front-line staff) and Combined Workflow (front-line + back-office separation).

- **Key Data Structures**: Remittance vouchers contain form numbers (e.g., RC159), tax program identifiers (e.g., Payroll Source Deductions), customer account/ID numbers (format: 123456782RC0001), payment amounts, and designated stamp areas for date-stamping.

- **Critical Business Rules**: GST 34 and 62 forms require photocopies made *after* customer signature and dual date-stamping on both original and copy; payments received outside business hours are treated as next-business-day; all form fields must be verified complete before processing.

- **Integration Point**: Central 1 acts as intermediary—financial institutions submit remittance data electronically via Business Taxes, which Central 1 then forwards to CRA and the Receiver General; form availability must be verified in Business Taxes before processing.

- **Data Flow**: Customer → Front-line (voucher intake, validation, accounting debit/credit) → Business Taxes (electronic submission) → Central 1 → CRA/Receiver General; stub and receipt returned to customer.

- **Fallback Constraint**: Vouchers not available for electronic processing in Business Taxes must be manually processed per Chapter 9, with physical mail/courier delivery to CRA required.

- **Operational Dependency**: Procedures reference Section 8.2 and Chapter 6 for detailed technical steps (form submission, remittance voucher examination), indicating modular documentation requiring cross-reference.