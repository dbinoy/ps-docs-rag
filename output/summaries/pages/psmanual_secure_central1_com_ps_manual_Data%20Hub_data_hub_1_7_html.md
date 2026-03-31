# Payments Dashboard Documentation Summary

- **Overview**: The Payments Dashboard is a multi-tenant analytics portal enabling authorized users to filter, visualize, and export Interac e-Transfer transaction data with peer benchmarking capabilities; currently supports up to 2 years of historical transaction data provided by Central 1.

- **Core Data Model**: Dashboard aggregates transactions across four dimensions—Transaction Type (EMT Receive/Send, MR Fulfill/Send), Feature (Account Number Routed, Auto Deposit, Money Request, Regular Q&A, Unknown), Originating Channel (External API, MD Desktop/Mobile Web, Mobile App, Unattended, Version Agnostic API), and Brand Name—with three measurement types (Transaction Volume, Total Payment Amount, Average Payment Amount).

- **Filter Architecture**: Dual-level filtering system where left-hand Filters menu applies globally across all visuals, while visual-specific drop-down menus (Breakdown, Bin Size, Time Period) affect only their respective chart; Date Filters support both pre-defined periods and custom date range selection via calendar or slider interface.

- **Data Visualization Engine**: Powered by Microsoft Power BI; seven default chart visuals with toggle capability to render as tables; supports standard Power BI operations (sharing, alerting, comments, data export, sorting) with custom features including cohort comparison against anonymized peer institutions and transaction distribution analysis in configurable increment ranges ($10–$100+).

- **Key Integration Dependency**: Relies on Central 1 as the authoritative transaction data provider; financial institutions with multiple brands access brand-filtered data views, implying multi-tenant data isolation requirements at the source system level.

- **Critical Architectural Constraint**: Interac e-Transfer is currently the only supported product type; any product expansion requires schema modifications across all seven visuals and filter definitions, suggesting product type as a foundational data partition key.

- **Alerting & Monitoring Capability**: Native alert system allows users to configure notifications on trend changes and conditions; alerts are visual-level abstractions likely backed by Power BI's scheduling/notification service, requiring consideration for notification delivery SLAs and alert rule storage/management.