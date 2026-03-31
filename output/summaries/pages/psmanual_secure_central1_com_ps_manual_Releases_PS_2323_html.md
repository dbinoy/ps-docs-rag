# Release 23:23 (October 4, 2023) - Wires Part Documentation Update

- **Overview**: Documentation update for Wires Part reflecting migration to a new wires platform, with primary changes to wire processing fee billing model and Saturday wire handling.

- **Key Process Change**: Wires created on Saturday destined for participating financial institutions now appear in Pending Incoming wires list the following business day (previously different behavior); settlement processing timeline remains unchanged.

- **Billing Model Shift**: Wire processing fees migrated from real-time/transactional billing to month-end consolidated billing; this affects all fee display, settlement documentation, and customer communications throughout the system.

- **New System Definitions**: Added ISO2022 and Lynx as defined terms in the Wires Part—likely representing new technical standards or platform components that architects should reference in wire processing workflows.

- **Enriched Payment Information**: New capability introduced across wire creation flows (Sections 16.7, 17.5) with references to Prohibited Remittance Content Procedure—indicates enhanced metadata handling and compliance validation integration points.

- **Financial Institution Integration Dependency**: Wire settlement and visibility depend on destination institution's participation status in the new wires platform; architects must account for institutional eligibility validation in outgoing wire processing.

- **Documentation Coverage Scope**: Updates span the full wire lifecycle—creation, FX quoting, submission receipts, incoming acceptance/return, and settlement—indicating all integration points require alignment with fee billing and processing rule changes.