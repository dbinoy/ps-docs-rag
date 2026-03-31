# Summary: 3 Legal Considerations for FX Notes

**Overview:** This page outlines mandatory regulatory and compliance requirements that financial institutions must satisfy when processing foreign currency note transactions through the Payment Solutions platform.

**Key Concepts & Regulatory Requirements:**
- Financial institutions bear sole responsibility for statutory compliance; documentation serves as convenience reference only and does not substitute for actual legislation
- Three primary regulatory frameworks apply: PCMLTFA/PCMLTF Regulations (AML/CTF), Economic Sanctions regulations (designated countries/persons), and institution-specific agreements with Globex 2000
- Sanctions prohibit direct/indirect financial transactions, service provisioning, property dealings, and asset availability to designated persons/countries; impose search and reporting obligations on financial entities

**Critical Compliance Controls:**
- Third-party determination logic is essential for detecting indirect benefit flows to designated persons—this requires enhanced due diligence in transaction authorization workflows
- Sanctions are subject to real-time change; static compliance rule sets are insufficient (requires dynamic reference to Global Affairs Canada data sources)
- Additional federal/provincial legislation (privacy, human rights) may intersect with FX transactions—institutions must implement supplementary policies beyond this guidance

**Integration Dependencies:**
- External dependencies: AML Compliance Officer contact, FINTRAC liaison, Global Affairs Canada website for current sanctions lists
- Internal dependencies: Globex 2000 agreement requirement (account-level prerequisite); Operations Manual Program reference for PCMLTFA compliance details
- Contact escalation point: Account Executive for Globex 2000 agreement administration (Section 1.3)

**Architect Considerations:**
- Transaction validation logic must incorporate real-time sanctions screening and AML rule engines before FX note processing
- No system-of-record maintained on this page; external regulatory sources are authoritative, implying need for regulatory data feeds and refresh mechanisms