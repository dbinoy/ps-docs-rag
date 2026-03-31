# Payment Solutions Release Summary: PS 23:03

**Overview:** Release notes documenting updates to Wires Data Extract Service file specifications (Form 9327) effective February 27, 2023.

## Key Changes & Concepts

- **Extract Scope Clarification:** Wires Data Extract Service contains *all wires* (not a filtered subset); documentation previously contained conflicting language that has been corrected.

- **AML Compliance Rule:** Wires flagged with cross-border status "Verify Manually" require mandatory review by the financial institution's AML (Anti-Money Laundering) team—architectural consideration for workflow/alerting systems.

- **Field Specification Updates:** Three core data fields modified in Chapter 4:
  - **MTS Ref No** (Format, Length, Example columns)
  - **Remittance Information** (Line 1 field length constraint)
  - **Sender FI to Receiver** (Line 1 field length constraint)

- **Data Format Alignment:** Sample XML and Report File outputs (Chapter 5) updated to reflect MTS Ref No format changes—validation schemas and parsers consuming this extract must be updated in sync.

- **File Format Type:** XML and Report file formats supported; schema validation dependencies exist downstream.

- **Integration Dependency:** Extract service integrates with AML team workflows; downstream systems must support routing/flagging of "Verify Manually" wires for manual intervention.

- **Support & Governance:** Changes documented in Form 9327; support contact escalation available via Central1 Client Support Services for implementation questions.