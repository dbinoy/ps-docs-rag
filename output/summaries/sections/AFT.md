# AFT Section Overview

## Purpose

This 53-page section provides comprehensive documentation for Automated Funds Transfer (AFT) operations. It covers the complete lifecycle of AFT transactions—from enrollment and origination through settlement, returns, exception handling, and reporting. The documentation addresses both PaymentStream AFT (web-based interface) and File Transmission (BC) channels, establishing operational procedures, legal requirements, and system constraints.

## Key Concepts

1. **AFT Origination Methods**: Two primary channels—PaymentStream AFT (interactive web portal with approval workflows) and File Transmission Service (batch processing for BC). Each has distinct setup, processing, and release mechanisms.

2. **Payor-Payee Relationships**: AFT requires pre-established records mapping payment originators to recipients. PaymentStream AFT includes dedicated management interfaces; file transmission relies on batch record specifications.

3. **Exception Handling Taxonomy**: The system categorizes problems into rejects (unpostable transactions), recalls/error corrections, returns (downstream rejections), notices of change, and trace requests—each with distinct processing workflows and recourse periods.

4. **Settlement Mechanics**: Separate posting processes handle outgoing AFT files (originator's bank), incoming AFT files (receiving bank), and service charges. This enables balanced reconciliation across multi-party transactions.

5. **Regulatory Compliance Framework**: Business PADs, dishonoured transactions, and recourse periods are governed by legal considerations documented per section, suggesting payment regulation (likely Payments Canada standards).

## How It Works

AFT follows a three-phase model:

- **Origination**: Users enroll in the service, establish policies, and input transactions either via PaymentStream portal (with approval gates) or batch files (with validation and upload workflows).
- **Transmission & Processing**: Files move through AFT deadlines with record entry limits. The system validates against established payor/payee records and posting rules.
- **Settlement & Returns**: Outgoing/incoming files post to respective accounts; returns flow backward through designated exception handling, with dispute/trace mechanisms for unresolved items.

## Integration Points

- **Enrollment & Policy Management**: Links to account provisioning and user management systems
- **Payor/Payee Database**: Central repository for transaction validation
- **Approval Workflows**: Multi-user task approval for PaymentStream AFT transactions
- **File Transmission Gateway**: Batch upload/download interface for file-based channels
- **General Ledger/Settlement Posting**: Service charges and transaction settlement tie to accounting systems
- **Exception Management**: Rejects, returns, and recalls feed into dedicated exception queues with escalation paths
- **Reporting Layer**: AFT-specific reports generate from transaction lifecycle data

## Architect Notes

**Constraints & Gotchas:**

- **Dual-Channel Complexity**: PaymentStream and File Transmission have parallel but distinct workflows; integration logic must account for channel-specific deadlines and approval models.
- **Regulatory Sensitivity**: PAD processing, recourse periods, and dishonour handling carry legal implications. Changes to return/recall logic require compliance review.
- **Time-Bound Operations**: AFT deadlines and entry limits are strict; batch processing must enforce cutoff windows—no post-deadline transaction acceptance.
- **Data Purge Cycles**: PaymentStream AFT has documented data retention/purge schedules affecting audit trails and historical queries.
- **BC-Only Features**: Batch Return Service and some contingency procedures apply only to BC channel, requiring conditional feature logic.
- **Exception State Management**: Rejects, recalls, and returns create long-