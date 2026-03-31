# Payment Solutions Release Summary: PS 24:47

- **Release Scope**: Service Level Agreement (SLA) updates from Convera, Central 1's FX Draft vendor partner, with corresponding documentation revisions (December 27, 2024)

- **FX Draft Functionality**: Two-tier user role system for Foreign Exchange Drafts—Admin Users (Form 9182) and Order Users (Form 9183)—indicating role-based access control and distinct operational workflows

- **Documentation Updates**: Both FX Draft guides (Forms 9182 and 9183) have been revised; "What's Changed" sections in those documents contain specific SLA modifications requiring review before architecture decisions

- **Vendor Dependency**: Convera operates as a critical external integration point for FX Draft services; SLA changes may impact performance constraints, timeout definitions, or throughput guarantees that affect system design

- **No Breaking Changes Indicated**: Page notes updates rather than deprecations, suggesting backward compatibility; however, SLA changes could introduce new rate limits or availability windows affecting retry logic and fault tolerance patterns

- **Documentation Reference**: Forms 9182/9183 serve as system contracts; architects should review revised "What's Changed" sections to understand modified operational boundaries before designing enhancements or integrations

- **Support Channel**: Client Support Services (1-888-889-7878 Opt 1, support@central1.com) is the escalation path for SLA interpretation questions during design validation