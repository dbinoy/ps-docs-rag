# Business Continuity Program Summary

- **Purpose**: Documents Central 1's comprehensive Business Continuity Program (BCP) framework addressing system, site, and regional disaster recovery with four primary operational plans (CMC, IRP, TRP, PRP).

- **Service Classification System**: Four service tiers with defined Recovery Time Objectives (RTOs) determine disaster response:
  - Mission Critical (0–4 hrs): Auto-failover via DNS load balancing; minimal manual intervention
  - Business Critical (15 min–48 hrs): Manual intervention required
  - Business Important (4 hrs–30 days): Manual intervention required
  - Business Supporting (48 hrs–30+ days): Requires system recreation from backup

- **Dual Data Center Architecture**: Active/passive deployment across Vancouver and Toronto data centers with redundant internet connectivity, UPS, and generators; single point of failure if both centers fail simultaneously (documented as never occurred).

- **Critical Integration Dependencies**: Clients must maintain direct connections to *both* data centers to enable automatic failover; DNS-based load balancing and client browser settings are load distribution mechanisms.

- **Communication Flow During Disasters**: Central 1 switchboard (1-800-661-6813) remains active via out-of-region virtual switch; status updates to clients occur within 48 hours post-declaration via ServiceNow, phone (1-888-889-7878), or email (support@central1.com).

- **Auxiliary Recovery Resources**: Mobile backup trailer deployment within 48 hours provides satellite-based voice/data connectivity and operational facilities; used only after primary recovery attempts.

- **Service Degradation Pattern**: Non-critical operational services (Change Requests, administrative functions) degrade during disasters until alternative staffing arrangements are made; core transaction processing prioritized.

- **Architect Constraint**: Design must assume RTO variance based on disaster magnitude and staff availability; cannot guarantee deterministic recovery windows within stated ranges.