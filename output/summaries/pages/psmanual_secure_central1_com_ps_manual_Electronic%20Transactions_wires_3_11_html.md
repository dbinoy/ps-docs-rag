# Summary: Managing Outgoing Wire Fees

- **Purpose**: Provides operational guidance for authorized Wires Users to configure, view, modify, and delete outgoing wire fees that financial institutions charge customers; fees can be manually entered or pre-populated based on defined criteria.

- **Fee Configuration Model**: Two fee types are configurable—regular outgoing wire fees and add-on fees (for future-dated/priority wires)—with two application modes: manual entry (no pre-configuration) or pre-populated (auto-filled based on user-defined rules, overridable by users).

- **Fee Matching Criteria**: Fees are defined by three hierarchical/combinatorial dimensions—maximum settlement amount (tiered up to $1,000,000, nullable for "any" amount), wire currency (CAD, USD, ANY), and destination country (Canada, United States, ANY)—with fee currency dynamically determined by transfer currency selection.

- **Permission & Access Model**: Access requires MTS "Spreads and Fees" permission assignment; only authorized Wires Users can perform all CRUD operations on fees via the Fees function in the Wires application.

- **External Cost Pass-Through Constraint**: Central 1 charges monthly processing fees per wire (with surcharges for priority/future-dated wires); the documentation requires configured customer fees to meet or exceed Central 1's processing fees to ensure cost recovery—this establishes a business rule dependency on external pricing data.

- **Field Immutability Rule**: Maximum Settlement Amount, Transfer Currency, Destination Country, and Fee Currency fields are read-only after creation; modifications require deletion and recreation, creating a potential operational friction point for architects designing audit/change workflows.

- **Customization Exception Path**: Form 6493 (Wires Customization Request) exists for contingency-only updates to pre-populated fees, indicating out-of-band fee adjustments bypass the standard UI—architects should understand this escape hatch's governance implications.