# Payment Solutions Release Summary: v21:35 (September 23, 2021)

- **Overview**: Electronic Bill Payments System update removing obsolete form procedures and marking related verification documentation as deprecated.

- **Key Change**: Section 12.4 (Biller-Initiated Bill Payment Queries and Traces) procedures removed due to form obsolescence—impacts query/trace workflows for biller-initiated transactions; architects should verify no active integrations depend on these deprecated procedures.

- **Affected Process Area**: Bill Payments Volume operations within the Electronic Bill Payments System Part; scope limited to query and trace functionality rather than core payment processing.

- **Documentation Status Change**: "Member Payment Verification – Electronic Bill Payments System" (document ID 2195) marked as Obsolete—architects must reference updated documentation and avoid designing against deprecated verification structures.

- **No New Data Structures/Fields**: This is a removal-only release; no new integration points or API changes introduced.

- **Support & Clarification**: Client Support Services (1-888-889-7878, Option 1; support@central1.com) handles migration questions—escalate if legacy biller-initiated trace integrations require design workarounds.

- **Architectural Implication**: Review existing payment query/trace implementations for dependency on Section 12.4 procedures; plan refactoring if active systems reference obsolete form handling.