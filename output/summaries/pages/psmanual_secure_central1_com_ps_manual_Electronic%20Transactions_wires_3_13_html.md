# Summary: Viewing Live Rates in Wires

- **Purpose**: Documents the foreign exchange rate viewing functionality within the Wires electronic transactions module, enabling users to access current FX rates with applied spreads in real-time.

- **Core Functionality**: The Rates page displays a live snapshot of FX rates at time of access; rates are dynamically updated and reflect market movements. All Wires users have read-only access to this feature.

- **FX Spread Application**: Displayed rates include the institution's configured foreign exchange spread (variable per institution), meaning rates shown are not raw market rates but retail-quoted rates.

- **Rate Refresh Mechanism**: Rates can be manually refreshed via UI control; no automatic real-time polling is documented—manual refresh implies either on-demand data fetching or cached rates with user-triggered updates.

- **Data Export Capability**: CSV export functionality available, suggesting the system maintains exportable rate datasets and interfaces with file generation/download services.

- **Critical Constraint - Weekend Stasis**: Rates held static Friday through Sunday (no updates Saturday); Saturday rates are Friday's closing rates. This affects any integration expecting continuous 24/7 rate currency and impacts trading/settlement windows.

- **Dependency**: Requires successful authentication via Wires login (Chapter 10), indicating dependency on identity/session management subsystem and role-based access control.

- **No Integration Details**: Page omits upstream data sources (market feeds, rate calculation engines, or reference systems), suggesting rates are provisioned/maintained externally to this UI component.