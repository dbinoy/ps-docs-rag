# Electronic Transactions Section Overview

## Purpose

This 89-page section documents Central 1's payment processing infrastructure, covering card-present (ATM/POS), card-absent (e-Transfer, International Transfers, Wires), and administrative fraud management systems. It provides operational and technical guidance for settlement, reconciliation, tracing, reversals, and fraud incident management across multiple payment rail networks.

## Key Concepts

1. **Settlement & Reconciliation** — Atomic posting of transaction batches with asynchronous trace/adjustment workflows to resolve discrepancies between acquirer/issuer perspectives
2. **Trace & Adjustment** — Formal dispute resolution mechanism initiated by either party; includes evidence collection, remediation procedures, and response code mapping
3. **Multi-Rail Architecture** — Parallel processing of Interac (domestic), international SWIFT/SWIFT gpi, and proprietary wires with distinct policy, regulatory, and technical requirements per rail
4. **Enterprise Fraud Management (EFM)** — Centralized incident triage system with configurable alerts, filters, and team workflows; sits upstream of settlement to flag suspicious transactions
5. **User Roles & Access Control** — Role-based administration (MTS administrators, fraud analysts, wire originators/approvers) with branch-level segmentation and audit trails

## How It Works

**Transaction lifecycle:**
1. Real-time authorization (card/e-Transfer/wire submission) → fraud pre-screening
2. Batch settlement at T+0 or T+1 depending on rail and processing model
3. Reconciliation against internal GL and counterparty reporting
4. Exception handling: EFM incident creation → investigation → trace initiation or reversal request → counterparty response → adjustment posting

**Key data flows:**
- Inbound: customer transactions, counterparty settlement files, response codes, trace replies
- Outbound: batch settlement submissions, trace requests, amendment notifications, fraud alerts

## Integration Points

- **Upstream:** Customer-facing channels (PaymentStream Direct, OAS, MemberDirect Business), acquiring networks, issuing banks
- **Downstream:** General ledger, nostro/vostro accounts, regulatory reporting (AML/CFT), payment networks (Interac, SWIFT, domestic clearinghouses)
- **Lateral:** EFM links to all transaction types; OAS provides Interac e-Transfer–specific tracing and misdirected funds recovery

## Architect Notes

**Constraints & Gotchas:**
- **Asynchronous settlement windows** vary by rail (ATM/POS batched hourly; international wires T+0 to T+2 depending on destination); design systems to tolerate delayed reconciliation
- **Multi-party accountability** — trace workflows require coordination; ensure audit trails track who initiated, who responded, and remediation ownership
- **Response code fragmentation** — each rail (Interac, SWIFT, domestic) has distinct codes; mapping and translation layers essential
- **Fraud hold procedures** — EFM can suspend transactions before settlement; implement compensating controls (manual override workflows, escalation paths)
- **Regulatory/compliance overlay** — international transfers subject to sanctions screening, AML holds, and SWIFT gpi transparency; bake into design from schema to API contract

**Design implications:**
- Event-driven architecture preferred for async settlements and trace state machines
- Immutable audit logs mandatory for regulatory defensibility
- Schema versioning critical across multiple clearinghouses and their evolving message formats