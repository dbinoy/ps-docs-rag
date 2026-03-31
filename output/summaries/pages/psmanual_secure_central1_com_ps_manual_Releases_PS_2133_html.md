# Payment Solutions Release 21:33 Summary

- **Subject**: Updated intermediary financial institution requirements for outgoing wire requests (Form 1171) effective September 17, 2021

- **Key Rule Change**: Canadian dollar (CAD) wires to the US now require explicit intermediary information obtained from the sender and recorded on Form 1171, then searched and selected in the Wires application (differs from prior practice)

- **Intermediary Selection Logic** (three distinct workflows):
  - CAD→US: Sender-specified intermediary (mandatory lookup/selection)
  - Non-domestic currency (e.g., EUR→UK): Select from system-suggested list with recommended default
  - Domestic currency (e.g., GBP→UK): No intermediary selection required; Central 1's correspondent bank handles routing

- **Data Structure**: Form 1171 captures intermediary bank details in the "Intermediary Financial Institution Information" section; this data flows into the Wires application for processing

- **Integration Point**: Form 1171 serves as the input document; intermediary data must be searchable/selectable within the Wires application, implying a lookup or validation mechanism against intermediary bank databases

- **Critical Constraint**: All international wires route through intermediaries that independently deduct fees; Central 1 cannot control or predict third-party fee deductions—this impacts customer fee transparency and reconciliation

- **Architectural Implication**: Wire creation workflow requires conditional logic based on currency pair and receiving country to determine intermediary handling; search/validation for CAD→US wires suggests dependency on an intermediary bank registry or reference data service