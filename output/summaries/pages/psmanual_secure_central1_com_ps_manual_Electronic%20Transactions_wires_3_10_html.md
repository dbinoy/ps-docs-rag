# Summary: Logging in to Wires

**Overview:** This page documents the authentication flow and navigation sequence for users to access the Wires application through the Client Centre portal.

**Key Concepts & Process Flow:**
- Multi-tier navigation required: Client Centre (https://clients.central1.com) → Applications → PaymentStream Direct → Transfers → Wires
- Authentication dependency on Client Centre; users must enter username/password at initial login or after cookie deletion/incognito session termination
- Applications are categorized by type (Admin & Support, Payments, etc.) with favorites functionality for quick access

**Integration Points & Dependencies:**
- Wires module is a child application within the PaymentStream Direct ecosystem, accessed through the Client Centre authentication layer
- Client Centre acts as the identity and access management (IAM) gateway—all Wires access is gated by Client Centre credentials
- No direct URL access to Wires; must traverse the Client Centre portal workflow

**Security Constraints & Operational Rules:**
- Mandatory session termination requirement: users must explicitly log off Client Centre and close browser when stepping away or finishing work
- Implicit session context: first-time users, cookie deletion, or private browsing mode triggers upstream username prompt before Client Centre login page
- No persistent authentication across browser sessions

**Architectural Implications:**
- Wires inherits Client Centre's session management and authentication state—any enhancement to Wires must respect Client Centre session lifecycle
- Navigation structure suggests potential for streamlining user journeys if favorites are underutilized; consider deep-linking strategy for frequently accessed features