# Summary: FX Notes Foreign Exchange Spreads and Transaction Fees Management

- **Purpose**: Authorized FX Notes Managers configure retail rate modifiers (FX spreads) and transaction fees through the Retail Rate Modifiers page to generate institutional income by adjusting exchange rates and applying per-transaction charges on currency conversions.

- **Key Entities & Operations**: Two primary configurable objects—**Foreign Exchange Spreads** (retail rate modifiers) and **Transaction Fees**—each supporting full CRUD operations (add, update, delete) with no dual authorization requirement currently enforced.

- **Rate Application Model**: Configured spreads/fees are embedded in transaction amounts at order entry time; live system rates at transaction submission override any cached or downloaded rate sheets, creating potential discrepancies between downloaded CSV/XLSX reports and actual settlement rates.

- **Access Control**: Management restricted to "Authorized FX Notes Managers" role with no granular field-level or approval workflow controls documented; single-actor authorization implies simplified governance model.

- **Data Export & Reporting**: Rate Sheet reports available in CSV/XLSX formats via transactional module; downloadable snapshots are point-in-time views and explicitly documented as potentially stale relative to live rates at order processing.

- **System Dependencies**: Tight coupling between FX Notes application and core order entry system (rates must be synchronized at transaction submission); no mention of external FX data feeds, reconciliation processes, or audit logging for spread/fee modifications.

- **Architectural Gap**: No documented versioning, change history, or rollback mechanisms for rate/fee updates; audit trail for configuration changes not addressed, creating compliance and dispute-resolution risks.