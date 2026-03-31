# Summary: Payment Solutions Terminology (Clearing and Deposits)

**Overview:** This page defines core terminology for the FX Drafts application and supporting Central 1 infrastructure used in foreign currency draft processing and user/file management.

**Key Concepts & Definitions:**
- **FX Drafts application**: Primary tool for quoting rates, entering foreign currency drafts (including USD), and in-branch printing—the core transaction system for this domain
- **Beneficiary**: The payee entity (person or legal entity) on a draft—critical for transaction routing and compliance verification
- **Transit Number composition**: Institution Number (3-digit CPA-assigned code: 809 for BC CUs, 828 for Ontario CUs) + Branch Number (5-digit identifier) together form the complete routing identifier—essential for inter-institution settlement

**Integration Points & Data Flow:**
- **Client Centre**: Central 1's secured digital portal serving as both application gateway and file exchange interface
- **File and Report Exchange**: Dual-access system (SFTP direct connection or Client Centre web interface) for authorized file uploads/downloads—critical integration point for batch processing and reporting
- **User Management application**: Handles provisioning of Client Centre Users and Security Officers with 2-step token management—prerequisite for FX Drafts access

**Compliance & Regulatory Constraints:**
- **PCMLTFA (Proceeds of Crime Money Laundering and Terrorist Financing Act)**: Referenced as applicable regulatory framework—implies mandatory AML/CFT validation requirements in draft processing workflows
- **User Management Security Officer role**: Gatekeepers for user provisioning and token management—architectural implication: segregation of duties between operational users and security administrators