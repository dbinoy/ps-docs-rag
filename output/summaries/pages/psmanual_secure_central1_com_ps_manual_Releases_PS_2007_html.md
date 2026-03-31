# Payment Solutions 20:07 Release Summary (March 16, 2020)

- **Release scope**: Enhancement to FX Notes Plus module introducing foreign cheque return reporting with visual attachments and updated currency shipping thresholds.

- **Foreign cheque return reporting enhancement**: FX Notes Plus now displays detailed notes and image attachments for returned foreign items and reference documents, requiring UI/database updates to render and store binary image data alongside transaction records.

- **Shipping threshold policy change**: EBC (Exchange Bank of Canada) contact requirement threshold increased from CAD $5,000 to CAD $10,000 equivalent per single transaction—impacts business logic for shipping instruction routing and financial institution workflows.

- **Currency conversion dependency**: System must evaluate transaction amounts in CAD equivalent values, implying integration with currency conversion service or rate table to normalize multi-currency transactions against CAD baseline.

- **Documentation coupling**: Manual updates across multiple sections (1.4, 13.1, 15.4) indicate scattered business logic implementation; architects should map feature dependencies across contacts registry, shipping procedures, and reporting modules.

- **Data attachment architecture**: Foreign cheque return reports now require blob storage (image attachments) and document linking—consider scalability, indexing strategy, and access control for stored images within transaction records.

- **External system dependency**: Exchange Bank of Canada (EBC) represents a critical integration point for shipping instructions; threshold logic should be externalized as a configurable parameter to accommodate future policy changes without code deployment.