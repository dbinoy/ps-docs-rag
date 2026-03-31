# Payment Solutions Release 20:06 Summary (March 4, 2020)

- **Overview**: Release introduces availability of unlocked forms on the secure site for internal system integration, with corresponding user responsibility and compliance requirements.

- **Form State Management**: Two form states exist—unlocked (for import/customization) and locked (for Central 1 processing). Locked forms protect integrity; unlocked forms require user compliance oversight. Form state is indicated in the Document Library "Format" column.

- **Compliance & Governance**: Organizations must independently verify compliance when modifying unlocked forms (e.g., Form 1696 Payor's PAD Agreement must maintain CPA Rule H1 compliance). Central 1 will not accept altered forms returned for processing.

- **Form Lifecycle Monitoring**: Users are responsible for continuous monitoring of the secure site for form updates and must immediately sync changes to internal systems—this creates an ongoing dependency on external form versioning.

- **Integration Constraints for Locked Forms**: Organizations importing locked forms into internal systems (banking systems, learning management systems) require explicit approval from Central 1 and must test output against the original to confirm no alterations occurred before production use.

- **Forms Released as Unlocked** (13 total): Includes payment transfers (1171), PAD agreements (1696), wire transfer routing instructions across 7 currencies (2605-3776), and other transaction types. Three forms (2605, 2606, 2607, 3710, 3771-3776) marked "Revised" with minor wording changes but no functional/routing data changes.

- **Key Integration Points**: Secure site document library, Central 1 support (1-888-889-7878), internal banking systems, and learning management systems; no API/system-to-system data flow documented.