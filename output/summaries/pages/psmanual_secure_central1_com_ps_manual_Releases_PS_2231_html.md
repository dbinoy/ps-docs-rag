# Summary: PS 22:31 Release — AFT National Expansion (December 12, 2022)

- **Purpose**: Documentation updates reflecting Automated Funds Transfers (AFT) transition from regional to national availability, with removal of region-specific details and standardization to local time zone calculations.

- **Key Concept — Regional to National Migration**: AFT products now available nationally instead of isolated to BC/Ontario/Atlantic regions. Documentation revised to remove hardcoded region references (e.g., "BC Only" → "BC and Atlantic Region"; "Ontario Only" → "All Regions Except BC and Atlantic"), requiring clients to calculate equivalent local times against published deadlines.

- **Critical Data Structures**:
  - **Destination Data Centre field (A record)**: Code 86920 restricted to Ontario originators only; 86900 for all other regions — enforces routing logic at origination point.
  - **Institution ID Number (C/D records)**: Examples clarified for BMO (000102180) to prevent regional ambiguity; removed BC (809) and ON (828) examples to eliminate region-specific assumptions.

- **Time Zone Processing Constraint**: No single time zone reference model; clients must independently calculate equivalent times for file delivery deadlines and error correction windows. This shifts validation responsibility to integrators and impacts batch scheduling logic in downstream systems.

- **Integration Dependency**: AFT File Specifications (doc 2726) and clearing file specs (6269, 6270, 9083–9086, 9528) are foundational to file structure validation; changes to Destination Data Centre codes require upstream origination systems and downstream clearing processors to align routing rules.

- **Service Configuration Changes**: Auto Offset feature removed "ON Region only" restriction (Service Application doc 5329), indicating functional parity across regions — architects must verify no downstream rules still assume regional gating.

- **Support Point**: Escalation channel: Client Support Services (1-888-889-7878 Option 1 or support@central1.com) for implementation questions regarding time zone calculations and regional code mappings.