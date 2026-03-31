# Currency Section Overview

## Purpose

This 28-page section documents the end-to-end currency management and foreign exchange capabilities of the Payment Solutions platform. It covers two primary domains: (1) **Cash Services** — the ordering, settlement, and management of domestic (Canadian/US) and foreign currency physical inventory, and (2) **FX Notes** — a foreign exchange transaction system enabling buying and selling of foreign currency to/from customers with real-time pricing and settlement.

## Key Concepts

1. **Cash Services Ordering Model**: A policy-driven workflow for requesting physical currency with support for standard orders, standing orders (recurring), late orders (expedited), and contingency orders (backup supply). Orders flow through ServiceNow with cash location/limit controls and approval gates.

2. **FX Notes Transaction System**: A customer-facing foreign exchange platform supporting buy and sell transactions with real-time spreads, transaction fees, and multi-currency support. Transactions generate settlement and trace requests.

3. **Cash Location Management**: ServiceNow-based configuration of branch/location-level cash positions, inventory limits, and ordering authority — fundamental to policy enforcement and audit.

4. **Settlement & Reporting**: Downstream financial reconciliation, charge application, and trace request handling for both cash orders and FX transactions. Critical for accounting and regulatory compliance.

5. **User Role Hierarchy**: Distinct permission models for Cash Services (ordering, approvals, reporting) and FX Notes (transaction execution, pricing management, branch administration).

## How It Works

**Cash Services**: Policy definition → ServiceNow location/limit setup → user role assignment → currency order creation (with order type selection) → approval workflow → reporting/settlement.

**FX Notes**: Policy & fee structure setup → user authentication → spread/fee configuration per currency pair → real-time customer transaction (buy or sell) → transaction logging with images/shipment tracking → settlement and trace reporting.

## Integration Points

- **ServiceNow**: Cash location hierarchy, policy enforcement, order management, user access controls
- **Reporting/Analytics**: Settlement reconciliation, trace request management, audit trails
- **Customer-facing systems**: FX Notes transaction interface for retail/commercial customers
- **Pricing/Risk**: Real-time FX spread calculation; fee configuration per transaction type

## Architect Notes

- **Regulatory complexity**: Foreign currency handling involves legal/compliance considerations (page 1.03) — validate requirements before architectural decisions
- **Dual system design**: Cash Services and FX Notes operate independently; clarify integration scope if unified reporting is required
- **ServiceNow dependency**: Cash Services heavily relies on ServiceNow for authorization; architectural changes must account for policy sync and latency
- **Real-time pricing**: FX Notes requires live spread/fee management; ensure system supports dynamic configuration without transaction delays
- **Audit/settlement lag**: Both systems generate settlement and trace requests as asynchronous processes — plan for eventual consistency patterns
- **Multi-currency scope**: FX Notes supports multiple currency pairs; ensure data model accommodates new currency additions without schema changes