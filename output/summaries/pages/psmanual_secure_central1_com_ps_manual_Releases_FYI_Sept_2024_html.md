# FYI – September 2024 Summary

**Overview:** Documentation of Payment Solutions Manual updates effective May 31, 2024, primarily addressing service decommissioning and clarifications to existing processes.

**Key Updates:**

- **Interac® Online (IOP) Decommissioning:** IOP service was officially decommissioned effective May 31, 2024. All references removed from the manual; File Specifications document 6275 marked obsolete. This eliminates an integration point for online payment authentication and requires clients to migrate to alternative payment methods.

- **Cheque Return File Specifications (Form 6280):** Added to Online Return System Document Library under Section 1.4 (Clearing and Deposits Volume). Architects should reference this specification when designing or maintaining cheque return processing workflows and file exchange mechanisms.

- **Currency Ordering Authorization Requirements:** Clarified the authorization thresholds for four request types—limit creation, standing order creation, location creation, and address change requests. Architects must understand these distinct authorization workflows when designing approval chains or validation logic in currency ordering systems.

- **ORS Integration Point:** Online Return System remains active and document-driven; the addition of Form 6280 specifications indicates structured data exchange requirements for cheque returns that must be incorporated into system interfaces.

- **Support & Governance:** Client Support Services (Central 1) is the primary escalation path for clarifications; indicates potential dependencies on external governance for specification changes or service decommissioning timelines.