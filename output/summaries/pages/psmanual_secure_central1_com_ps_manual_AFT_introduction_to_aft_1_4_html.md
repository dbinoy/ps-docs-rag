# Summary: Establishing Policies for Originating AFT Transactions

- **Purpose**: Defines mandatory policies for financial institutions to establish before enabling business members to originate Automated Funds Transfer (AFT) transactions, with focus on regulatory compliance, risk mitigation, and internal controls.

- **Regulatory Compliance Requirements**: Financial institutions must implement policies for FINTRAC reporting—specifically Suspicious Transaction Reports and Terrorist Property Reports—covering AFT transactions of any amount at any stage (negotiation, approval, or post-cancellation/decline). References FINTRACâs Guidelines 2 and 3 as normative requirements.

- **PAD Agreement Framework**: Originators must use CPA Rule H1-compliant Payorâs PAD Agreements (Form 1696); financial institutions must audit business member compliance by sampling signed payor agreements annually. Related service agreements include Form 1904 (pre-authorized debits), Form 2007 (cash management PADs), and Form 2043 (direct deposits).

- **Risk Mitigation Controls**: Requires implementation of transaction/file limits (monitored by Central 1 based on FI asset size), confirmation emails, chargeback monitoring, frequency tracking, and collateral/line of credit requests. Specific risks flagged: overdrafts from offsetting entries, 90-day PAD return windows, unauthorized software access, and credential compromise exposing multiple Originator IDs.

- **User Access & Security Model**: Each user requires unique user ID + password (8+ characters, mixed case/numbers/symbols); third-party service providers maintaining multiple unaffiliated company Originator IDs must have separate user IDs per company to isolate damage. 2-Step Security tokens apply to business members on PaymentStream AFT. Central 1 auto-deletes inactive Originator IDs after 12 months.

- **PaymentStream AFT Integration Points**: File upload/release triggers confirmation emails; file limit exceptions require Central 1 review; transaction and file limits are enforced at system level. Platform manages business member and financial institution originator tracking with associated permission levels.

- **Staffing & Audit Requirements**: Financial institution staff must understand due diligence, credit approval, collateral assessment, and ongoing monitoring; internal controls require management reviews, internal audits of accessibility/activity, and documented procedures for secure credential delivery and access restriction.