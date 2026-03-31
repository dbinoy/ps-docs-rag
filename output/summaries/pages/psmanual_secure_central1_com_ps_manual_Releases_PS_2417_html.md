# Release 24:17 Summary – AFT Clearing File Specification Updates

- **Scope**: Clarification and standardization of AFT (Automated Funds Transfer) clearing and returning clearing file format specifications for CAD and USD across regional variants (BC/Atlantic vs. all other regions) to resolve submission discrepancies.

- **Key Data Structure Changes**:
  - **"A" Record**: Creation number field capped at 4 numeric digits; Credit Union data element constraints now province and client-type dependent
  - **"C", "D", "E", "F" Records** (clearing): Account data must be numeric with flexible leading zero handling (removable or padded to 9/12 digits); Institution Account No. for Returns now accepts alphanumeric with no padding requirement
  - **"I", "J" Records** (returns): Original Account No. now alphanumeric without padding constraints; Amount field must be right-justified with leading zeros across all regions except BC/Atlantic

- **Regional Format Divergence**: BC/Atlantic specifications (docs 6269, 6270) allow more flexible numeric/alphanumeric handling; all other regions (docs 9083–9086) enforce stricter numeric-only requirements for account and payee fields with mandatory right-justified amounts.

- **Critical Constraint**: Inconsistent leading zero treatment between regions—BC/Atlantic permits removal/padding flexibility while non-BC/Atlantic regions mandate numeric format only; architects must route validation logic based on regional origination.

- **Integration Dependencies**: Changes affect downstream clearing house processing and return file reconciliation; clients submitting multi-currency or multi-region transfers must implement conditional formatting logic in payment file generation middleware.

- **Documentation Dependencies**: Four specification documents (6269, 6270, 9083–9086) updated with new file format examples; example section updates suggest validation test suites and mapping templates may require refresh.