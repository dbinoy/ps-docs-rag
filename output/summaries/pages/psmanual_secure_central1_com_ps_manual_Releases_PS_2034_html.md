# Release 20:34 Summary for Solutions Architect

- **Purpose**: Correction to Primary Identification validation rules in the Wires Part following errors introduced in Release 20:30.

- **Primary Identification Definition Update** (Section 2.1, Definitions): Driver's licence reinstated as valid primary identification; Birth Certificate removed from the accepted list. This affects identity verification workflows in wire transfer processing.

- **Prior Release Correction**: Release 20:30 incorrectly removed Driver's licence from primary identification. Record of Landing and Permanent Resident Card removals in 20:30 remain valid (intentional changes).

- **Data Flow Impact**: Any system consuming Primary Identification enumeration for KYC/AML validation in wire transactions must be updated to reflect the corrected acceptable document types.

- **Affected Process**: Electronic Transactions Volume - Wires Part specifically; impacts identity verification logic at transaction initiation or settlement stages.

- **No New Integration Points**: This is a definitional correction, not a schema or API change (based on available documentation). Verify whether dependent systems require configuration updates or code changes to enforce the revised rules.

- **Support Channel**: Client Support Services for clarification on implementation impact (1-888-889-7878 Option 1 or support@central1.com).

- **Architect Consideration**: Assess whether system validations are hardcoded vs. config-driven; hardcoded lists will require code deployment, while config-driven approaches may only need data updates.