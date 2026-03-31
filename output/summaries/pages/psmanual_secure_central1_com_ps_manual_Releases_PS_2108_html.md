# Payment Solutions Release 21:08 Summary

- **Purpose**: Documentation update to Deposit Processing Part clarifying identification requirements for non-members in BC Benefits Cheques processing under the BC Benefits Cheques Indemnity Agreement.

- **Key Process Change**: Social Development no longer uses internal ID Schedule for non-member identification verification; instead references external Government of British Columbia Identification Requirements documentation as the authoritative source.

- **Non-member Identification Flow**: Non-members lacking acceptable identification must physically visit a Ministry of Social Development location to request acceptable ID documentation be sent to their chosen financial institution—placing verification responsibility on the member/depositor rather than the payment processor.

- **Documentation Reference**: Direct integration dependency on Government of British Columbia's published Identification Requirements policy; this is an external, evolving reference that Payment Solutions documentation now points to rather than maintaining internally.

- **Affected System Component**: Clearing and Deposits Volume subsystem, specifically Section 5.6 (BC Employment and Assistance Cheques) in the Deposit Processing Part.

- **No Technical Data Structure Changes Noted**: Update appears to be procedural/policy clarification rather than schema, field, or code modifications, but architects should verify if downstream validation rules or user workflows require adjustment based on the external BC government requirements.

- **Support Escalation**: Client Support Services (1-888-889-7878, Option 1) handles implementation questions—suggest confirming validation logic alignment during design reviews.