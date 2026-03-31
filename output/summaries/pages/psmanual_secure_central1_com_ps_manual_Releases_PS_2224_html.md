# Release 22:24 (September 26, 2022) - Summary

- **Overview**: Updates to Country-Specific Guidelines and Instructions (Form 3597) affecting sanctions/warning messaging and payment instruction logic, synchronized across Payment Solutions and the Wires application.

- **Sanctions Logic Changes**: Removed sanctions messaging for 4 countries (Bolivia, Brazil, Laos, St. Maarten); added for 10 countries (Bosnia and Herzegovina, Burkina Faso, Gibraltar, Guinea, Kenya, Mozambique, Nigeria, Paraguay, Tunisia, UAE); updated language for China (removed Tax Haven reference) and Ukraine (expanded Crimea restrictions to include Luhansk/Donetsk).

- **Payment Instructions Modifications**: Added new country routing/instructions for Belize; updated existing instructions for Colombia, Costa Rica, UAE, and Vietnam—suggests Form 3597 contains country-indexed payment routing rules, not just compliance flags.

- **System Integration Dependency**: Form 3597 updates are bidirectionally synchronized with the Wires application—architects must account for dual-system update coordination and potential consistency validation requirements.

- **Data Structure Implication**: Country-level record in Form 3597 likely contains composite fields: `country_code`, `sanctions_status`, `warning_message`, `payment_instructions`—changes to any field require comprehensive country profile versioning.

- **Regulatory Constraint**: Sanctions messaging removals suggest OFAC/sanctions list monitoring is external/upstream; this release reflects policy changes, indicating the system is customer-facing guidance layer, not authoritative sanctions source.

- **Support Contact**: Client Support Services (1-888-889-7878, Option 1; support@central1.com) owns questions—suggests this release may impact user workflows requiring support escalation.