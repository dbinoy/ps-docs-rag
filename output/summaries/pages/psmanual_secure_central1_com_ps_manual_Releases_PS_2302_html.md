# Summary: PS 23:02 Release - ISO 20022 Return Code Definitions

- **Overview**: Introduction of Form 9610 (ISO 20022 Return Code Definitions) to provide standardized return code lookup documentation for wire transfer rejections.

- **Data Flow & Integration Points**: Return codes populate in the "Sender FI to Receiver FI Information" section on two UI pages within the Wires module: (1) Pending Incoming Wires – Details and (2) Received Wires – Details, indicating real-time code display at wire status pages.

- **Code Source & Governance**: Return code definitions derive directly from ISO20022.ORG External Code Sets; the form serves as a published convenience reference, not a custom definition system—architects should assume compliance requirements tied to ISO 20022 standards.

- **Wire Return Processing**: Wire returns now include standardized return codes and/or reason text; architects should expect these fields as mandatory/required in wire return payload structures.

- **Form Structure**: Form 9610 is a lookup/reference document (status: "New"); not indicated as transactional—design should treat it as read-only reference data rather than mutable configuration.

- **No System Architecture Changes Noted**: Release appears to add UI/documentation capability without indicating backend schema modifications, API changes, or new microservice dependencies.

- **Support & Escalation**: Client Support Services (1-888-889-7878, Option 1 or support@central1.com) owns questions—no mention of self-service configuration or admin tools.