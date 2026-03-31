# wwparcel.html Summary for Solutions Architect

- **Page Purpose**: Comprehensive table of contents for Payment Solutions manual covering three primary modules: Enterprise Fraud Management (EFM), PaymentStream™ Direct, and Wires, with supporting documentation on user management, policies, and transaction processing.

- **Core Modules & Data Flows**:
  - **EFM**: Incident management (tagging, filtering, referring), transaction alert classification (fraudulent/legitimate/auto-risk), manual alert administration, fund recovery workflows
  - **PaymentStream Direct**: Customer profile functions, bill payments (including CRA tax payments via Forms RC159/RC160), debit card locking, e-statement delivery
  - **Wires**: Outgoing/incoming wire processing with multi-model support (centralized/decentralized), foreign exchange spread management, IBAN validation, country-risk assessment (tax haven/sanctioned nations), FINTRAC EFT reporting compliance

- **Critical User Management Architecture**: Role-based access control across three user pathways (Client Centre users, existing CPS Admin Security Officers, new CPS Admin Security Officers) with separate permission models for each module; MTS (Management Transaction System) handles Wires administrator/user provisioning with queue-based change authorization workflows

- **Key Constraints & Compliance**: Wire cut-off times, PEP/HIO determination requirements, Interac® e-Transfer limits policy enforcement, internal control policies for user segregation, record-keeping mandates for FINTRAC reporting; mobile deposits and bill payments have module-specific alert handling

- **Integration Dependencies**: Wires application integrates with EFM for transaction monitoring; Bill Payments module handles CRA-specific payment types (GST/HST, corporation taxes, payroll deductions); Lock Your Debit Card and Switch Concierge™ by ClickSWITCH are ancillary functions within PaymentStream Direct

- **Data Structures & Processing Models**: Wire templates support creation/editing/restoration; incident filters and internal data lists are customizable; transaction alert revision capability suggests audit trail requirements; settlement procedures differ by transaction type (Interac® e-Transfer vs. Wire)

- **Architect Must Know**: This manual covers policy enforcement, not technical APIs—design enhancements require understanding role-based permission hierarchies, multi-stage approval queues (particularly in Wires), and regulatory reporting obligations (FINTRAC). The decoupling of EFM monitoring from transaction origination systems suggests event-driven architecture patterns.