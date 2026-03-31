# Settlement of Provincial Concentrator Holding Account - Architecture Brief

- **Overview**: Documents the settlement mechanics for Provincial Concentrator holding accounts, including credit posting for Branch Capture deposits and PAD-initiated sweep transactions to provincial accounts at Central 1.

- **Branch Capture Settlement**: Central 1 credits institution accounts for cheques processed via Branch Capture; deposits flagged with code "BC" on AIBC/AIBU (BC) or AIOC/AIOU (Ontario) statements. Deposit adjustments issued when items fail processing (image quality, ineligible currency/type) or amount keying errors occur.

- **PAD Sweep Mechanism**: Provincial Concentrator accounts debited via pre-authorized debit (PAD) based on deposit totals submitted on Province of BC Deposit Slip in ServiceNow; transactions appear on Automated Transfer System Detailed Listing (CCD) report; account must zero-balance at end of each processing cycle.

- **Key Data Structures**: Deposit Slip submission in ServiceNow; CCD report for PAD transaction visibility; statement codes (BC) for source identification; reconciliation requirement is daily (not batch-cycle).

- **Critical Constraint**: PAD failures must NOT be returned through clearing—errors require Paper Payments and Cash Returns Trace Request form submission in ServiceNow (Section 5.2 referenced for error procedures).

- **Integration Dependencies**: ServiceNow (Deposit Slip input, trace request submission); Central 1 account system; Branch Capture processing pipeline; Deposit Processing subsystem (adjustment logic); clearing system (for non-PAD error handling).

- **Architect Consideration**: Daily reconciliation requirement and PAD exception routing (out-of-band via ServiceNow form) suggest need for audit trail, exception management, and settlement status monitoring independent of standard clearing return mechanisms.