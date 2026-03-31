# Summary: Contingency Procedures for Stop Payment Requests and Desktop Draft Stock Orders

- **Purpose**: Defines fallback procedures when the FX Drafts system is unavailable for processing stop payment requests and managing desktop draft stock orders.

- **Primary System Dependency**: FX Drafts is the authoritative system for stop payment and draft stock order operations; no alternative processing path is documented within the system.

- **Failure Scenario & Escalation**: When FX Drafts becomes unavailable, users must contact Convera directly rather than implementing local workarounds—indicates Convera is the upstream provider/partner.

- **No Documented Queuing/Retry Mechanism**: The procedure lacks detail on message queuing, retry logic, or asynchronous reconciliation, suggesting manual intervention is required during outages.

- **Reference Dependency**: Exact contact information and escalation details are maintained in Section 1.3 (Contacts, Websites, and Other Resources)—architects should verify this section is current and accessible during system onboarding.

- **Architectural Gap**: The page provides minimal contingency detail (overview only, no procedures detailed); architects should clarify whether full contingency workflows exist elsewhere or need to be designed for future resilience.

- **Integration Point**: Convera relationship is critical for stop payment processing; architects should understand Convera's SLA, communication protocols, and data format requirements for manual submissions.