# Payment Solutions 24:08 Release Summary

- **Overview**: Documentation update released February 15, 2024, addressing user guidance in the "How to Use this Manual" section and printing functionality.

- **Terminology Migration**: All references to "secure site" have been deprecated and replaced with "Client Centre" terminology—indicates a platform rebranding or consolidation that architects should account for in UI/API documentation and any client-facing integrations.

- **Client Centre as Primary Portal**: The update emphasizes Client Centre as the central access point; architects should understand this is the primary user interface for forms, news, and notifications rather than legacy secure site infrastructure.

- **New Notification & Preference Features**: System now supports user-initiated signup for news notifications and configurable news update preferences—suggests new backend services for notification management, user preference persistence, and potentially message queue integration (if not already present).

- **Forms Management Capability**: Added searchable forms library on Client Centre—architects should identify whether this is a new forms repository service, search index infrastructure, or integration with existing content management systems.

- **Support Contact Point**: Client Support Services remains the escalation path (1-888-889-7878 Option 1, support@central1.com)—useful for understanding SLA/support dependencies during architecture decisions.

- **No Breaking API or Data Model Changes Indicated**: This is primarily a documentation and UI update with no apparent changes to payment processing logic, data structures, or system integrations.