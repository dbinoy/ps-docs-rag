# Payment Solutions Release Summary: 24:19 (May 3, 2024)

- **Scope**: Documentation update to Digital & Payment Services Class A Fee Schedule (Form 2725) removing bill payment reversal capability for CRA Business Taxes remittances, effective May 5, 2024.

- **Affected Document**: Form 2725, Section 2.5 (Electronic Bill Payment Processing and Tracing Fees)—revised to reflect removal of same-day reversal option for CRA biller transactions.

- **Geographic/Entity Constraint**: Form 2725 applies exclusively to BC and Ontario Class A credit unions; architects must implement audience-based access controls or conditional logic for this fee schedule.

- **Business Rule Change**: Same-day reversals for CRA Business Taxes bill payments are no longer supported as of May 5, 2024; payment processing workflows must enforce this restriction and prevent reversal requests for these transaction types.

- **Integration Dependency**: Related change documented in separate Client Centre news item ("Changes to Same Day Bill Payment Reversals"); architects should treat both announcements as coupled, with potential downstream impacts on bill payment reversal APIs or transaction state machines.

- **Support/Escalation**: Client Support Services (1-888-889-7878 Option 1 or support@central1.com) is the owner for implementation questions; architects should define clear escalation paths for CRA-specific payment handling inquiries.