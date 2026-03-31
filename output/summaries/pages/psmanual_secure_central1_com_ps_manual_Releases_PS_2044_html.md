# Payment Solutions Release Summary: November 6, 2020

- **Overview**: Documentation update release (v20:44) reflecting decommissioning of biometric authentication devices and streamlined user management procedures across PaymentStream Direct and related systems.

- **Authentication Framework Changes**: Introduction of new security definitions—2-step security, 2-step security token, and step-up authentication—indicating shift from biometric to token-based multi-factor authentication model.

- **User Management Role Definitions**: Updated procedures for granting PaymentStream Direct access to three distinct user types: Secure Site Users, existing CPS Admin Security Officers, and new CPS Admin Security Officers, with consolidated documentation references to CPS Admin Application Part and User Management Part.

- **Documentation Consolidation Pattern**: Removal of modify/delete user procedures from PaymentStream Direct docs signals centralization of user lifecycle management in dedicated CPS Admin Application and User Management modules—architects should treat these as authoritative sources for access control logic.

- **Affected Systems and Integrations**: Changes span multiple components—PaymentStream Direct, Corporate Capture, Treasury Connect, Campaign Manager, and MemberDirect Online Voting—indicating user management framework applies across heterogeneous product suite with unified authentication/authorization model.

- **Role-Based Access Control Scope**: Document updates to "User Role Combinations" (status 5936) suggest explicit matrix-based role constraint definitions; architects must understand these combinations when designing access control policies or role hierarchies.

- **Phased Rollout**: Documentation updates occurring in phases; implementation of underlying system changes (biometric removal, token-based auth) may precede or lag documentation, creating potential version/compatibility constraints for enhanced integrations.