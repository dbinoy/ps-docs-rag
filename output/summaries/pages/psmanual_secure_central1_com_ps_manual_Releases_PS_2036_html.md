# PS 20:36 Release Summary

- **Release scope**: Documentation update to EMTC/EMFC File Specifications (Form 6195) for Interac e-Transfer® transaction reconciliation; no file format changes implemented

- **Key update**: Table 2 ("C" or "D" Record - Detailed Record), records 7-14 now include disambiguated field descriptions that vary based on transaction type (credit vs. debit), addressing previous ambiguity in specification

- **Critical data structure**: EMTC/EMFC files use record-type delimiters ("C" for credit, "D" for debit) with conditional field semantics—architects must ensure downstream systems handle context-dependent field interpretation

- **Integration dependency**: Form 6195 is the authoritative specification for Interac e-Transfer reconciliation flows; any custom reconciliation logic or file parsers must reference this updated documentation to correctly interpret records 7-14

- **Backward compatibility**: No file format changes means existing parsers remain compatible, but field interpretation logic must account for the clarified credit/debit distinctions to avoid reconciliation errors

- **Support contact**: Client Support Services (1-888-889-7878, Option 1) or support@central1.com for clarification on specific field requirements during design

- **Architect consideration**: When designing reconciliation or transaction processing systems, validate that field handling distinguishes transaction direction per the clarified specifications to prevent data mapping errors in downstream GL or reporting integrations