# FYI – February 2020 Summary

- **Purpose**: Release notes documenting manual updates to Payment Solutions documentation as of February 2020

- **Access Control Policy Change**: New secure site user accounts now have a 15-day activation window (reduced from 30 days) before automatic disablement—affects CPS Admin and Biometric Device Management modules and user provisioning workflows

- **Scope**: Updates span the Access and Administration Volume, specifically the "Policy on Internal Controls to User Management and Secure Site User Management" section, indicating changes to identity and access management procedures

- **Form Update**: Wires Customization Form 6493 (Document ID/Status code: 6493) revised its "Collect Funding Method" section—architects should verify this form's schema and any downstream integrations with wire transfer processing pipelines

- **No Integration Points Explicitly Stated**: Document does not specify which systems consume the Wires Customization form or how the 15-day account disablement triggers downstream workflows

- **Reference Data**: CPS Admin and Biometric Device Management are identified as dependent modules; architects should confirm whether the shortened activation window affects provisioning APIs, audit logging, or account lifecycle management

- **Support Dependencies**: Changes require coordination with Central 1 Client Support (1-888-889-7878, support@central1.com) for clarification on implementation details and rollout impact