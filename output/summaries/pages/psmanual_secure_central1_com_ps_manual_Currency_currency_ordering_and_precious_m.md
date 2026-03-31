# Summary: Precious Metals Module (Section 14)

- **Purpose**: Documents the end-to-end process for Class A clients (BC/ON only) to purchase and sell back precious metals through Central 1's partnership with Royal Bank of Canada, with armoured car delivery via cash parcels.

- **Key Processes**:
  - Purchase workflow: quote request → customer confirmation → order placement → delivery via next RBC cash parcel
  - Sell-back workflow: quote request → customer confirmation → physical preparation → shipment in next outbound cash parcel → settlement
  - Both constrained to 5:00 AM–1:30 PM PT, Monday–Friday only (no statutory holidays)

- **Critical Data Elements**: Quote requests and order confirmations require FI name, branch address, and transit number; sell-back parcels require separate deposit slips (not returned as receipt) with product type(s), quantities, and matching manifest values.

- **Inventory & Pricing**: Live market quotes apply to all transactions; flat ordering/sell-back fees charged; no additional delivery charges. Products limited to RBC Mint bars/coins (gold 1kg/1oz bars, 1oz coins; silver 100oz bars, 1oz coins with 10-coin minimum).

- **Integration Points**: Central 1 Treasury (treasury@central1.com) acts as intermediary; settlement posts to FI's Central 1 current account; RBC dispatch/delivery dates drive settlement timing; armoured car company logistics dependency for parcel delivery.

- **Internal Controls & Verification**: FIs must verify incoming/outgoing parcels in joint custody within 24 hours; maintain vault registers; reconcile inventory daily if applicable; discrepancies trigger Central 1-RBC investigation with account adjustments posted at settlement.

- **Architectural Considerations**: Eligibility filtering (Class A + BC/ON), time-window validation (5 AM–1:30 PM PT), statutory holiday exclusion, quote-to-order state machine, settlement integration with core account system, and audit trail requirements for internal control compliance.