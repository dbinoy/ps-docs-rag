# Release 23:04 (March 3, 2023) Summary

- **Scope**: Documentation updates to Interac e-Transfer® Online Administration System (OAS) Part covering definitions, search functionality, customer profiles, and troubleshooting procedures.

- **Key Concept - Limit Management**: Updates to Limit Groups, Rolling Limit, and Rolling Period definitions reflect changes to Interac's incoming e-Transfer limits—architects should understand these are configurable thresholds that govern transaction volume constraints.

- **New Product Line**: Introduction of "Interac e-Transfer for Business" as a distinct definition suggests expanded product scope requiring separate handling/configuration paths from consumer transfers.

- **OAS Search Capabilities**: Two distinct search functions now documented—Basic Searches (Section 4.2, renamed) and Advanced Searches (Section 4.7)—indicating tiered query complexity for transaction lookups and reporting; architects should plan for dual query interfaces.

- **Customer Profile Data Structure**: Section 6.2 updates describe transfer limits field modifications within customer profile summaries, suggesting schema changes to how limit thresholds are stored/displayed per customer entity.

- **New Support Function**: Chapter 9 addition (Troubleshooting Tracing Requests) indicates new operational workflow for investigating transaction issues—potential integration point for logging, audit trails, and escalation tracking.

- **Integration Dependency**: All references point to OAS as the administrative interface; this is a central system managing customer limits, transfers, and traces—critical for any downstream transaction authorization logic.