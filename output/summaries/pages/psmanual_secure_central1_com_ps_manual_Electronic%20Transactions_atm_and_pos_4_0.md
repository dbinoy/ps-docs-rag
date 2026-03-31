# Summary: ATM and POS Trace Request Management

- **Purpose**: Defines procedures for initiating and managing trace requests for ATM and POS transactions, with routing logic dependent on network (THE EXCHANGE vs. others) and switch provider (Cardtronics vs. Everlink).

- **Routing Logic**: Traces on THE EXCHANGE network bypass Central 1 (direct acquirer-issuer handling); non-EXCHANGE transactions route to Cardtronics directly or to ServiceNow for Everlink, where Central 1 acts as intermediary forwarder.

- **Primary Integration Point**: ServiceNow Service Catalogue (https://clients.central1.com) is the operational system of record for Everlink-based trace submissions; manual Form 2465 is fallback-only when ServiceNow is unavailable.

- **Data Elements**: Both ATM and POS trace requests capture PAN, transaction date/time, trace/reference/sequence number, amount, ATM ID or Terminal ID, service provider selection, reason code, and switching report attachment—with "Other" reason requiring narrative explanation in Additional Information field.

- **Response SLAs**: ATM traces require 10 business day response; POS traces require 30 calendar day response per Interac regulations; overdue requests escalate through existing ServiceNow tickets to Central 1 management.

- **Scope Constraints**: Interac exempts customer-initiated POS traces under $20.00 unless duplicate; POS trace submission requires specific conditions (multiple postings, declined-but-posted, no cardholder record) before Central 1 forwards to acquiring institution for adjustment processing.

- **Dispute Escalation**: Unresolved disputes reference external operating rules (Canadian Exchange, ACCULINK, Cirrus, Visa, Interac) with tiered escalation paths (Level 1-3 support) varying by network participant type and codes (EXC/ACCULINK/INT/PLS/CIR).