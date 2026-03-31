# Release 21:04 Summary for Solutions Architecture

- **Purpose**: Documents CEBA (Canada Emergency Business Account) reporting procedure updates in ServiceNow following Export Development Canada (EDC) policy changes regarding loan repayment and administration fee reporting.

- **Key Process Change - Payment Reporting**: The CEBA Repayment form now supports backdated payment entries; the payment date picker removed the constraint limiting selections to current reporting periods, enabling users to report loan repayments made outside their original reporting window.

- **Key Process Change - Admin Fee Calculation**: EDC introduced a $2,500 minimum fee floor for loan administration fees. System must support calculated fee submission with EDC applying floor logic downstream (if calculated < $2,500, EDC raises to $2,500; if calculated ≥ $2,500, EDC pays calculated amount). Note: calculated fees are editable within the "CEBA Loan Administration Fee – Received" category state in My Company module.

- **Critical Constraint - Quarterly Fee Deadline**: Loan administration fee reporting has a hard deadline of the 15th calendar day each quarter and can only report for the previous quarter. Central 1 cannot process late submissions; this represents a firm integration boundary with EDC's reporting cycle.

- **Data Structure Considerations**: The CEBA Repayment form displays calculated forgiveness amount (derived from total borrowed); outstanding principal requires monthly-end reporting values. These fields depend on accurate principal tracking across repayment periods.

- **Integration Dependency**: Tight coupling to EDC's quarterly reporting window and fee calculation rules; any enhancement to fee logic or payment date handling must coordinate with EDC's backend validation and settlement processes.

- **Support Contact**: Client Support Services handles implementation questions (1-888-889-7878 Option 2 or digitalbanking_support@central1.com).