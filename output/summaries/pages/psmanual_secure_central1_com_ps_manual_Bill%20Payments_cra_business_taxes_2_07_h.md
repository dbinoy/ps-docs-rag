# PaymentStream Direct Business Taxes Access - Architecture Summary

- **Scope**: Documents login procedures and environment access for Business Taxes functionality in PaymentStream Direct, covering both test and production pathways through the Client Centre portal.

- **Dual Environment Architecture**: Two isolated environments—TEST (Prev-Comp mirror and SYS preview) and PRODUCTION—require separate authentication flows but share identical UI/UX patterns; test transactions are not forwarded to CRA, production transactions are automatically relayed to Canada Revenue Agency.

- **Access Control Model**: Feature access gated by role-based permissions (CPS Admin Security Officer or Client Centre User with Business Taxes entitlement); see Chapter 5 for user management detail—architectural implication is that access control is enforced upstream in Client Centre before PaymentStream Direct instance access.

- **Authentication Integration Point**: Client Centre (https://clients.central1.com) acts as SSO/credential broker for PaymentStream Direct; session cookies persist across application selection; first login, cookie deletion, or incognito mode triggers username re-prompt—relevant for designing federated auth or session handling.

- **Application Selection Navigation**: Multi-tier UX (Applications > Environment Selection > Payments module) with application grouping/favorites functionality; applications discoverable via categorization (Admin & Support, Payments)—impacts information architecture for future feature additions.

- **CRA Transmission Contract**: Production environment establishes a data flow contract where Central 1 acts as intermediary processor/forwarder to CRA; test environment provides sandbox isolation for training without CRA submission—critical constraint for compliance and audit trails.

- **Cross-Reference Dependencies**: Page references Chapter 5 (user management) and Section 8.2 (tax form submission procedures)—suggests Business Taxes is modular component with separate auth, submission, and management workflows that must remain loosely coupled.