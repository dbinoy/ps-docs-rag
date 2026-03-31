# Payment Solutions Release Summary: Version 22:23

**Overview:**
Release 22:23 (September 16, 2022) introduces a schema modification to the CBS Online User Request process, specifically expanding Form 2513 to capture provincial jurisdiction information.

**Key Points:**

- **Form Update**: CBS Online User Request Form 2513 revised to include a new mandatory or optional province name field—validates user registration/request data against Canadian provincial jurisdictions

- **Data Structure Change**: Schema addition suggests integration with CBS (likely "Central 1 Business Services" or similar back-end system); architects should account for backward compatibility and field validation rules for valid province codes/names

- **Change Type**: Document Library status marked as "Revised," indicating this is a breaking or non-breaking schema change requiring downstream system updates in form processing pipelines

- **No apparent integration points mentioned**, but Form 2513 likely feeds into account provisioning, compliance, or regulatory reporting workflows—architects should verify dependencies on forms processing engine and any downstream systems consuming this data

- **Support/Governance**: Client Support Services manages implementation questions (1-888-889-7878, support@central1.com, Option 1)—suggests staged rollout; confirm implementation deadlines and migration strategy for existing Form 2513 submissions

- **Constraint to Consider**: Provincial field addition may have regulatory/compliance implications for Canadian financial services—verify if this supports KYC, AML, or jurisdiction-based access control logic