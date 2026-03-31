# Settlement for CRA Business Tax Transactions - Architecture Summary

- **Scope**: Defines settlement mechanics for CRA business tax payments between Central 1 and FIs in BC/Ontario, and between FIs and their customers; FIs outside BC/Ontario settle through provincial centrals.

- **Settlement Timing**: Payments posted to FI's Central 1 account on business day following receipt; settlement effective date is receipt date (not backdated). Weekend/statutory holiday receipts settle on next business day. Daily settlement window closes at 23:59:59 PT; post-cutoff transactions roll to next day.

- **Settlement Code & GL Mapping**: All CRA business tax payments post as code **"TX" (Bill Payment Tax Settlement)** to FI's Central 1 account; architect must ensure GL reconciliation logic recognizes this distinct transaction code.

- **Fund Guarantee Requirement**: CRA business tax transactions are guaranteed funds—FI must debit customer account and transfer to internal GL account **before** submitting to CRA (not after settlement confirmation). This is a critical pre-condition constraint for payment submission.

- **Payment Date Determination**: CRA recognizes **processing date in Business Taxes system** as payment date for electronic remittance vouchers, but **date stamp** for paper vouchers—creates dual-track date logic for compliance and customer communication.

- **Cheque Dishonour Workflow**: If cheque payment is dishonoured by drawee bank, FI must attempt recovery; if unsuccessful, request reimbursement from federal government (dependency on separate Dishonour/Return of Cheques procedures).

- **Integration Dependencies**: Process mirrors Electronic Bill Payments settlement workflow; requires coordination with Business Taxes processing system, CRA remittance voucher generation, and dishonour/return procedures.