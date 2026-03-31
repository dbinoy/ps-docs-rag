# Release 25:02 Summary – Enterprise Fraud Management v4.7

- **Overview**: January 15, 2025 release updating Enterprise Fraud Management documentation to align with version 4.7 platform upgrades, with emphasis on incident management workflows and fraud classification procedures.

- **Key Concept – Risk Scoring**: Introduction of "Highest Score" column/filter in incident lists (Section 7.3, 7.5) and "Risk Score" column in Activity timeline (Section 7.8); architects should understand this is a primary sorting/filtering mechanism for incident prioritization.

- **Process Change – Auto Risk Transactions**: Mandatory classification rule implemented—all Auto Risk transactions must now be explicitly marked as "Risk" or "No-risk" (Section 8.4); this represents a stricter state machine for transaction processing and may impact downstream automation logic.

- **New Functionality – Bulk Alert Operations**: Added bulk manual alert creation capability accessible from both incident page and Events search results page (Section 8.6); indicates expanded integration surface between incident management and event search subsystems.

- **Fund Recovery Workflow**: New "Initiate Fund Recovery" box introduced with conditional logic for when/how to use it (Section 8.10); architects need clarity on triggering conditions, approval workflows, and system dependencies (accounting/settlement systems likely involved).

- **Data Governance Constraint – Comment Visibility**: Comments are system-wide visible across applications; architects must enforce validation rules ensuring comments meet descriptiveness/appropriateness standards before persistence to prevent downstream data quality issues.

- **Tagging System**: New Section 7.4 introduces tagging capability for incidents; integration point for metadata management and potential filtering/search enhancements requiring data model updates.