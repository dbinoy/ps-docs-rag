# Summary: Traces and Reversal Requests for International Transfers

- **Purpose**: Documents trace and reversal request procedures for international transfers within the Payment Solutions platform, specifically addressing how to investigate and resolve transfer issues.

- **Trace Management**: International transfer traces follow the same operational model as electronic bill payment traces; operators use BPCV (Bill Payment Confirmation Verification) and BPRE (Bill Payment Reversal/Exception) reports to audit transfer timing, receiving biller identification, and credited account numbers.

- **Online Tracing System Integration**: Trace investigations require escalation to the Online Tracing System (referenced as "Part" in documentation); this is a dependency for root-cause analysis of failed or delayed transfers.

- **Reversal Request Constraint**: Reversal requests are explicitly **prohibited** for international transfers as a fraud prevention control—this is a hard business rule that architects must enforce at the API and workflow layer.

- **Third-Party Dependency**: Agility Forex is the operational partner responsible for issue remediation when problems occur; there is no automated reversal pathway, only manual reconciliation through Agility Forex support channels (contact details in Section 1.3).

- **Data Structure Dependencies**: BPCV and BPRE reports imply structured logging of: transfer timestamp, destination biller entity, credited account identifier, and transfer status—these fields must be queryable and auditable.

- **Design Constraint for Enhancement**: Any new international transfer features must prevent reversal initiation at all system touchpoints (UI, API, batch processes) and route all exception handling through Agility Forex escalation workflows rather than automated reversals.