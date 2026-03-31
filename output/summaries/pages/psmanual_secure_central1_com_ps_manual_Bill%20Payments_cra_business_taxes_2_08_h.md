# Summary: Processing Business Tax Payments and Filings Electronically

- **Purpose**: Defines procedures for submitting CRA (Canada Revenue Agency) business tax payments and filings electronically through Central 1's Business Taxes system, targeting front-line and back-office staff using single or combined workflow models.

- **Key Process Flow**: Remittance voucher verification → Business Taxes login → branch selection → tax form selection (by name or number, excluding language codes E/F) → form completion with CRA voucher data → preview/validation → submission → receipt generation with confirmation number.

- **Critical Constraint on Reversals**: Corporate and personal CRA Billers do not accept same-day bill payment reversals; only non-same-day traces can be submitted via the Online Tracing System (OLT), creating a dependency on that system for dispute resolution.

- **Filing Date Rules**: Dates can be backdated up to 5 business days (combined workflow only) but cannot be forward-dated; payments received during extended hours must be processed next business day with appropriate date-stamping.

- **Data Fields Required**: Customer account number, business name, business number, filing date, payment amount; optional fields include gross payroll amount and employee count, with a last-day-of-deductions-withheld date selector.

- **Archive & Audit Integration**: CRA transactions persist in PaymentStream Direct for 18 months with searchable archived tasks (transit number, initiator ID, amount, date range); only transactions involving money movement create tasks.

- **Form Validation Dependency**: If electronic form is unavailable in Business Taxes, manual processing via Chapter 9 is required; refer to Bank Truncation Guide (Form 10138) for eligible CRA payees list.