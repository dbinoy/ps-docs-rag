# Data Hub Documentation Summary

- **Overview**: Data Hub is an interactive analytics platform (powered by Microsoft Power BI) that enables financial institutions to transform transaction data into actionable KPIs, usage patterns, and performance metrics without manual data sourcing or analysis.

- **Current Scope & Roadmap**: Payments Dashboard currently supports Interac e-Transfer® transactions only; wires and other payment types are planned for future releases, indicating a phased product expansion strategy.

- **Key Capability**: Multi-level filtering with dual output formats (charts and tables), plus peer benchmarking against anonymized financial institutions of similar size/product usage, and multi-format export functionality.

- **Data Refresh Cadence**: Daily refresh cycle on business days only; architects should account for T+1 latency when designing real-time or near-real-time dependent features.

- **Platform Dependency & Volatility Risk**: Built on Microsoft Power BI infrastructure, meaning UI/feature availability may diverge from documentation without notice—documentation may become stale, and Power BI updates could impact custom integrations or expected user workflows.

- **Access Model**: Always-available platform with no apparent usage throttling or session restrictions mentioned; no authentication model or role-based access control details provided on this page.

- **Support & Escalation**: Central 1 Client Support Services owns operational support (ServiceNow, email, phone); this is the single point of contact for setup, access issues, and system problems.