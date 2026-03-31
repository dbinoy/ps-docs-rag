# FYI – January 2020 Summary

- **Purpose**: Documentation of January 2020 updates to the Payment Solutions Manual covering access controls, user administration, and document standards.

- **2-Step Security Token Lifecycle**: Soft token replacement requires users to manually delete the old token from their authenticator app before installing the new token; the system prompts re-registration at next login.

- **Token Deactivation Dependency**: When replacing any token type, the existing token must be explicitly deactivated before a new token can be assigned—sequential state transition required.

- **Password Reset SLA**: One to two minute delay documented for password reset operations; impacts user onboarding and support workflows.

- **Authenticator App Integration Point**: Third-party authenticator apps control soft token storage and registration; UX varies by app (e.g., "Scan a Barcode" workflow not guaranteed across implementations)—potential support complexity.

- **Transaction Code Reference Standard**: AFT (Automated Funds Transfer) transaction codes now reference CPA Standard 007 for validation; impacts document library controls and payment file processing validation rules.

- **Token Removal Scope**: Token removal applies broadly across access loss scenarios (user offboarding, device changes, access revocation)—no differentiation in removal logic between use cases.