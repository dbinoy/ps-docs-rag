# Payment Solutions 20:04 Release Summary (Feb 28, 2020)

- **Overview**: Release documenting updates to counterfeit banknote handling procedures across Currency Volume Ordering System (BC) and Cash Parcel Online Ordering System (Ontario) following RCMP program termination.

- **Key Process Changes**: 
  - Counterfeit notes in *incoming* cash parcels from RBC → return to RBC (not police/RCMP)
  - Counterfeit notes in *deposits* → escalate to local police department only (RCMP no longer accepts); fallback to RCMP only if no local jurisdiction exists

- **Documentation Sections Updated**: Section 6.8 (incoming parcel handling) and Section 9.9 (deposit returns) across both regional systems, indicating parallel manual maintenance across BC and Ontario deployments.

- **Data Structure Change**: Removed "Law Enforcement Receipt Attached" field from document form 2117 (Claim for Discrepancy in Cash/Coin Parcel Received), eliminating downstream tracking/audit trail for law enforcement submissions.

- **Integration Dependency**: RBC cash parcel receipt workflow is a critical touchpoint—architects must ensure return-to-RBC pathways are distinct from historical RCMP forwarding logic to prevent routing errors.

- **Regional Variance**: Dual system maintenance (BC and Ontario) suggests potential for future harmonization or region-specific rule configuration rather than manual documentation duplication.

- **Support Contact**: Client Support Services (1-888-889-7878, Option 1; support@central1.com) owns operational clarifications—relevant for escalation paths in system design.