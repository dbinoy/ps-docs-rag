# Summary: 6 Posting AFT Service Charges

**Overview:** This page defines the process for posting three types of AFT charges—transaction fees, service fees, and setup fees—to financial institutions' Central 1 accounts and downstream to originators.

**Key Concepts & Charge Types:**
- **Outgoing Transaction Charges** (code OF): Posted monthly to Central 1 account; FIs manually post to originator accounts using transaction counts from ICCB/UCCB or ICTV/UCTV reports
- **Incoming Transaction Charges** (code DD for credits, code PP for debits): Posted to Central 1 monthly; FIs decide whether to pass through to members (e.g., bundled in account fees)
- **AFT Service Fees**: Monthly fee model (automatic file release on PaymentStream AFT) vs. per-file charge model (manual uploads or File and Report Exchange); one-time setup fee per new originator

**Critical Data Structures & Report Dependencies:**
- Four primary reports drive billing: AFT Monthly Fee Report (AFTM/UFTM), AFT Clients File Fee Monthly Summary (AFMS/UFMS), AFT Clients Daily Charges Report (AFTD/UFTD), Monthly Customer AFT Billing Report (ICCB/UCCB), and Monthly AFT Transaction Volumes Report (ICTV/UCTV)
- Reports sorted by branch; fee assignments keyed to Originator ID
- Charge codes (OF, DD, PP) used for Central 1 posting and reconciliation

**Integration Points & Manual Process Risk:**
- Central 1 account posting is automated, but originator-level billing requires **manual posting** by FI staff using report data—no downstream integration specified
- Regulatory constraint: Class A credit unions in BC/Ontario reference Form 2725 (Payment Services Class A Fee Schedule) for permissible charges
- PaymentStream AFT platform is the primary system generating billable events (automatic vs. manual file handling)

**Architect Must Know:**
- This is a **manually-intensive billing process**—reports provide data but posting to originator accounts is not automated; consider this a design gap if modernizing
- Fee recovery strategy is FI-discretionary (pass-through or absorb); no validation rules defined to prevent FI-originator charge disputes
- No mention of reconciliation mechanisms, rejected transaction handling, or audit logging for manual posts