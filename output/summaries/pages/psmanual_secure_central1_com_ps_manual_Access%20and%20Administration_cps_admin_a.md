# CPS Admin Troubleshooting Summary for Solutions Architect

- **Scope**: Documents login failure modes, password reset procedures, and application access issues for the CPS Admin system, with references to 2-step security token and Client Centre user management.

- **Account Lockout Mechanism**: Login attempts are tracked cumulatively across time (not just within a session)—7 consecutive failed attempts trigger a 30-minute lockout regardless of when attempts occur, requiring clarification on lockout state management and reset logic.

- **Password Reset Role Hierarchy**: Two distinct user classes with asymmetric reset capabilities—CPS Admin Security Officers (reset via provincial central only, in writing) cannot self-service or reset peer passwords; Client Centre Users reset via Security Officer action through User Management application (Section 5.3).

- **Two-Tier User Management**: CPS Admin has its own user management component separate from Client Centre User management, creating two independent authorization domains; applications may have their own tertiary user management layers requiring triple-setup validation.

- **Application Authorization Model**: User access is role-based per application; successful Client Centre authentication is prerequisite but insufficient—users must be explicitly provisioned in each target application's user management component or face access errors.

- **Distributed Administration**: Password reset for Security Officers routes through provincial central entities (not in-system), indicating federated governance; integration point between central authorization and local CPS Admin instances.

- **Error Resolution Dependencies**: Application access failures may stem from three causes: user provisioning gaps, application-level user setup errors, or application availability—architects must design diagnostics to distinguish between authorization tier failures.