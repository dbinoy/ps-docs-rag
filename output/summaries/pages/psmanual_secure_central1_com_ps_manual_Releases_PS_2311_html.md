# Payment Solutions Release 23:11 Summary

- **Purpose**: Release notes documenting updates to Currency Ordering functionality and Cash Services user management procedures, effective June 7, 2023.

- **User Profile Management Enhancement**: Locations Filter capability added to Section 6.3 user profile creation workflow in Cash Services module, enabling filtered location assignment during initial user setup.

- **Access Control Updates**: Section 6.9 procedures revised to support filtering logic when modifying location-based access permissions for existing users—indicates role-based access control tied to location hierarchies.

- **Supply Chain Integration**: Currency ordering workflow depends on external provider routing (Brinks or designated cash shipment provider) for penny bag procurement; Westkey Graphics explicitly excluded as a penny bag source, suggesting multiple vendor integrations with specific capability mappings.

- **Canadian Currency Processing Rules**: Strict coin deposit constraints defined—loose/rolled CAD notes and non-penny coins share deposit slips, but pennies require: (a) loose form, (b) separate bag, (c) fixed denomination ($25/bag). This indicates transaction validation rules and deposit slip generation logic must enforce these constraints.

- **Critical Data Constraints**: Penny bag denomination ($25 CAD) is a hardcoded business rule; separate deposit slip logic for penny vs. non-penny coin suggests distinct transaction types or line-item categorization in deposit records.

- **Support Contact**: Escalation path to Client Support Services (1-888-889-7878 Option 1 or support@central1.com) indicates documented procedures are customer-facing and require support alignment.