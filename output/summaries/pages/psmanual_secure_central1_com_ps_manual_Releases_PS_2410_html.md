# Payment Solutions 24:10 Release Summary

- **Release scope**: February 28, 2024 update to Wires Part documentation covering add-on fee management, MDB/Forge Commercial wire processing, and authorization limit clarifications

- **Add-on fee automation**: Wires application now auto-populates the Fee field for high-priority and future-dated wires when pre-populated fees are configured at the financial institution level—requires configuration in Wires application settings

- **MDB/Forge Commercial wire support**: New Chapter 29.10 and clarified Sections 29.2, 29.3 define roles, authorization limits, and processing workflows for business customer wires; integration involves MTS Branch Management system for authorization governance

- **Customizable wire elements**: Section 4.2 expands wire fee structure to include future-dated and priority wire add-ons; these are configurable elements managed through Chapter 11 procedures

- **Wires Data Extract Service naming**: Formal agreement terminology uses "WTS Data Extract Services (Optional)"—critical for contract alignment and system integration documentation (Section 4.4)

- **Authorization limit constraints**: MDB/Forge Commercial wires operate under distinct authorization rules per Section 9.5; clarification across Sections 22.1 and 29.3 indicates tiered approval workflows tied to wire type and branch settings

- **Documentation artifact**: Customization Request #6493 revised to reflect add-on fee structure—indicates this change may require downstream system customization requests or configuration templates