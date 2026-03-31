# Payment Solutions Release Summary: 24:33 (September 11, 2024)

- **Scope**: Updates to Wires Data Extract Service File Specifications (Form 9327), Chapter 4 field definitions, with corresponding XML schema and sample file revisions.

- **System References Updated**: LVTS system code replaced with LYNX; NOS system added as new originating/receiving system option—verify downstream dependencies in wire routing and system integration layers.

- **Structural Additions**: Two new sections introduced (INSTRUCTING AGENT INFORMATION, SENDER CORRESPONDENT) and new fields added across multiple existing sections (e.g., Province/State, Postal/Zip, Relationship)—requires schema migration and backward compatibility consideration.

- **Field Length & Position Changes**: Widespread updates to field length constraints and positional ordering (Type field repositioned in ORDERING CUSTOMER, SENDING CUSTOMER, BENEFICIARY CUSTOMER, THIRD-PARTY SENDER)—impacts parsing logic, validation rules, and data mapping in integration code.

- **FINTRAC Reporting Expansion**: New regulatory fields added (Funded by Person or Entity?, Funding Method) and "Postal Code" standardized to "Postal/ZIP"—affects compliance reporting pipelines and KYC/AML data capture.

- **Content Column Refinements**: FI ID and Address labels updated (Address→Street); sample data added to BENEFICIARY CUSTOMER and ACCOUNT WITH INSTITUTION—indicates stricter content specification; validate against existing production data patterns.

- **XML/Schema Versioning**: Chapter 6 introduced as new XSD definition chapter; sample XML and report files updated—confirm version control strategy and API backward compatibility windows for consuming clients.