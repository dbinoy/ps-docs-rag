# Summary: AFT Terminology & Definitions

**Overview:** Defines core terminology and concepts for Central 1's Automated Funds Transfer (AFT) system, covering transaction types, processing infrastructure, and key operational parameters.

## Key Concepts & Processes

- **Transaction Types:** AFT encompasses two primary flows—debit transactions (Pre-Authorized Debits/PADs) and credit transactions (Direct Deposits)—both governed by CPA Standard 005 and Rule H1
- **Processing Model:** Central 1 operates as originating direct clearer for BC/Ontario institutions; processing occurs in daily runs (up to 4 runs/day for CAD in BC, 3 in Ontario; 1 run/day for USD in both regions)
- **Lead Time Constraint:** AFT files must arrive 2 business days before due date (shorter lead times possible with Serviceability Code '0'), creating a hard dependency on submission timing
- **Offsetting Entry Mechanism:** System automatically posts offsetting debits/credits to originator accounts; must reconcile against individual transaction totals in outgoing files

## Data Structures & Field Dependencies

- **Financial Institutions File (FIF):** Payments Canada-maintained directory with serviceability codes indicating business days required to credit payee accounts—critical for SLA calculations
- **Serviceability Code:** Variable field on FIF determining credit availability timeline; affects lead time negotiation
- **Settlement Date:** Typically equals due date; posted to financial institution by Central 1

## Integration Points & Dependencies

- **File Exchange:** SFTP or Client Centre web portal for file transmission/receipt; connects to Payments Canada clearing infrastructure
- **Return Systems:** Online Return System (ORS) and Batch Return Service handle transaction reversals and Notice of Change creation
- **Multi-Currency Support:** USD AFT transactions require separate processing pipeline from CAD transactions

## Critical Architectural Considerations

- **Run-Based Processing:** System operates on scheduled batch runs, not real-time; design must accommodate discrete processing windows and downstream communication delays
- **Recall Constraints:** Only applicable pre-posting; debits recallable only if not yet sent to receiving institution's data centre—requires state tracking per transaction
- **Unpostable Transaction Handling:** System must support rejection paths for transactions that cannot be debited/credited; integration with ORS for exception management