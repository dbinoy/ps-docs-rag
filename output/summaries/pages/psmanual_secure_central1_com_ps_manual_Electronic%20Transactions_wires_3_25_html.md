# Summary: Recalling, Tracing, and Amending Wires

- **Overview**: Documents the post-approval lifecycle for outgoing wires—specifically trace, recall, and amendment request workflows for approved wires (including future-dated) that cannot be directly cancelled in the Wires application.

- **Key Constraint**: All wire operations (trace, recall, amendment) are processed on a best-efforts basis and are non-guaranteed. Once released by Central 1, success depends on receiving institution voluntary cooperation; some foreign jurisdictions have non-return policies. This must be communicated prominently in any UX enhancements.

- **Request Types**: Four distinct request types with different outcomes—Trace (status/cancellation), Recall (fund return), Amendment (metadata correction), Compliance (documentation hold), and Fraud Recall—each with unique processing logic and fee structures.

- **Two-Path Request Architecture**: Requests to participating Wires institutions are resolved peer-to-peer (direct contact between FIs); requests to non-participating institutions route through ServiceNow or Form 1917 submission to Central 1 as intermediary. This dual-path design requires conditional routing logic.

- **ServiceNow Integration**: Primary submission channel via Client Centre → Applications → ServiceNow → Service Catalogue → Electronic Payments. System generates ticket numbers, tracks request state, and Central 1 updates tickets with results. Manual Form 1917 fallback only when ServiceNow unavailable.

- **Financial & FX Impact**: Recalled funds return less fees; subject to foreign exchange gains/losses (FX rate at recall date for non-participating institution wires). Fees charged regardless of recall success. Different fee schedules for Class A credit unions (Form 2725) vs. other clients (via Account Executive).

- **Data Fields & State Transitions**: Wire Details section captures common metadata across all request types; "Reason for Trace or Recall" field used for future-dated cancellation indication. Approved future-dated wires can only be cancelled via trace request. Amendment requests fail silently if receiving institution rejects or already processed wire.