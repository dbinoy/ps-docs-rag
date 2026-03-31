# FX Notes Settlement and Trace Request - Architecture Summary

- **Purpose**: Defines settlement mechanics, posting procedures, and reconciliation workflows for FX Notes transactions across BC/Ontario member institutions and non-member financial institutions via AFT channels.

- **Settlement Architecture**: Net settlement model posts to financial institution Canadian dollar current accounts using transaction code **FC** (wholesale value inclusive of fees); amount can be credit or debit; posted next business day after Globex 2000 settlement file receipt by Central 1.

- **Posting Routing**: Member institutions receive postings by branch or designated transit number (e.g., head office) to Canadian dollar current accounts; non-members receive settlements via AFT with expected processing within two business days of Globex delivery.

- **External System Dependencies**: Globex 2000 (settlement file source), Central 1 Banking System (Current Account Services for viewing postings), File and Report Exchange (AIBC/AIOC report distribution for BC/Ontario respectively).

- **Key Data Fields & Codes**: Transaction code **FC** (identifies FX Notes postings), wholesale value (settlement basis, excludes institution spread/fees), AIBC (BC) and AIOC (Ontario) account activity reports; non-members reference Provincial Central reports.

- **Reconciliation Integration**: Profitability report (Manager/Auditor roles only) displays revenue by transaction with wholesale and customer details; reconciles against AIBC/AIOC reports (member institutions) or Provincial Central reports (non-members) using FC transaction code filtering.

- **Operational Constraint**: Non-business-day transactions (e.g., Saturday) delay processing to next business day; settlement posting lag is minimum one business day from file receipt.