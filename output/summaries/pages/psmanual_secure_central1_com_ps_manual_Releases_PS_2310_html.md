# Payment Solutions Release 23:10 Summary (May 30, 2023)

- **Overview**: Documentation update to Electronic Bill Payments (EBP) System reflecting UI changes to the EBP Billers Listing Application search results interface and information display workflows.

- **Data Structure Changes**: 
  - `Bill Presentment` column removed from EBP Billers Listing search results page
  - `Vendor # (legacy)` column added with jurisdiction-specific applicability (Ontario financial institutions only)

- **Regional/Compliance Constraints**: `Vendor # (legacy)` field introduction indicates legacy vendor identification maintained for Ontario FIs; suggests regional data model variations or backward compatibility requirements for billers previously onboarded under legacy vendor coding schemes.

- **API/Interface Impact**: Section 5.2 (Viewing Biller Information on Bill Payment Vendor Information) was removed—indicates potential consolidation of biller lookup workflows or deprecation of a separate vendor information endpoint; architects should verify whether this functionality was merged into Section 5.1 or if downstream integrations consuming that endpoint require migration.

- **Integration Point**: EBP Billers Listing Application operates as a search/query interface for biller master data; changes suggest updates to underlying biller metadata schema or search index that may affect third-party integrations or internal billing UI layers consuming biller lookup APIs.

- **Support & Documentation Baseline**: Client Support contact (1-888-889-7878, support@central1.com) provided; release tied to prior notification on central1.com—recommend reviewing prerequisite "Upcoming Updates to EBP Billers Listing Application" communication for full context on API/schema deprecations.