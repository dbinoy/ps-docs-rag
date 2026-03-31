# Release 22:18 (July 11, 2022) Summary

- **Purpose**: Documentation updates to ATM/POS services following network rebranding and content reorganization; primarily editorial changes with targeted functional updates

- **Network Rebranding & Service Changes**:
  - Canadian EXCHANGE → THE EXCHANGE; US EXCHANGE → Allpoint; Direct Cash Payments → Cardtronics
  - Removed references to deprecated CUETS and POS In-Branch services
  - Subscription services now available beyond BC/Ontario credit unions

- **Key Functional Updates**:
  - Fraud monitoring expanded to include CNP (Card Not Present) transaction types
  - Record retention periods updated for ATM/POS transactions; all records now require 7-year retention mandate
  - Settlement cut-off times formalized across networks, with Allpoint specified at 5:59:59 pm PT/8:59:59 pm ET

- **Integration Dependencies**:
  - Central 1 Switching & Card Services provides governing rules and regulations
  - CCUA manages Route and Transit listings and operating policies
  - FINTRAC inquiries now require 5-business-day response SLA for Requests for Information on trace handling
  - ACCULINK and THE EXCHANGE linked for exception deposit notification workflows

- **Critical Architectural Considerations**:
  - Network rules governance delegated to individual networks (transaction allowance details moved out of manual)
  - Document distribution and trace request handling tightly coupled to issuer notification workflows
  - Login/procedural documentation removed; contact/resource information centralized in Section 1.6