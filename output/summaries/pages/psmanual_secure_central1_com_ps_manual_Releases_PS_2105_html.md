# Summary: PS 2105 Release (February 5, 2021)

- **Purpose**: Release notes documenting a revision to the Digital & Payment Services Fee Schedule (Form 2725) effective February 5, 2021

- **Scope constraint**: Form 2725 is restricted to BC and Ontario Class A credit unions only—any system enhancements or integrations must enforce this geographic and institutional classification filter

- **Document artifact**: Form 2725 represents a formal fee schedule data structure; architects should verify version control and audit trail mechanisms for regulatory compliance (potential OFSI/regulatory reporting dependency)

- **Reference dependency**: Full technical details are documented in a separate secure site news item (linked but not reproduced here)—architects must access that resource to understand specific fee changes and their downstream impacts on transaction processing, billing systems, or reporting modules

- **Data governance**: This is a versioned regulatory document marked "Revised" in the Document Library—confirm if form changes trigger recalculation engines, customer communication workflows, or contract amendment processes

- **Support integration point**: Client Support Services (phone/email) is the operational escalation path; consider whether support systems need lookup tables or knowledge base entries tied to Form 2725 revisions

- **Architecture implication**: If this fee schedule feeds pricing engines, billing systems, or customer-facing APIs, those integrations may require deployment updates tied to release dates