# Summary: Troubleshooting Tracing Requests for Interac e-Transfer

**Overview:** Diagnostic guide for resolving customer inability to send/receive Interac e-Transfer transactions through the OAS (Online Administration System), with focus on account states, service availability, and transaction status tracking.

**Key Concepts & Rules:**
- **Account eligibility gates:** Customer profile status (Disabled flag), email scrubbing (Scrubbed Email list), and notification channel blocking (Fraud Analyst-maintained lists) prevent transaction initiation
- **Transfer limits enforcement:** Per-transaction maximums and rolling limits (1/7/30-day windows calculated to the minute) apply to outgoing transfers only; global $25,000 hard cap on incoming transfers set by Interac (not visible in OAS)
- **Open transfer exclusivity:** Only one active transfer can exist between sender-recipient pair at a time
- **Transfer lifecycle states:** Open, Completed, Blocked (by Interac or Fraud Analyst), Cancelled (by Fraud Analyst), Interrupted (inconsistent state from comms breakdown/timeout/abandonment), Failed (post-settlement review via ECCX reports)

**Data Structures & Search Integration:**
- OAS Customer Details page houses: Disabled indicator, Profile Summary tab (Scrubbed Email field + Revoke option, transfer limits), Transfer History with memo field for fraud analyst annotations
- Transfer Details page tracks: blocked status, cancellation records, Transfer History audit trail
- ECCX Failed Transactions report (daily cadence) uses two search keys: `Interac Ref No` (case-sensitive, no wildcards, search category: "Interac Payment Reference") and `C1 Retrieval Reference No` (case-insensitive, wildcard-compatible, search category: "FI Reference Number")

**Critical Dependencies & Integration Points:**
- **Interac Services health check:** Heartbeat signal on Transfer Parameters tab indicates service availability; maintenance windows block all transactions
- **Central 1 backend:** Manages interrupted transfer remediation (automated cleanup, rollback/completion decisions post-investigation); handles misdirected funds recovery requests via OAS Misdirected Funds Recovery tab
- **Banking host integration:** Interrupted transfers arise from banking host comms failures; manual account adjustments required when transactions show Completed in OAS but failed on bank settlement side

**Architectural Constraints for Enhancement:**
- Scrubbed email blocking applies retroactively to pending transfers sent *before* scrubbing occurred
- Rolling limit calculations are precise to the minute; architectural designs must support sub-minute granularity in windowing logic
- Interac blocked lists (email/phone) are opaque