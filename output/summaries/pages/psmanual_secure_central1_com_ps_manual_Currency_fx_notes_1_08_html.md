# Summary: Currency Notices on FX Notes

- **Purpose**: Documents the user-facing notice system for FX Notes, enabling admins to communicate currency availability updates and critical information to dashboard users.

- **Two operational modes**: 
  - **View mode**: End users see notices in the "Important Information" section on FX Notes home page (passive consumption)
  - **Post mode**: FX Notes Managers access Administration > Important Posts to create and publish notices (active management)

- **Notice scope**: Notices can be institution-specific (optional filtering by institution entity) or broadcast system-wide, suggesting a multi-tenant architecture where notices may apply to a subset of institutions.

- **Data flow**: Admin creates notice via form input (institution selection + content) → Save action persists to backend → Notice renders on Dashboard and home page Important Information section (no apparent approval workflow).

- **Access control dependency**: Role-based access restricted to "FX Notes Managers" for posting; implies authentication/authorization layer validates permissions before exposing Administration menu.

- **No versioning or audit trail mentioned**: Current documentation does not specify notice edit/delete capabilities, expiration logic, or historical tracking of posted notices—potential gaps for compliance or rollback scenarios.

- **Integration constraint**: Notice system appears isolated to FX Notes dashboard UI; no mention of notification channels (email, API webhooks) or downstream system impacts, limiting reach beyond active application users.