# Summary: Navigating Wires and Viewing Wire Details

- **Purpose**: Defines the Wires application's four primary views for managing outgoing and incoming wire transfers, their status lifecycles, and user interaction patterns for viewing wire details.

- **Four Segregated Wire Views**:
  - **Pending Outgoing**: Requires 1 or 2 approvals; requires "View Outgoing Transfers" + 2-step token + "Authorize Outgoing Transfers" permission
  - **Pending Incoming**: User must accept/return; requires "View Incoming Transfers" + 2-step token + "Accept Incoming Transfers" permission
  - **Submitted Wires**: Historical view (default 5-day window, filterable); shows all outgoing wires regardless of status
  - **Received Wires**: Historical view (default 5-day window, filterable); shows all incoming wires with accept/return/investigation states

- **Status Lifecycle for Outgoing Wires**: 1 Approval Required → 2 Approvals Required → Pending (import delay, sanctions scanning, EFM fraud review) → Sent/Returned/Cancelled/Hold (for non-participating institutions missing cut-off)

- **Sanctions List Integration**: Wires destined to participating financial institutions transition immediately to "Sent" post-approval and sanctions scanning; non-participating institutions may show "Pending" during import and require manual handling on missed cut-offs

- **Branch-Level Access Control**: Wire visibility is filtered by MTS branch assignments per user; requires tight integration with Chapter 9 (MTS Branch Management) and Chapter 8 (Wires User Management) for role-based access

- **Structured Remittance Data Flow**: Incoming wires optionally contain XML-formatted remittance information (invoice, PO, customer details); viewable via UI but requires manual escalation to Central 1 Support for delivery to downstream systems

- **External Dependency**: Enterprise Fraud Management (EFM) system processes outgoing wires for fraud detection; "Pending" status can indicate active EFM review, introducing asynchronous processing delays