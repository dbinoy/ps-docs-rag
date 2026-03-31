# Release 24:44 Summary – Payment Solutions Architecture Brief

- **Scope**: Updated routing instructions for Mexican Peso (MXN) incoming wire transfers via Form 3775, specifically the correspondent bank designation used by Citi when originating institutions cannot determine the primary routing path.

- **Routing Rule Change**: Correspondent bank instruction updated from **Banco Nacional de Mexico S.A. (BNMXMXMMCVT)** to **Banco Citi Mexico (CITIMXMMCVT)**—this is a critical data point in wire processing logic that determines the fallback routing path for MXN inbound transfers.

- **Affected Document**: Form 3775 is the control document for MXN incoming wire instructions; any integration consuming these routing rules must reference the revised version to ensure correct correspondent bank resolution.

- **Operational Constraint**: The change applies specifically to scenarios where the sending financial institution *cannot determine* Citi's primary MXN correspondent—this represents an error-handling or fallback pathway in the wire routing workflow.

- **Integration Dependencies**: Systems that validate or construct wire routing instructions, compliance screening workflows, or STP (Straight-Through Processing) rules for MXN inbound transfers may need configuration updates to reference the new correspondent SWIFT code.

- **No Breaking Changes Noted**: The update is a correspondent bank substitution, not a structural change to Form 3775 or the routing instruction schema—legacy integrations should continue functioning with the new bank reference.

- **Support Contact**: Client Support Services (1-888-889-7878, Option 1) owns this change; coordinate with them for downstream system impacts or customer communication requirements.