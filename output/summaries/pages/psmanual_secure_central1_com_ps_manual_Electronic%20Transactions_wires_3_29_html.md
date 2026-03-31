# MemberDirect® Business (MDB) / Forge Commercial Wires Integration Summary

- **Purpose**: Enables business customers to initiate domestic and international wire transfers through MDB/Forge Commercial (FX or USD/CAD options), with wires routed to the Wires application for financial institution review and processing

- **Proxy Architecture**: Each business customer requires exactly one MTS User ID (formatted as `mdb-businessname`, lowercase, max 20 chars, no spaces) that acts as a proxy/integration point between MDB/Forge Commercial and the Wires application; multiple business users funnel through this single MTS User ID for wire identification and tracing

- **Three-Tier Authorization Model**:
  - MTS Branch Settings define Level 1 and Level 2 authorization thresholds (recommends $1.00 Level 1 to force review of all business wires)
  - BUA manages per-business user limits
  - Wires Application enforces approvals; Level 1 threshold amounts bypass approval entirely (critical constraint for compliance)

- **Required Setup Dependencies**: User Management Security Officer → MTS Administrator → BUA Administrator chain; business users require 2-Step Security token and two-factor authentication; Wires Application Users must have appropriate permissions and approval limits for the specific transit used

- **Fraud Monitoring Integration**: Outgoing wires flagged in Central 1's Enterprise Fraud Management (EFM) system are held silently (no customer notification); architects must understand EFM sits outside the main wire processing workflow

- **Transit Isolation Pattern**: Best practice recommends home transit number dedicated to MDB/Forge Commercial business wires (separate from in-branch transit) to enable role-based access control, targeted authorization limits, and reporting segregation without affecting branch operations

- **Critical Constraint**: Do not create corresponding Client Centre User IDs for business customers; they authenticate only through MDB/Forge Commercial with 2FA, not Client Centre