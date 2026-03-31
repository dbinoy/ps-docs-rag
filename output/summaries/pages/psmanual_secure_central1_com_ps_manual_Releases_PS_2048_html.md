# Payment Solutions Release 20:48 – December 11, 2020 Summary

- **Purpose**: Documentation updates for expanded CEBA (Canada Emergency Business Account) program supporting increased loan amounts ($20K additional for existing recipients, $60K cap for new applicants) with interest-free terms and conditional forgiveness (up to 33%) if repaid by December 31, 2022.

- **Key Process Changes**: 
  - New settlement reconciliation workflow added (Section 3.6: Settlement of CEBA Loan Repayments)
  - New cancellation workflow introduced (Chapter 3)
  - Upsizing capability added for funded CEBA loans with new categorization framework (Sections 2.5, 5.4)

- **System Integration Points**: Updates span multiple platforms—MemberDirect, Forge, and ServiceNow—indicating multi-tenant architecture; ServiceNow workflow handles CEBA repayment form submission with strict end-of-day cutoff constraints for reporting.

- **Critical Data Structures**: Form 9140 used for application procedures; repayment forms processed through ServiceNow; loan repayment settlement records require reconciliation; fraud flagging and late admin fee reporting now trackable in FAQ section.

- **Operational Constraints**: Loan repayment reports have time-bound submission windows (end-of-day cutoffs on specified dates); forgiveness eligibility tied to December 31, 2022 repayment deadline; fraud detection and late reporting handling now documented requirements.

- **Support Dependencies**: Client Support Services (1-888-889-7878, Option 2) and digitalbanking_support@central1.com as escalation points indicate business rule validation should be coordinated with support team.