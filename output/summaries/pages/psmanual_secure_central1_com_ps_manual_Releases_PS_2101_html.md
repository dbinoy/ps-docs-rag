# Payment Solutions Release 21:01 Summary

- **Purpose**: Documentation updates to Funds Transfer processing and IBAN validation rules, effective January 8, 2021.

- **Compliance Review Deadline Rule**: Wires submitted after 6:00 PM ET requiring manual compliance review are held and released the next business day morning, not same-day. This is a hard constraint in the transfer processing workflow (Section 11.6).

- **MTS Outbox Visibility Lag**: Outgoing wires sent via MTS (Money Transfer System) may experience delayed appearance in the MTS Outbox—documentation now clarifies this behavior to prevent false negative scenarios where users cannot immediately verify sent transfers.

- **IBAN Data Structure Addition**: Form 9252 (International Bank Account Number Countries) now includes IBAN specifications for Libya, indicating the system supports country-specific IBAN format validation rules as a configurable data set.

- **Validation Constraint—Non-Blocking IBAN Errors**: The Wires application does not prevent transmission of wires with missing or incorrectly formatted IBANs. IBAN validation is informational/logged only, not a pre-submission gate—important for exception handling and downstream reconciliation.

- **Integration Dependencies**: Compliance review logic and MTS synchronization are coupled processes affecting transfer timing; IBAN validation integrates with the Wires application but does not block send operations.

- **Support Contact**: Client Support Services handles implementation and clarification questions (1-888-889-7878, Option 1; support@central1.com).