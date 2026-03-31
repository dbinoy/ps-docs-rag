# Summary: Terminology and Frequently Asked Questions (AFT)

- **Purpose**: Defines 90+ core terms and concepts for the Automated Funds Transfer (AFT) system, establishing shared vocabulary for payment processing operations.

- **Core AFT Transaction Types**: 
  - **Debit**: Pre-authorized Debits (PADs) with three subtypes—Personal, Business, Cash Management, and Funds Transfer
  - **Credit**: Direct Deposits
  - **Administrative**: Error Corrections, File Error Corrections, Notice of Change (NOC), Recalls, and Resubmissions (return codes 901 NSF, 908 Funds Not Cleared)

- **Critical Identifiers & Data Structures**:
  - **Customer ID** / **Originator ID**: 10-digit Central 1 assigned identifier (unique per AFT file originator)
  - **Transit Number**: Composed of 3-digit Institution Number (CPA-assigned) + 5-digit Branch Number
  - **File Creation Number**: Auto-incremented sequential identifier; files must be received in order
  - **Due Date**: Payment posting date; Settlement Date typically equals Due Date

- **Lead Time & Processing Constraints**: Default 2 business day lead time before Due Date for file receipt at Central 1; shorter lead times possible with Serviceability Code "0"; stale-dated transactions capped at 173 days.

- **Key Integration Dependencies**:
  - **Financial Institutions File (FIF)**: Payments Canada-maintained directory; includes Serviceability Codes determining credit posting timelines
  - **CPA Standards**: AFT files exchanged per CPA Standard 005; PAD rules governed by CPA Rule H1
  - **File & Report Exchange**: SFTP or web-based upload/download portal; primary data exchange mechanism
  - **Online Return System (ORS)**: Web-based transaction returns and NOC creation

- **Security & Compliance Framework**:
  - **2-Step Security Token**: Hard Token or Soft Token (mobile app) required for Client Centre access
  - **CPS Admin roles**: CPS Admin Security Officers manage user lifecycle; Client Centre Users cannot manage other users
  - **Restricted Entities**: Defined exclusions (money transmitters, casinos, marijuana providers, virtual currency exchangers) requiring compliance controls

- **PAD Authorization Model**: Set Interval PADs require pre-notification once; Sporadic PADs require per-transaction authorization (non-waivable); Cash Management PADs enable inter-institutional fund transfers for same/affiliated businesses.