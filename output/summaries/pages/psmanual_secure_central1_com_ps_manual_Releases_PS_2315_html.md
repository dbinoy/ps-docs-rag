# Payment Solutions Release Summary: 23:15 (July 5, 2023)

- **Release scope**: Update to Digital & Payment Services Class A Fee Schedule (Form 2725) with details published in accompanying secure site news item—review news item for specific fee structure changes and effective dates.

- **Regulatory/product constraint**: Form 2725 availability limited to Class A credit unions in BC and Ontario jurisdictions only; any system enhancements must enforce this geographic and institutional-type eligibility rule.

- **Document artifact**: Form 2725 is a versioned document in the Document Library with "Revised" status; architect must understand version control, deployment mechanism, and how fee schedule updates propagate to downstream billing or rate-calculation systems.

- **Data structure implication**: Fee schedule likely contains rate tables, service codes, and pricing matrices; confirm data schema changes and whether existing API contracts or fee-lookup endpoints require modification to handle revised structure.

- **No explicit integration points documented**: This release appears to be a configuration/content update rather than a system integration; however, verify whether billing engines, customer-facing portals, or partner systems consume Form 2725 data and require synchronization.

- **Support and change management**: Contact point is Client Support Services (1-888-889-7878 Option 1); establish change notification process to ensure impacted teams are informed of fee schedule revisions.

- **Incomplete specification**: Detailed changes are deferred to a separate news item—request the linked news item to identify specific fee impacts, backward compatibility concerns, and any required data migrations.