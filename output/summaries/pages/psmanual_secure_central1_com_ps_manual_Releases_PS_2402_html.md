# Release 24:02 Summary: PaymentStream AFT Maintenance Window Update

- **Release scope**: Documentation update to PaymentStream AFT (Automated Funds Transfer) availability hours and transaction purge schedule, effective January 4, 2024

- **Service availability constraint**: PaymentStream AFT services are unavailable Sundays 1:00 AM – 3:00 AM PT; this is a hard maintenance window that must be communicated to all downstream consumers

- **Data purge operation**: Transaction purge schedule for PaymentStream AFT executes during the same maintenance window (Sundays 1:00 AM – 3:00 AM PT); architects must account for data retention policies and recovery requirements around this cycle

- **AFT origination dependency**: Updates affect "Originating AFT via PaymentStream" workflows; any system initiating AFT transactions through PaymentStream must handle service unavailability during the maintenance window (implement retry logic, queue management, or schedule submissions outside this window)

- **Documentation references updated**: Section 1.3 (availability/support hours) and Section 13.2 (purge schedule) in the PaymentStream AFT manual reflect these timing changes; integration documentation must align with these specifications

- **Integration consideration**: Systems dependent on real-time AFT processing or expecting continuous availability must implement timeout handling and graceful degradation for the weekly 2-hour maintenance window

- **Support escalation path**: Client Support Services (1-888-889-7878, Option 1, or support@central1.com) is the contact for implementation questions regarding the new maintenance window impact on integrations