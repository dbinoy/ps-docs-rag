# Settlement of Receiver General Concentrator Holding Account - Summary

- **Overview**: Documents the settlement workflow for cheques processed via Branch Capture and the sweep mechanism for Receiver General Concentrator holding accounts, including reconciliation requirements and error handling procedures.

- **Branch Capture Settlement**: Central 1 credits institutions' Central 1 accounts for Branch Capture cheque values; deposits appear on statements (AIBC/AIBU for BC, AIOC/AIOU for Ontario) with code "BC". Deposit adjustments are issued for processing failures, keying errors, or ineligible items (currency mismatches, non-clearing eligible items).

- **Sweep Mechanism & Data Flow**: Central 1 initiates sweeps that debit Receiver General Concentrator holding accounts based on deposit totals submitted via ServiceNow Receiver General Deposit Request; transactions appear on Automated Transfer System Detailed Listing (CCD) report; holding account balance must zero each cycle.

- **Daily Reconciliation Requirement**: Institutions must actively monitor and reconcile Receiver General Concentrator holding accounts daily; this is a critical control point and dependency on institution-side processes.

- **PAD Error Handling Constraint**: Pre-authorized debit (PAD) errors must NOT be returned through clearing; instead, errors require submission of "Paper Payments and Cash Returns Trace Request" form in ServiceNow (cross-reference to Section 6.2).

- **Downstream Settlement**: Central 1 calculates total value for Receiver General's Concentrator account at Central 1, then initiates wire transfer to Receiver General with deposit summary detail keyed by Routing Authorization Number—represents integration point with external wire transfer and reporting systems.

- **Integration Dependencies**: ServiceNow (Receiver General Deposit Request, Paper Payments and Cash Returns Trace Request), Deposit Processing system, Automated Transfer System (CCD reporting), and external wire transfer rails.