# Summary: FX Drafts Policy Establishment

- **Purpose**: Defines mandatory and recommended policies for financial institutions issuing Foreign Exchange (FX) Drafts, covering compliance, risk management, and system access controls.

- **Regulatory Compliance Requirements**: Institutions must establish staff training policies for PCMLTFA (Proceeds of Crime Money Laundering and Terrorist Financing Act) and PCMLTF Regulations; non-compliance requires escalation to AML Compliance Officer or FINTRAC.

- **Non-Member Transaction Data Capture**: For FX drafts ≥$3,000 CAD equivalent to non-members, institutions must record and maintain: individual identity, name, address, transaction date, amount received, payment instrument type (cash/cheque/traveler's cheque/money order), and issuer identification; aggregation rule applies to multiple drafts totaling ≥$3,000 CAD on same transaction.

- **Convera Integration Constraints**: External payment processor (Convera) enforces blocking rules requiring downstream compliance validation before draft honoring; drafts cannot be negotiated until Convera releases clearance message; system prevents: multiple sub-$10,000 USD drafts per beneficiary/day, money service business issuance, and financial institution beneficiaries.

- **Access Control Model**: User management is institution-defined; requires unique user IDs per employee, no ID sharing, secure password delivery via Client Centre, and annual inactive user purging (≥1 year inactivity triggers deletion).

- **Architecture Dependencies**: FX Drafts integrates with Central 1's Client Centre authentication layer (password-based SSO); links to Operations Manual Program and User Management modules; reporting obligations tie to FINTRAC reporting workflows (Suspicious Transaction Reports).

- **Risk Governance**: Institutions may implement stricter policies than minimums (e.g., blanket identity verification for all non-members regardless of amount), establishing policy-as-code enforcement points in transaction processing.