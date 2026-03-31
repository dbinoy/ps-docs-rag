# Clearing and Deposits: Section Overview

## Purpose

This section provides comprehensive operational guidance for payment clearing and deposit processing within a financial cooperative environment. It covers the complete lifecycle of deposit items (cheques, money orders, drafts) from acceptance through settlement, including specialized services like imaging, returns processing, and foreign exchange instruments. The documentation addresses both branch-level capture operations and corporate-scale transaction management.

## Key Concepts

1. **Deposit Capture & Processing**: Multi-channel acceptance and digitization of payment instruments via Branch Capture, Corporate Capture, and Mobile Deposits, with image-based clearing workflows.

2. **Cheque Imaging & MICR**: Magnetic Ink Character Recognition (MICR) validation and image file management for statement delivery and legal compliance, enabling paperless clearing.

3. **Dishonour & Returns Management**: Systematic handling of failed/returned items through the Online Return System (ORS), including reason coding, reimbursement tracking, and contingency procedures.

4. **Instrument Types**: Canadian dollar money orders, FX drafts, and specialty deposits (ICBC agent deposits in BC) with distinct policy, ordering, and settlement workflows.

5. **Incoming Clearing**: Inbound items received from other institutions, requiring parallel processing, tracing, and settlement mechanics separate from outbound deposits.

## How It Works

**Outbound Flow**: Items deposit → capture/scanning → validation (MICR, acceptability checks) → approval/transmission → clearing system submission → settlement/adjustment.

**Inbound Flow**: Incoming clearing items → processing/posting → tracing capability → settlement.

**Exception Handling**: Dishonoured items → ORS return entry → reason coding → reimbursement request → settlement adjustment.

**Specialized Services**: Money order and FX draft management includes inventory control, policy enforcement, voiding/refunding procedures, and reconciliation tracking.

## Integration Points

- **Scanner Infrastructure**: Branch Capture and Corporate Capture procurement, testing, maintenance, and user access management
- **Clearing Systems**: External clearing networks for item submission and return processing
- **Online Return System (ORS)**: Centralized platform for cheque/AFT returns, research, reinstatement, and batch file uploads
- **Settlement/GL**: Deposit settlement adjustments and financial statement posting
- **Member Statements**: Cheque image delivery and archival integration
- **ServiceNow**: Manual return and reimbursement request tracking

## Architect Notes

**Constraints & Gotchas**:
- **Legal/Regulatory**: Cheque imaging compliance, dishonour notice timing, and instrument-specific regulations require policy configuration before operational deployment
- **Image Lifecycle**: MICR testing, image file formats, and member statement delivery are tightly coupled; changes impact multiple downstream systems
- **Contingency Criticality**: Documented fallback procedures for ORS outages and scanner failures are operational requirements, not optional features
- **Aged Deposit Management**: Branches can accumulate old unresolved deposits; design should include visibility/escalation mechanisms
- **Multi-Instrument Complexity**: Money orders, FX drafts, and ICBC deposits introduce separate policy trees, stock management, and settlement logic—avoid monolithic deposit processing models
- **Error Taxonomy**: Rich appendices (reason codes, error messages, transaction codes) indicate high transaction complexity; validation rules must be comprehensive
- **Tracing & Research**: Deposit research and tracing capabilities are critical for dispute resolution; ensure audit trail completeness in any redesign