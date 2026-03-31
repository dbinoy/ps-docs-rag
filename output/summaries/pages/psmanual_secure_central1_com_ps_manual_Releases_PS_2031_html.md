# Payment Solutions Release 20:31 Summary

- **Release scope**: Documentation update to Payment Solutions Manual covering Interac e-Transfer® Online Administration System (OAS) on September 1, 2020

- **Key update areas**:
  - Section 2.1 (Definitions) revised with new/updated terminology for Electronic Transactions Volume and Interac e-Transfer® OAS
  - Chapter 7 added as new content covering scrubbed email address revocation procedures

- **Critical process**: Email address revocation workflow now formally documented—architects should verify OAS handles email state management and revocation callbacks correctly

- **Data considerations**: Scrubbed/revoked email addresses require state tracking within OAS; integration points likely exist with email validation and transaction blocking logic

- **No breaking changes indicated**: Update appears documentation-focused; however, new revocation chapter suggests possible OAS API/workflow changes that downstream systems (transaction processing, reconciliation) may depend on

- **Support/escalation**: Client Support Services (1-888-889-7878 Option 1 or support@central1.com) owns inquiries—architects should reference this for Interac e-Transfer® OAS behavioral clarifications

- **Architect action item**: Review full Chapter 7 revocation specifications and updated definitions in Section 2.1 to identify integration dependencies before designing any e-Transfer® transaction workflows or email validation enhancements