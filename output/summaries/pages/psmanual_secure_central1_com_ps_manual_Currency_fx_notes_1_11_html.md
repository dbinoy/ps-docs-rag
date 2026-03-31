# Summary: Viewing Transactions, Images, and Shipments (FX Notes)

- **Purpose**: Provides user workflows for accessing and filtering FX transaction records, shipment management, and foreign currency denomination images within the FX Notes platform.

- **Transaction Status Taxonomy**: System defines 13 distinct transaction states (Draft, Pending Compliance/Operational/Financial Approval, Pending Reception, Pending Vault Processing, Ready to Prepare, Ready to Ship, Delayed, Completed, Voided, Cancelled, Adjusted) that represent approval workflows across compliance, operations, and finance teams—critical for multi-stage authorization design.

- **Transaction Filtering**: Orders page supports filtering by transaction type (Buy from Client, Sell to Client), status, and date range; Shipments page supports filtering by tracking/waybill number or carrier—filters must support compound queries and be indexed for performance.

- **Shipment Label Generation**: Shipping labels are generated from transaction records and retrievable via transaction Reference Number; labels are browser-printable via standard print function—no proprietary label format engine required, but audit trail needed for reprints.

- **Currency Image Management**: Foreign currency denominations sourced from external vendor "Globex 2000" and stored with thumbnail/full-resolution image assets accessible via currency → denomination → image hierarchy—indicates external asset repository dependency and potential CDN integration point.

- **Dependency on Section 6.2 Authentication**: All workflows require prior login via authentication process defined elsewhere; architecture must ensure session management spans multiple functional areas (Transactional → Orders/Shipments/Denomination).

- **Reference Entity Linkage**: Transactions generate "Buying Operation and Client Receipt" documents; shipment tracking tied to transaction Reference Number—core data model requires strong foreign key relationships and denormalization for reporting.