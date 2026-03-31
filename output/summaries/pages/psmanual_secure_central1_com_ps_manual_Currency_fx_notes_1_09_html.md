# Summary: Selling Foreign Currency to a Customer (FX Notes)

- **Scope**: Documents the complete workflow for Standard FX Notes users to sell foreign currency (cash) to customers, from order placement through delivery and receipt verification.

- **Order Processing Flow**: Orders entered in FX Notes → Globex 2000 receives order → physical currency shipped via courier (≤$20K CAD per package, max 2 packages) or armoured car (>$20K CAD) → delivery to financial institution within 1-5 business days depending on currency type and region.

- **Currency Categories & Availability**: Two tiers—major currencies (AUD, EUR, JPY, MXN, CHF, GBP, USD) with 1-2 day delivery to major Canadian cities; minor currencies with 1-5 day delivery nationwide. List is dynamic and managed within the FX Notes application.

- **Time-Sensitive Deadlines & Rate Management**: Orders submitted after 3:00 pm ET (12:00 pm PT) are processed next business day with current day's exchange rate but next day delivery SLA. Exchange rates held for 15 minutes and refreshable; rate field is read-only.

- **Order Form Data Structure**: Key fields include Branch Location (multi-branch support), Pricing Options (user-configured FX spreads), Product Type (hardcoded as CASH), Transaction Fee (configurable per internal policy), Currency, Amount (foreign currency quantity), CAD Value (calculated equivalent), Denomination Breakdown (best-effort fulfillment), Customer Name, and Special Requests.

- **Order Lifecycle & Cancellation Window**: Orders remain editable/cancellable for 1 hour post-submission while in "Pending Operational Approval" status; after approval, currency must be retained in inventory or returned to Globex 2000 per Chapter 10 procedures.

- **Receipt Verification & Compliance Requirements**: Mandatory joint-custody verification within 24 hours of receipt (note count, authenticity check, no counterfeits). Damaged parcels must be documented with photos and reported to C1support@globex2000.com; packaging retained pending Globex 2000 disposition instructions. FINTRAC Large Cash Transaction Reports required for ≥$10K CAD customer cash payments; AML Compliance Officer consultation and Form 1923 (Foreign Exchange Transaction Ticket) may be required.

- **Integration Dependencies**: FX Notes application interfaces with Globex 2000 (order fulfillment, shipping coordination), courier/armoured car logistics providers, financial institution branch location registry, and AML/FINTRAC compliance framework.