# Summary: PS 21:16 Release Notes – Outgoing Wire Request Form Updates

- **Release scope**: Nomenclature and regulatory update to Form 1171 (Outgoing Funds Transfer Request renamed to Outgoing Wire Request) effective June 2, 2021, aligning terminology with FINTRAC compliance requirements.

- **Terminology migration**: All system references require updates—"MTS" → "Wires", "funds transfers/transfer" → "wire(s)"—affecting downstream documentation, APIs, and user-facing labels across the Payment Solutions platform.

- **Data structure changes**: 
  - Mandatory field indicators (asterisks) added to Sender Information and Beneficiary Information sections in Form 1171
  - PEP (Politically Exposed Person) Declaration section text revised—validate schema against updated declaration logic

- **FINTRAC reporting integration dependency**: Additional Information for FINTRAC Reporting section now requires mandatory completion for all wires ≥$10,000 CAD equivalent sent outside Canada (regardless of source currency)—previously excluded CAD wires; this changes conditional logic in wire processing workflows.

- **Compliance constraint**: Architects must implement validation rules enforcing "reasonable effort" completion of FINTRAC Additional Information section for cross-border wires ≥$10,000 CAD equivalent; this affects transaction validation gates and error handling.

- **No new system integration points mentioned**: Updates appear localized to Form 1171 metadata and FINTRAC reporting module; verify backward compatibility for existing wire transmission workflows.