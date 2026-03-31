# Payment Solutions 24:07 Release Summary

- **Purpose**: Documentation updates to bond redemption and transfer procedures in the Clearing and Deposits Volume, effective February 9, 2024.

- **Redemption Policy Change (CSB bonds)**: Shifted from internal value tables to Bank of Canada Unclaimed Properties Office online tool as primary source for redemption values; fallback to value tables when tool unavailable—requires API integration or manual lookup workflow design.

- **External Dependency**: Bank of Canada Unclaimed Properties Office website is now critical integration point for redemption rate determination (Sections 5.2, 6.1); architects must account for tool availability, response times, and error handling.

- **Deposit Segregation Requirement**: Canada Savings Bonds and Ontario Savings Bonds must be processed in separate Canadian deposits when prepared for Central 1—impacts deposit batching logic and validation rules.

- **Physical Transport Constraint**: Central 1 no longer accepts registered mail; signature-required shipping services required—affects document/instrument handling workflows and potentially requires carrier API integration.

- **Entity-Specific Guarantee Procedures**: New procedures added for bonds registered to companies or charitable organizations requiring signature guarantee—introduces entity type classification into ownership transfer data model.

- **Form and Reference Updates**: Multiple form references changed (Transfer of Ownership, Change of Address, Estate Transfer) and Canada Savings Bonds Program website references migrated to Bank of Canada Unclaimed Properties Office—requires documentation URL management and potential form versioning considerations.