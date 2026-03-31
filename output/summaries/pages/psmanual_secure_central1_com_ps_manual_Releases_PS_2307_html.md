# Release 23:07 (April 19, 2023) — AFT & Cheque Clearing File Specifications Update

- **Scope**: Updates to five clearing file specifications for Automated Funds Transfer (AFT) and cheque processing, affecting CAD/USD currencies across Canadian regions (excluding BC and Atlantic)

- **Currency Code Changes**: "A" Records across all four AFT specifications now explicitly document that Currency Code Identifier contains spaces or the ISO currency codes ("CAD" or "USD"), indicating stricter validation or documentation requirements

- **Settlement Code Standardization**: "E", "F", "I", "J" Records across AFT and AFT Return specifications changed Originator Direct Clearer Settlement Code description to "Indicates N", suggesting a constraint on valid values or a behavioral change in settlement routing logic

- **Data Element Removals**: 
  - All four AFT specifications: "Z" Record Data Element 12 removed
  - DCPA/QCPA Cheque specifications: "A" Record elements 07-08 and "Z" Record elements 06-08 removed (payload structure compression)

- **Transaction Type Differentiation**: DCPA/QCPA now distinguishes CAD (150) from USD (160) in "B" Record Transaction Type field, enabling currency-specific processing rules downstream

- **Integration Impact**: File format changes likely affect validation logic, parser configurations, and downstream clearing house integrations; architects must update schema definitions and integrate change notifications to dependent systems

- **Support & Governance**: Changes governed by Client Support Services; engineers should reference document IDs (9083-9086, 9528) when implementing parser/validator updates