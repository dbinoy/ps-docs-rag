# Payment Solutions 22:11 Release Summary

- **Purpose**: Major documentation update consolidating Funds Transfer Part content into restructured Wires Part (Funds Transfer Part now obsolete); substantive reorganization with chapter renumbering across Electronic Transactions Volume.

- **Key Architectural Change**: Live foreign exchange rates now integrated into Wires application (previously required manual Bank of Canada contact); rate management split into separate chapters for spreads (Ch. 12) vs. live rate viewing (Ch. 13).

- **Multi-Currency Support Expansion**: Added routing instruction forms for NZD (Form 9352), Kazakhstan payment classification codes (Form 9471), and Uganda payment purpose codes (Form 9415); supports domestic CAD/USD/EUR and international AUD, CHF, GBP, JPY, MXN, PLN wire flows.

- **System Requirements Constraint**: Internet Explorer removed from supported browsers; Microsoft Edge marked as incompatible with Wires Application—impacts client infrastructure planning and browser compatibility validation.

- **Compliance/Regulatory Handoff**: Removed most compliance content from documentation; architects must ensure FINTRAC EFT reporting, sanctions list scanning, and PEP/HIO identification workflows are externalized to compliance officer consultation or Operations Manual Program—not embedded in system design.

- **Management & Approval Framework**: Second approval now required only for wires *exceeding* (not equal to) MTS Level 2 authorization threshold; MTS used for administrator, user, and branch management across chapters 6-9.

- **Integration Dependencies**: References updated across User Management Part (Access & Administration Volume) and Deposit Processing Part (Clearing & Deposits Volume)—design changes require cross-volume documentation sync and form version control (13 forms revised, 2 forms added).

- **Data Services**: New Wires Data Extract Service (Form 2592, specification Form 9327) available to BC, Manitoba, Ontario, and other Central 1 clients—represents queryable extraction point for external integrations.