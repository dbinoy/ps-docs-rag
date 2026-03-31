# Summary: Editing an Outgoing Wire

- **Purpose**: Defines the workflow and constraints for modifying outgoing wire transfers prior to approval, with role-based access controls and audit logging.

- **Editable vs. Locked Fields**: Users can modify Sender, Beneficiary, Payment Details, Sender FI to Receiver FI Information, and Regulatory information fields. Immutable fields (Sending FI, Beneficiary FI, Amount, Currency, Fees, Sender FI Details, Receiver FI Details, Intermediary) require wire cancellation and recreation if changes are needed.

- **Role-Based Access Control**: Three user categories have edit permissions—(1) wire creator until full approval, (2) users with "Authorize Outgoing Transfers" permission until second-level approval, and (3) subsequent editors are restricted to creator and initial editor only. Critical constraint: users cannot approve wires they edit.

- **Two-Factor Authentication**: Required only for users with approval permissions accessing the "Pending Outgoing" queue; creators accessing "Submitted Wires" bypass 2FA, indicating differential security posture based on authorization level.

- **Audit Trail**: System records transaction modification metadata (timestamp and user ID of most recent edit) in the Transaction Information section, essential for compliance and reconciliation.

- **State Management Dependencies**: Wire editability depends on approval workflow state (single vs. two-step approval paths); editing resets approval gates, requiring re-authorization by secondary approvers.

- **UI/Process Flow**: Edit workflow involves authentication → queue selection → wire selection → field modification → confirmation review → receipt generation, with no explicit API endpoints or system integration points documented.