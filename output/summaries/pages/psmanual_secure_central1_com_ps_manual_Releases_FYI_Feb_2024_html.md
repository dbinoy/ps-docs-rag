# FYI – February 2024 Summary

- **Purpose**: February 2024 release notes documenting terminology updates and functional enhancements across the Payment Solutions Manual's six primary volumes (AFT, Bill Payments, Central 1 Banking Services, Clearing and Deposits, Currency, and Document Library).

- **Nomenclature Migration**: Systematic replacement of legacy "CBS" and "CBS Online" terminology with "CAS" (Current Account Services) and "CAS Online" across multiple volumes—indicates backend system rebranding or consolidation with potential API endpoint and authentication schema changes for integrations.

- **Corporate Capture Enhancement**: Form 8996 enrollment instructions added to Deposit Processing (Section 9.3)—architects must understand the corporate capture data flow and Form 8996 schema requirements for client onboarding integrations.

- **FX Shipping Constraint Change**: Priority shipping deprecated; all foreign currency orders and drafts now limited to overnight delivery only—affects SLA contracts, fulfillment orchestration, and client communication workflows for FX transaction processing.

- **EBC Return Notification Dependency**: Electronic Banking Channel (EBC) now provides transaction details via email post-return request (Section 10.2, FX Notes Plus)—introduces asynchronous email notification dependency and potential need for webhook/notification service integration.

- **Document Revision Impact**: Three critical documents revised (CBS Online User Request 2513, Central 1 Account Request 3571, Treasury Services Treasury Report Guide 6158)—architects should validate these documents for schema/process changes affecting account provisioning, reporting, and integration workflows.

- **Contact Point**: Support escalation via Client Support Services (1-888-889-7878, Option 1 or support@central1.com)—useful for clarifying migration timelines and backward compatibility windows during design.