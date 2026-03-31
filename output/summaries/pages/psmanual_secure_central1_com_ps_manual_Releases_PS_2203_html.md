# Release 22:03 (January 31, 2022) Summary

- **Purpose**: Documentation clarification on agreement responsibility allocation for mobile deposit and corporate capture channels within the Deposit Processing subsystem.

- **Key Rule Change**: Central 1 explicitly does NOT provide agreement templates for mobile deposit or corporate capture customers; financial institutions must create their own agreements reflecting their risk tolerance and operational processes.

- **Mandatory Compliance Point**: Central 1's Service Schedule contains mandatory clauses that MUST be incorporated into customer-facing agreements created by financial institutions—this creates a dependency where institution agreements must reference/embed Central 1-mandated terms.

- **Affected Functional Areas**: 
  - Section 3.5 (Mobile Deposits): Institution owns agreement creation responsibility
  - Section 3.7 (Corporate Capture Deposit Processing): Institution owns agreement creation responsibility

- **Architectural Implication**: Any mobile deposit or corporate capture integration must account for external agreement management workflows outside Payment Solutions' control; system design cannot assume standardized contract templates or centralized agreement validation.

- **No New Data Structures/APIs Mentioned**: This is a process clarification, not a system change—no new integration points, schemas, or endpoint modifications documented.

- **Support/Escalation**: Client Support Services (1-888-889-7878 Option 1 or support@central1.com) for implementation questions regarding mandatory clause requirements.