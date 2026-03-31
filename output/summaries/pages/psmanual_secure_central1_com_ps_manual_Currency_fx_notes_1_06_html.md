# FX Notes Login Documentation Summary

- **Purpose**: Documents the authentication and access workflow for FX Notes, a foreign exchange application within the Client Centre portal ecosystem.

- **Authentication prerequisite**: Users must be provisioned in Client Centre with one of two roles—CPS Admin Security Officer or Client Centre User—and explicitly granted FX Notes application access through the User Management module (Chapter 5).

- **Access mechanism**: Multi-step navigation required: Client Centre portal (https://clients.central1.com) → Applications catalog → FX Notes selection; no direct URL login documented.

- **Session handling**: System maintains cookie-based state; first login, cookie deletion, or private/incognito browsing triggers username re-entry prompt; application relies on standard browser session management without apparent multi-factor authentication mention.

- **Integration dependency**: FX Notes is one application among multiple grouped by functional type (Admin & Support, Payments, etc.) within a centralized Client Centre application catalog; architecture implies shared authentication/authorization infrastructure.

- **User discovery pattern**: Application discoverability supports both browsing (scrollable catalog) and bookmarking (favorites), suggesting frequently-accessed applications are stored client-side or in user preferences.

- **Security constraint**: Mandatory logout and browser closure required when leaving workstations; no timeout policy or concurrent session limits explicitly defined—potential architectural gap for unattended sessions.