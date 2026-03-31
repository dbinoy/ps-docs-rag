# Summary: Chapter 24 - Receiving Incoming Wires

- **Overview**: Document defines the operational and compliance workflow for inbound wire receipt through Central 1's Wires platform, including acceptance/return logic, sanctions screening, and FINTRAC reporting requirements.

- **Wire Processing Flow**: Non-participating institution wires upload ~10-minute intervals; participating institution wires display immediately in "Pending Incoming" status. Only business days (Mon-Fri, excluding statutory holidays) supported.

- **User Access Control**: Requires MTS "Update Incoming Transfers" permission + 2-step security token assigned to Client Centre ID; visibility scoped to user's assigned branches via MTS configuration (Chapter 9).

- **Sanctions Screening Integration**: Central 1 scans all inbound wires against government sanctions lists; wire status transitions: Frozen → Under Investigation (if match confirmed) or Frozen → Pending (if cleared). Funds held in Central 1 escrow account during investigation; financial institution responsible for secondary screening, FINTRAC reporting, and PEP/HIO determination.

- **Routing Instructions**: Currency-specific forms (10 currencies supported: CAD domestic/international, USD, EUR, GBP, AUD, CHF, JPY, MXN, PLN, NZD) define required fields for beneficiary/correspondent financial institution identification; missing/incorrect routing causes wire rejection or unfavorable FX conversion.

- **Regulatory Compliance Touchpoints**: Mandatory FINTRAC EFT reporting for international wires ≥$10,000 CAD equivalent (5-business-day submission window); suspicious transaction reporting; CPA By-law No. 7 section 49 name-account matching logic; PCMLTFA prohibition on disclosure of reported transactions.

- **Critical Constraint - Frozen/Under Investigation Wires**: Cannot be accepted or returned while in either status; requires Central 1 Compliance + financial institution's corporate security + government agencies for resolution; staff must never disclose investigation status to parties.