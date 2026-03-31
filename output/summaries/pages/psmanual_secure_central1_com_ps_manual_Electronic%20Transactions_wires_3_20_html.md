# Summary: Searching for Wires and Exporting Wire Information

- **Core functionality**: Users can search, filter, and export wire transaction records (both incoming via Received Wires and outgoing via Submitted Wires) with a rolling 7-year historical data window.

- **Search constraints**: Date range filters are capped at a maximum 100 calendar-day span per query, requiring architects to consider pagination or batch processing strategies for larger historical queries.

- **Data export mechanism**: Search filters are applied to CSV exports, meaning the export respects all active filter criteria—this implies the export function depends on the filter state rather than querying raw data independently.

- **Data retention policy**: 7-year rolling history is maintained; architects should clarify whether this is enforced at the database level or via archival/purge processes, and whether it applies uniformly across both Received and Submitted wire types.

- **Dependent process**: Wire searching relies on prior navigation via Section 19.2 (Viewing Wires and Wire Details), indicating a hierarchical UI flow; any API redesign must account for this dependency chain.

- **Receipt generation and printability**: Submitted wires support dual-view modes (Details vs. Receipt) and printing; the receipt view strips internal details, suggesting separate data presentation layers or field-level masking logic that architects must preserve.

- **No external system integrations mentioned**: The page describes internal wire management only; no third-party payment networks, bank APIs, or settlement systems are referenced—clarify upstream/downstream integrations separately.