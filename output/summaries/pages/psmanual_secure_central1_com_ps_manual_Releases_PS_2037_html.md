# PS 2037 Release Summary: CEBA Repayment Reporting Requirements

- **Scope**: Updated EDC reporting requirements for CEBA loan repayments, establishing twice-monthly submission cycles with defined deadlines and account debiting schedules.

- **Reporting Schedule**: Two-window cadence—payments received 1st–15th reported by 22nd of same month; payments received 16th–last day reported by 7th of following month. Central 1 debits financial institution accounts on the 8th and 23rd of each month, then forwards funds to EDC same-day.

- **ServiceNow Integration**: CEBA Repayment Form in ServiceNow was revised to reflect the new reporting schedule; procedures and supporting images were updated to document the form completion process (Chapter 3, Central 1 Facilitated CEBA Application Procedures).

- **Account Debit Mechanism**: Central 1 acts as intermediary, debiting financial institution current accounts on fixed dates (8th and 23rd) rather than variable settlement; architects must account for this dual-debit reconciliation pattern in GL and liquidity models.

- **Data Flow Dependencies**: Reporting relies on Central 1's receipt and aggregation of financial institution submissions; delays in submission impact EDC fund transfers on the 8th/23rd debit dates—no grace period or exception handling documented.

- **Documentation Artifacts**: FAQ added to Section 7.3 addressing repayment reporting deadlines; Quick Reference Guide (9140) serves as primary procedural reference for implementation.

- **Support Contact**: digitalbanking_support@central1.com or 1-888-889-7878 Option 2 for clarifications on deadline or submission requirements.