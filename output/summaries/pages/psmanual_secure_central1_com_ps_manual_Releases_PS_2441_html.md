# PS 24:41 Release Summary – Wires Enhancement

- **Release scope**: Enhancement to Wire transfer processing module enabling receipt and extraction of structured remittance information (SRI) from incoming wire messages.

- **Key enhancement**: Added capability to parse, identify, and deliver XML-formatted structured remittance data embedded within incoming wire transactions—addressing data enrichment needs for downstream reconciliation and customer reporting.

- **New operational procedures**: Section 19.3 documents two workflows: (1) verification logic to detect presence of structured remittance information in inbound wires, and (2) request mechanism to extract and deliver XML payload to end customers.

- **Data structure**: Structured remittance information flows as XML within wire message envelope; architects should expect XML schema validation requirements and potential mapping between wire message standards (likely ISO 20022 or SWIFT MT) and internal data models.

- **Integration dependency**: Wire ingestion pipeline must support conditional routing based on SRI presence detection; extraction logic requires XML parsing and customer-level entitlement/delivery controls.

- **Architectural consideration**: Design should accommodate variable SRI payload sizes and implement idempotent request handling for XML delivery to prevent duplicate customer data feeds.

- **Support/governance**: Contact Client Support Services (1-888-889-7878, Option 1 or support@central1.com) for implementation questions or clarifications on SRI format specifications.