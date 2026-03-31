# Release 23:22 Summary for Solutions Architects

- **Scope**: Policy alignment update for FX Notes Plus foreign currency shipment procedures following Exchange Bank of Canada (EBC) liability limit changes mandated by FedEx and domestic insurance guidelines.

- **Key Constraint**: Maximum liability capped at $10,000 CAD equivalent per FedEx Envelope/Box with limit of 4 units per delivery address per day; exceeding this threshold triggers mandatory armoured courier delivery with associated fees (cost model not specified in release notes).

- **Process Changes**: 
  - Currency shipments now require dual-custody packaging under HD camera surveillance
  - Sealed envelope signatures must be applied with permanent marker
  - Courier pickup requires package-level scanning verification
  - Claims processing now depends on video footage evidence

- **Documentation Updates**: Terminology migration from "secure site" to "Client Centre" across affected sections (7.1, 7.3, 13.1, 13.2); liability limit notes embedded in order deadline/delivery method guidance and shipping overview sections.

- **Integration Dependencies**: Relies on FedEx liability policies and EBC insurance guidelines; armoured courier fulfillment pathway must be integrated into delivery method selection logic when order amounts exceed $10,000 CAD equivalent.

- **Architect Considerations**: Design order validation rules to flag and route high-value shipments; implement fee calculation for armoured courier alternative; ensure video capture/retention system integration for claims validation workflows; update client-facing documentation references in UI/API responses.