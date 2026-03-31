# PS 2003 Release Summary (February 28, 2020)

- **Purpose**: Documentation update addressing user authentication and workflow issues in PaymentStream AFT (Automated File Transfer) module, with FAQ clarifications added.

- **Key Issue Resolved**: Business members were receiving login error messages when accessing PaymentStream AFT post-authentication; solution involved bookmark creation guidance to prevent session/redirect failures.

- **Affected Component**: PaymentStream AFT Part within the AFT Volume origination workflow—specifically the initial login and session persistence flow.

- **Documentation Change**: Added Question #12 to Section 2.2 (Frequently Asked Questions) in the AFT Volume originating AFT via PaymentStream AFT Part documentation; specific FAQ content not detailed in this summary.

- **Integration Context**: PaymentStream AFT is a client-facing entry point that depends on secure session management and URL handling; bookmark workaround suggests potential state management or redirect URL complexity in the authentication flow.

- **Support/Escalation**: Issues routed to Client Support Services via phone (1-888-889-7878, Option 1) or email (support@central1.com)—indicating this was a known usability friction point.

- **Architect Consideration**: Session handling and URL-based navigation design in PaymentStream AFT may have UX/reliability constraints; any authentication or workflow redesigns should account for stateful session requirements and bookmark dependency patterns.