# Summary: Archiving Closed Trace Requests

- **Purpose**: Documents the archival workflow for closed trace requests in the Online Tracing (OLT) system, enabling Tracers and SuperTracers to manually archive traces or allow automatic archival after seven calendar days.

- **Automatic Archival Policy**: Closed traces are automatically archived after seven calendar days; manual archival can be initiated anytime before this deadline by authorized users (Tracers/SuperTracers).

- **Archive Effect & Data Access**: Archived trace requests are removed from the OLT Inbox but remain accessible via the Search Trace Request function—archived data is not deleted, only relocated from the active inbox view.

- **Critical Constraint**: Traces with status "closed - pending adjustment" are explicitly blocked from archival, indicating a business rule that prevents archiving traces awaiting post-closure modifications.

- **User Roles & Access Control**: Only Tracers and SuperTracers have permission to initiate manual archival; role-based access control is enforced at the OLT application level.

- **Process Integration**: Archival is integrated into the OLT Inbox UI workflow and depends on the Search Trace Request function for retrieving archived records—suggests two distinct data retrieval paths (active inbox vs. search archive).

- **Architect Consideration**: Design must account for a time-based archival trigger (seven-day background job), status-based exclusion logic, and dual-state data accessibility (inbox vs. searchable archive) without permanent deletion.