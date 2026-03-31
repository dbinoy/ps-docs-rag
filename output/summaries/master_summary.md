# Payment Solutions Master Architecture Guide

## 1. System Overview

Central 1's Payment Solutions platform is a multi-domain financial transaction processing system serving member institutions across Canada. It integrates discrete but interconnected operational domains—Automated Funds Transfer (AFT), bill payments, cheque clearing/deposits, and banking services—into a unified ecosystem with shared settlement, security, and data management infrastructure. The platform handles origination, transmission, clearing, settlement, exception management, and regulatory compliance across payment types, with emphasis on audit trails, multi-currency support, and role-based access control.

---

## 2. Domain Map

| Section | Coverage | Key Responsibility |
|---------|----------|-------------------|
| **Root / Access & Admin** | Authentication, RBAC, 2-Step Security, file exchange, user lifecycle | Security model and administrative governance |
| **AFT** | Automated Funds Transfer origination, settlement, returns, exceptions | Direct bank-to-bank payment processing (PaymentStream and batch channels) |
| **Bill Payments** | EBPS, BPRP, CRA Business Taxes, Online Tracing System (OLT) | Non-AFT payment routing, remittance processing, trace resolution |
| **Clearing & Deposits** | Cheque/instrument capture, MICR imaging, dishonour processing, incoming clearing | Physical/digital instrument processing and returns management |
| **Central 1 Banking Services** | AgriInvest, CEBA, CAS Online, account reconciliation | Operational/settlement accounts and government program administration |

---

## 3. Core Flows

### **Flow 1: AFT Origination → Settlement**
```
User Input (PaymentStream portal or file upload)
  → Payor/Payee validation
  → Approval workflow (if PaymentStream)
  → File assembly & cutoff enforcement
  → Transmission via AFT gateway
  → Receiving bank posting
  → Settlement posting (originator + receivee + service charges)
  → Exception capture (rejects/returns/recalls)
```
**Critical Points**: Strict AFT deadline enforcement; parallel outgoing/incoming posting; returns trigger exception workflows with defined recourse periods (Payments Canada regulated).

### **Flow 2: Bill Payment Submission → Trace Resolution**
```
EBPS file submission (file or eCommSwitch direct)
  → Payee routing
  → Asynchronous settlement confirmation
  → Discrepancy detection
  → Trace request creation (OLT)
  → Manual investigation & resolution (5–10 business days typical)
  → Settlement adjustment
```
**Critical Points**: Eventual consistency model; no real-time confirmation guarantee; OLT is manual bottleneck; CRA payments follow separate compliance workflows.

### **Flow 3: Deposit Capture → Clearing → Return Processing**
```
Branch/Corporate/Mobile capture
  → Image scanning & MICR validation
  → Acceptability checks
  → Clearing submission
  → Settlement posting
  → (If returned) → ORS entry → reason coding → reimbursement tracking
```
**Critical Points**: Imaging mandatory for statement delivery; dishonour handling via Online Return System; foreign exchange drafts and specialty deposits have distinct ordering/policy cycles.

### **Flow 4: Exception & Trace Management**
```
AFT returns/rejects/recalls OR Bill payment discrepancies OR Deposit dishonours
  → Exception queue entry
  → Reason coding & routing
  → Escalation (rejects non-postable; returns have recourse windows; recalls reversible)
  → Trace request (OLT) or direct reinstatement
  → Settlement adjustment
```
**Critical Points**: Three AFT exception types (rejects/recalls/returns) each with distinct SLAs; OLT is transaction-level investigation platform; BC-only features require conditional logic.

### **Flow 5: User Access & File Exchange**
```
Security Officer policy definition (CPS Admin)
  → User registration & permission assignment (User Management)
  → (2-Step Security token enrollment if required)
  → Portal access (Client Centre) or SFTP file exchange
  → Role-based folder visibility & file spec validation
```
**Critical Points**: Cascading permission inheritance; token lifecycle critical (hard token shortages cause onboarding delays); file specs tightly coupled to clearing operations.

---

## 4. Key Integration Points

**External Systems:**
- **Clearing Networks** — Payment Canada infrastructure for cheque/AFT/bill payment clearing
- **eCommSwitch** — Direct connection protocol for bill payments (alternative to file submission)
- **ServiceNow** — CEBA loan administration, manual return/reimbursement request tracking
- **CAS Online** — Web portal for account management and reporting
- **CPS Admin / User Management** — Separate administrative consoles for policy and access control

**Protocols & Standards:**
- **SFTP** — Machine-to-machine file exchange with registered credentials
- **MICR validation** — Cheque/instrument reading standard
- **File specifications** — Central 1 proprietary formats for EBPS, AFT, deposit, and return submissions (tightly coupled to downstream processing)

**Data Flow Hubs:**
- **Data Hub** — Centralized transaction persistence and analytics query layer
- **Document Library** — Artifact storage for compliance and audit trails
- **Settlement/GL** — Financial posting and reconciliation engine

---

## 5. Critical Design Constraints

| Constraint | Implication |
|-----------|------------|
| **Strict Cutoff Windows** | AFT entry limits and deadlines are non-negotiable; batch processing must enforce pre-deadline submission and reject post-cutoff requests. |
| **Eventual Consistency** | Bill payments and traces operate asynchronously; real-time confirmation is impossible. Design with reconciliation workflows, not real-time guarantees. |
| **Regulatory Compliance** | PAD processing, recourse periods, dishonour handling, and CRA workflows carry legal obligations. Changes require compliance review before deployment. |
| **Dual-Channel Complexity** | AFT has PaymentStream (interactive) and File Transmission (batch) with distinct approval models and deadlines. Feature logic must account for both. |
| **Data Retention Cycles** | PaymentStream AFT has documented purge schedules; historical queries must plan for archival. Verify audit trail requirements early. |
| **BC-Only Features** | Some AFT contingency procedures and Batch Return Service apply only to BC channel; use conditional feature flags. |
| **Token Dependency**