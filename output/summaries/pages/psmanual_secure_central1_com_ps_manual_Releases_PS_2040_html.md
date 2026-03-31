# Payment Solutions 20:40 Release Summary

- **Overview**: October 26, 2020 release streamlined the FTP User Request (Form 2010) approval workflow to reduce provisioning time and strengthen firewall security controls for new IP address additions to Central1's infrastructure.

- **Primary Change**: Addition of mandatory "Reason for Change" field in the Direct Connection section of Form 2010, enabling better risk assessment and audit trails for firewall rule modifications.

- **Process Improvement**: Lean approval process redesigned to mitigate risk exposure—architects should assume downstream firewall provisioning workflows now have stricter validation gates tied to the reason field.

- **Data Structure Impact**: Form 2010 schema modification adds a required field in Direct Connection section; any system consuming or generating this form must support the new field to maintain compatibility.

- **Integration Point**: FTP user provisioning process integrates with Central1's firewall management system; the "Reason for Change" field serves as a control input for automated or manual firewall rule deployment.

- **Operational Constraint**: New IP address onboarding now has explicit documentation requirements; architects designing self-service or programmatic user request systems must enforce this field as mandatory.

- **Support & Governance**: Client Support Services (1-888-889-7878, Option 1 or support@central1.com) is the approval authority; escalation paths and SLAs should be validated before designing dependent systems.