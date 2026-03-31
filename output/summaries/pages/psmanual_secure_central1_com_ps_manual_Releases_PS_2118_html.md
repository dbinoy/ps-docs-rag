# Payment Solutions Release Summary: Version 21:18

- **Release scope**: Mandatory update to Form 1171 (Outgoing Wire Request) effective June 15, 2021, focusing on international wire processing requirements.

- **Key regulatory constraint**: Intermediary Financial Institution Information Section is now mandatory for all outgoing wire transfers destined outside Canada; domestic wires are exempt from this requirement.

- **Updated data structure**: Form 1171 Intermediary Financial Institution Information Section now has revised completion instructions—architects must ensure validation logic enforces mandatory field population for cross-border transactions.

- **Integration point**: This change affects wire origination workflows; systems must implement conditional validation that triggers intermediary institution data collection based on destination country/region validation.

- **Data flow impact**: Wire requests must now capture and validate intermediary financial institution details before submission for cross-border transfers; this adds a data collection gate in the wire initiation process.

- **Backward compatibility consideration**: Existing wire request processing logic must be updated to enforce mandatory field rules; legacy wire templates or APIs may require schema updates.

- **Support dependencies**: Client Support Services (1-888-889-7878 Option 1, support@central1.com) is the escalation point for implementation questions or compliance clarifications.