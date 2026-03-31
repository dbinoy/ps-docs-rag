# Payment Solutions Release Summary: FX Drafts Platform Migration (August 7, 2020)

- **Overview**: Western Union Business Solutions (WUBS) migrated FX Drafts to a new platform, requiring procedural updates across User Management, system requirements, and contingency operations.

- **Access Control Architecture Change**: User permissions for FX Drafts transitioned from centralized CPS Admin/User Management to distributed admin-level permissions within the FX Drafts application itself—requires architectural consideration for identity federation and permission synchronization between systems.

- **System Requirements & Dependencies**: New Section 1.2 documents updated system requirements for FX Drafts; architects must review compatibility matrices and any changes to integration endpoints or API contracts with WUBS infrastructure.

- **Regulatory Integration Point**: Cross-references added to Operations Manual Program (subscription-based for BC/Ontario credit unions) for anti-money laundering (AML) compliance procedures—indicates AML validation logic may be externalized or require audit trail design for regulatory reporting.

- **Contingency Data Flows**: New Chapter 8 introduces desktop-based fallback procedures (forms 9189, 9190) for stop payment requests and draft stock orders when FX Drafts application is unavailable—architects must design offline-capable transaction queuing and eventual consistency mechanisms.

- **Document Library Obsolescence**: Four legacy documents marked obsolete (6295, 6395, 6396, 8896); two new CU Admin and Order Creator user guides (9182, 9183) indicate role-based feature differentiation requiring separate API/UI surfaces.

- **Support & Escalation**: Single point of contact (Central 1 Client Support: 1-888-889-7878 Option 1) suggests centralized incident management; no mention of self-service diagnostics or health check APIs.