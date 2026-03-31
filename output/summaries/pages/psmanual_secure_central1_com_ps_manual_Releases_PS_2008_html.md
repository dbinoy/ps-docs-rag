# Payment Solutions 20.08 Release Summary

- **Release scope**: March 31, 2020 update to the Wires Part of Payment Solutions documentation, focused on wire transaction management capabilities and regulatory framework updates.

- **Core new functionality**: Introduction of outgoing wire editing capability (Chapter 11) for authorized users to modify unapproved wires, with defined rules and restrictions governing when edits are permitted.

- **Wire transaction states and data structures**: System maintains four distinct wire list states—Pending Incoming, Pending Outgoing, Submitted Wires, and Received Wires—with enhanced documentation for viewing lists and examining wire details.

- **Regulatory framework changes**: Migration from legacy regulatory bodies (FICOM, FSCO) to current authorities (BCFSA for British Columbia, FSRA for Ontario), requiring updated contact references and definitions across documentation.

- **Key architectural constraints**: Edit operations are restricted to unapproved wires only, suggesting a state-machine workflow where wire approval status gates modification capabilities and prevents editing of submitted/processed transactions.

- **Integration considerations**: Incoming wire reception procedures (Section 16.2) are documented alongside outgoing wire management, indicating bidirectional wire flow handling with distinct operational procedures for each direction.

- **Data governance**: New definitions added for BCFSA and FSRA, suggesting compliance metadata or regulatory classification fields may exist in wire transaction schemas to support multi-jurisdictional operations.