# Payment Solutions 20:09 Release Summary

- **Release scope**: Documentation updates to AFT (Automated Funds Transfer) Re-presentment service clarifications for PaymentStream™ AFT Originators, effective April 15, 2020

- **Core process**: AFT Re-presentment allows enrolled originators to re-present dishonored PAD (Pre-Authorized Debit) transactions; settlement reports include identifiable markers for re-presented transactions to enable tracking and reconciliation

- **Service enrollment workflow**: Central 1 confirms AFT Re-presentment service activation via ServiceNow ticket, including confirmed start date and request-related metadata—architects should design for ticket-driven service provisioning integration

- **Key architectural updates**:
  - Section 1.3 documents re-presentment request mechanisms and settlement report structures
  - Section 5.4 specifies preference indication procedures and ServiceNow confirmation requirements
  - FAQ expansion (Questions 12-26) codifies rules distinguishing AFT Originators with vs. without re-presentment enrollment

- **Critical constraint**: Re-presentment service is restricted to **enrolled AFT Originators only**—eligibility checks must validate enrollment status before enabling re-presentment workflows or settlement report filtering

- **Data dependency**: Settlement reports must contain distinguishable transaction markers for re-presented items; architects must ensure reporting data schema supports identification and filtering of re-presented vs. original transactions

- **Deprecation note**: "AFT Re-presentment Service – Quick Reference" (document 9014) is obsolete; all content migrated into Introduction to AFT manual sections—update documentation references and decommission standalone quick reference artifact