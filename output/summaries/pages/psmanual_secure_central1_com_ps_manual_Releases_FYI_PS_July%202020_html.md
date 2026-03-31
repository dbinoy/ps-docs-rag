# FYI – July 2020 Payment Solutions Manual Updates

- **Purpose**: Release notes documenting July 2020 revisions to Payment Solutions Manual documentation, specifically affecting M2M requests and transaction/charge code definitions.

- **M2M Daily Modification Request (Doc 2357)**: Clarified explanations for four M2M request types; architects should review updated definitions when designing M2M-dependent workflows or integrations.

- **Transaction/Charge Code Changes (Doc 3667)**:
  - **Removed codes**: IC (Inter-CU Transfer) and IC (Inter-CU Trans Fee) – systems relying on these codes require deprecation handling and fallback logic
  - **Code mapping update**: OF (Originating AFT OFI) changed from code 43 to code 45 – critical for any integration points that perform code lookups, routing, or validation

- **Data Structure Constraint**: Transaction/charge code changes represent breaking changes to code-to-value mappings; architects must implement migration strategies to prevent processing failures in systems storing or referencing the removed/modified codes.

- **Integration Impact**: Inter-CU transfer functionality was restructured (removal of two IC codes suggests process consolidation); dependent systems processing inter-credit union transfers need architectural review.

- **Support Contact**: Central 1 Client Support Services (1-888-889-7878, Option 1 or support@central1.com) for clarification on implementation details and backward compatibility constraints.