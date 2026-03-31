# Settlement of ICBC Agents' Accounts - Summary

- **Purpose**: Describes the settlement mechanism for cheques processed through Branch Capture and pre-authorized debits (PAD) for ICBC agent deposit accounts at Central 1.

- **Branch Capture Settlement Flow**: Central 1 credits the financial institution's Central 1 account for cheques processed via Branch Capture; deposits flagged with code "BC" on statements (AIBC/AIBU for BC; AIOC/AIOU for Ontario).

- **Deposit Adjustment Triggers**: Central 1 issues adjustments for unprocessable items (image quality, piggybacks), keying errors with force-balanced deposits, or ineligible items (currency mismatch, non-clearing eligible).

- **ICBC Agent Account Sweep Mechanism**: Central 1 initiates a sweep that debits the agent account via PAD the following day based on deposit totals reported on the ICBC Deposit Slip in ServiceNow; transactions appear on the Automated Transfer System Detailed Listing (CCD) report with expected zero balance per cycle.

- **Reconciliation Requirement**: Financial institutions must monitor and reconcile ICBC agent accounts daily; PAD failures must not be returned through clearing and require a Paper Payments and Cash Returns Trace Request form submission in ServiceNow (referenced in Section 6.2).

- **Key Integration Points**: ServiceNow (deposit slip reporting), Branch Capture system, Automated Transfer System (CCD reporting), and PAD processing infrastructure.

- **Architectural Constraint**: Zero-balance expectation at cycle end requires precise reconciliation logic and error handling outside standard clearing return mechanisms.