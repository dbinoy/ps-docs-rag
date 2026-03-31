# Summary: Payment Solutions 20:10 Release – Cash Services Procedures Update

- **Purpose**: Release notes documenting updates to Cash Services Procedures Quick Reference Guide (Form 9031) effective April 27, 2020, clarifying system functionality for migrated financial institutions during transitional period before full Payment Solutions Manual consolidation.

- **System Availability**: Cash Services operates with no time limitations—24/7, 7-day-a-week availability with no scheduled downtime constraints for order entry and management operations.

- **User Type Architecture**: System distinguishes between eClient user types (Admin, Access Management, standard user) and Branch user types; financial institutions are restricted to eClient types only, with Branch types visible but non-functional in FI configurations. Admin and Access Management roles have location-scoped permissions (can only manage profiles for users with overlapping location access).

- **Core Data Entities & Workflows**: Primary workflows encompass user/profile creation and maintenance, cash order entry with default field population, order state management (Pending → Ready → Carrier Check → Released), and delivery date search filtering (treating Delivery Date as "from" parameter rather than exact match).

- **Reporting & Settlement**: New Chapter 4 introduced Cash Services Settlement Reports functionality; integration point likely for reconciliation with back-office accounting systems.

- **Temporal Constraint**: Document explicitly marked as temporary resource pending full migration of all financial institutions; architecture must accommodate future consolidation into unified Payment Solutions Manual covering multi-provincial procedures.

- **Support Dependencies**: Escalation path defined through Client Support Services (1-888-889-7878, Option 1; support@central1.com)—indicates production support model requires external ticketing integration.