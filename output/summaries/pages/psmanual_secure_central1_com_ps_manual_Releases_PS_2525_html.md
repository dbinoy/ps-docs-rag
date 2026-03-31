# Release 25:25 (October 7, 2025) - International Transfers Documentation Migration

- **Overview**: Central 1 migrated International Transfers implementation documentation and forms from its Payment Solutions manual to Intellect Design, consolidating International Transfers resources under a single vendor platform.

- **Affected Forms & Content Removed**:
  - Form 9080: International Transfers Implementation Requirements – Retail
  - Form 9111: International Transfers FX Spread
  - Both forms transferred to Intellect Design and removed from Central 1's forms library

- **New Access Model**: Implementation information, forms, and resources for retail and business International Transfers are now accessed via the **International Transfers product page on the Client Centre** (not the Payment Solutions manual).

- **Integration Point Change**: International Transfers workflows now depend on Intellect Design as the authoritative system of record; any enhancements or form modifications require coordination with Intellect Design, not Central 1.

- **Architectural Implication**: Solutions must treat International Transfers as a managed service via external vendor (Intellect Design) rather than internally-documented functionality; client-facing systems should route International Transfers inquiries and resource links to the Client Centre product page.

- **Support & Governance**: Client escalations continue through Central 1 support (1-888-889-7878, Option 1 or support@central1.com), but technical implementation details now originate from Intellect Design's documentation.