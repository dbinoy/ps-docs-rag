# Payment Solutions 24:30 Release Summary

- **Purpose**: August 15, 2024 release clarifying Record Entry Limit constraints for AFT (Automated Funds Transfer) transaction backdating and future-dating capabilities across transaction types and release mechanisms.

- **Key Constraint - Backdating**: PADs (Pre-Authorized Debits) support 173-calendar-day backdating; direct deposits limited to 30-calendar-day backdating.

- **Key Constraint - Future-Dating**: 
  - Manual data entry release type: both PADs and direct deposits capped at 14 calendar days
  - File upload release type: both PADs and direct deposits capped at 45 calendar days
  - Automatic data entry release type: **no future-dating permitted** (system extracts 3 business days pre-due-date)

- **Data Structure Consideration**: Record Entry Limit field requires transaction-type-aware validation logic (PAD vs. direct deposit) and release-type-aware logic (manual entry vs. file upload vs. automatic).

- **System Integration Point**: Automatic release transactions have hard dependency on a 3-business-day extraction cycle tied to due date calculations—architects must account for this in any workflow redesign or due-date modification features.

- **Backward Compatibility Risk**: These clarifications suggest previous ambiguity; validate existing production configurations against new constraints to identify non-compliant scheduled transactions.