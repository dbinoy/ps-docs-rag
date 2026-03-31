# Summary: BPRP Data Files

**Overview:** This page documents the Bill Payment Remittance Processing (BPRP) data file formats and delivery mechanisms that enable Corporate Creditors to automatically post customer payments received through Central 1's payment processing system.

## Key Points for Architecture

- **Scope & Applicability:** BPRP applies to BC and Ontario credit unions plus other Central 1 clients; other provinces handled by respective provincial centrals (implies multi-tenant, region-specific configuration)

- **Two Supported File Formats:**
  - **Flat File:** Proprietary Central 1 format requiring custom programming for integration; generated 5 days/week regardless of transaction volume
  - **EDI Format:** CPA Rule H6 compliant industry standard; compatible with third-party software; generated 5 days/week only when transactions exist (asymmetric behavior vs. Flat File)

- **Distribution Channel:** Files delivered via File and Report Exchange (referenced as a separate system component); requires separate documentation/procedures for end-user access (Section 6.8)

- **Data Flow:** Central 1 → File and Report Exchange → Corporate Creditor downloads → imports into their internal system for account crediting (offline batch process, not real-time API)

- **Operational Considerations:** System outages trigger proactive email notifications via Client Support Services; file format changes require manual request to billers@central1.com or fax 1-855-730-6424 (no self-service configuration)

- **Architecture Implications:** Design must account for two distinct file generation rules and handle conditional file delivery; File and Report Exchange is a critical dependency for data retrieval