# Summary: Troubleshooting and Best Practices for Client Centre Users

- **Purpose**: Diagnostic and procedural guide for resolving Client Centre login failures and application access issues, with best practices for secure application bookmarking and favorites management.

- **System Synchronization Constraint**: New user accounts require up to 45 minutes for back-end system synchronization before first login attempt; this represents a critical timing dependency in the user provisioning workflow.

- **Account Lockout Logic**: Accounts automatically lock for 30 minutes after 7 consecutive failed password attempts, with lockout persistence across multiple days—architects must account for this in authentication retry logic and user support workflows.

- **Browser Cookie Dependency**: Client Centre session management relies heavily on persistent browser cookies; cookies can be corrupted or stale when users share computers, requiring private/incognito mode as a diagnostic workaround and indicating potential session state issues.

- **Application Access Patterns**: Applications have distinct landing pages (referenced in bookmarking guidance) and require proper session context; bookmarks created mid-session fail, suggesting stateful application architectures with session validation at entry points.

- **Integration Point - Password Reset Workflow**: User login troubleshooting integrates with password reset functionality (Section 6.6), indicating a tightly coupled identity management system where password reset is a primary remediation path.

- **Two-Step Authentication Integration**: 2-step security token issues are delegated to a separate documentation reference ("2-Step Security Part"), indicating modular authentication architecture with independent troubleshooting procedures.

- **Favorites Feature Architecture**: The "My Favourites" functionality requires distinct back-end storage (users check applications, system persists state) separate from browser bookmarking, suggesting user preference persistence in the Client Centre database.