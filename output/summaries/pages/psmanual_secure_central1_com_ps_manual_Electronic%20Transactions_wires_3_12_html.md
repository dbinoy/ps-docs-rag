# Summary: Managing Foreign Exchange Spreads in Wires

- **Purpose**: Documents procedures for authorized Wires Users to view, add, modify, and delete foreign exchange (FX) spreads that are automatically calculated into outgoing wire transfers in foreign currencies.

- **Access Control**: FX spread management requires MTS "Spreads and Fees" permission assignment; user provisioning is defined in Section 8.6 of the documentation.

- **Spread Classification Hierarchy**: Spreads can be set at two levels—by currency classification (major, minor, exotic, pegged) or by individual currency—with individual currency spreads overriding classification-level spreads, establishing a precedence rule for configuration resolution.

- **Automatic Calculation**: FX spreads are automatically injected into outgoing wire transfer amounts; no manual intervention required post-configuration, indicating real-time integration at wire processing/calculation layer.

- **Data Operations**: Four CRUD operations are supported: view (Organization Spreads page), create, update (spread value and type field), and delete, with confirmation workflows (green checkmark to confirm, red X to cancel).

- **Spread Type Field**: A "Type" dropdown exists for spread classification, but the documentation does not enumerate valid values—clarification needed on whether this maps to spread methodology (e.g., percentage, basis points, fixed amount).

- **Dependencies**: Integration with MTS user management system for permission enforcement; wire processing system must consume configured spreads at transaction time; no data export, audit logging, or version control procedures are documented.