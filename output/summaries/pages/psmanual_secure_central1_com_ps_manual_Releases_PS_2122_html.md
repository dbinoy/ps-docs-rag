# Payment Solutions Release Summary: Version 21:22

**Overview:** Documentation update for Interac e-Transfer® Online Administration System (OAS) covering enhanced transaction tracing, transfer memo viewing, and remittance detail capabilities.

**Key Concepts & Updates:**
- **Interac e-Transfer transaction tracing** via OAS (Section 4.1) - enables visibility into electronic transfer processing workflows
- **Transfer Memo viewing** (Section 4.4, new) - capability to retrieve transaction-level memo/reference data within OAS
- **Remittance Details viewing** (Section 4.5, new) - new data exposure for remittance information retrieval through OAS interface
- **Terminology standardization** (Section 2.1) - formalized definitions for Electronic Transactions Volume and OAS terminology

**Data Flows & Integration Points:**
- OAS serves as the primary administrative interface for querying Interac e-Transfer transaction state and metadata
- Customer profile summary retrieval (Section 6.2) updated—suggests changes to profile data model or query logic
- Transfer memo and remittance details are discrete data structures now independently accessible, indicating potential API or UI endpoint additions

**Constraints for Architects:**
- Interac e-Transfer is a regulatory/branded payment network—changes likely subject to Interac operational standards and certification requirements
- FAQ expansion (Section 2.2) suggests new user confusion points; design should anticipate support burden around new features

**Support Contact:** Client Support Services (1-888-889-7878 Option 1 or support@central1.com)