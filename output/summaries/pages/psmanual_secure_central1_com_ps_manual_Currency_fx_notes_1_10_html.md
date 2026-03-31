# Summary: Buying Foreign Currency from a Customer (FX Notes)

- **Purpose**: Defines the operational workflow for financial institution staff to purchase foreign currency from customers via FX Notes, including authentication, order processing, and secure shipment to Globex 2000.

- **Authentication & Compliance**: Currency notes must be visually verified against FX Notes reference images before purchase acceptance; transactions ≥$10,000 CAD equivalent trigger FINTRAC Large Cash Transaction Reports; transactions ≥$3,000 CAD equivalent require KYC data capture (name, address, DOB) and Foreign Exchange Transaction Ticket (Form 1923).

- **Key Data Elements in Buy Order**: Branch Location (multi-branch routing), Pricing Options (FX spread selection), Product Type (always "CASH"), Transaction Fee (Yes/No with configurable amount), Currency (dropdown), Amount (foreign currency quantity or CAD Value equivalent), Exchange Rate (non-editable, Globex 2000 rate with 15-minute hold), Denomination Breakdown (granular currency composition).

- **Integration with Globex 2000**: FX Notes submits orders to Globex 2000; exchange rates are pulled from Globex; shipping method (UPS primary, Canada Post for remote areas) is determined by Globex during enrollment; maximum package size is $5,000 CAD equivalent per opaque bag, $10,000 CAD equivalent per order (max 2 packages).

- **Shipment Workflow**: Orders must have "Pending Reception" status before label/packing slip download; dual-custody packing in camera-monitored space required; receipts and packing slips accompany each opaque security bag; UPS pickup called in (not online) on business days only with prepaid label; driver must scan packages before departure.

- **Critical Constraints for Architects**: 15-minute rate holds (refresh capability required), $5,000/$10,000 shipment caps with multi-package orchestration, Retail Rate Modifiers dependency for fee management, counterfeit detection escalation path (RCMP/local police), operational audit trail via camera timestamps and courier scans.