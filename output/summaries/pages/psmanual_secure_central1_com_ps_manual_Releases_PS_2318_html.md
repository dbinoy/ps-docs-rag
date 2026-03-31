# Release 23:18 (July 25, 2023) - Interac e-Transfer OAS Documentation Update

- **Scope**: Documentation update for Interac e-Transfer Online Administration System (OAS) with migration of reference materials from secure site to Client Centre portal

- **Key Integration Point Change**: Login workflow migrated from secure site authentication to Client Centre authentication—architects must ensure Client Centre IAM integration is primary authentication mechanism for OAS access

- **Data Flow Impact**: Tracing and transaction lookup functionality remains unchanged; new Section 4.8 (Archived Data Searches) added to OAS tracing workflows, requiring support for historical data retrieval patterns

- **New Concept Introduced**: "Interrupted Transfers" formalized as a distinct transfer state with specific troubleshooting procedures; this requires architects to account for intermediate/failed states beyond standard success/failure binary outcomes

- **Documentation Consolidation**: Obsolete Interac e-Transfer Fraud Management documentation removed from OAS guides—architects should verify no active system dependencies exist on deprecated fraud management workflows or data structures

- **System Capabilities**: OAS supports customer profile viewing, transaction tracing, and archive data searches; architects need to understand data retention policies for archived transfers

- **Support Dependency**: Escalation point is Client Support Services (1-888-889-7878); architects should document OAS-specific troubleshooting procedures and SLAs for transfer status resolution