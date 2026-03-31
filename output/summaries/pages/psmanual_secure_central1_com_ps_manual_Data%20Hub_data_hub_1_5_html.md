# Data Hub Login Process Summary

- **Purpose**: Provides step-by-step authentication procedures for accessing the Data Hub Payments Dashboard through the Client Centre portal at https://clients.central1.com

- **Authentication Architecture**: Multi-step federated login requiring Client Centre credentials with mandatory Microsoft Online Services authentication using Client Centre ID with @central1client.com domain suffix (e.g., testuser@central1client.com)

- **Key Integration Point**: Data Hub depends on Client Centre as the identity provider and gateway; users cannot access Data Hub directly but must route through Client Centre's Applications menu (Applications > Payments Dashboard)

- **Session Management & Constraints**: 
  - Login experience varies based on browser history, cookies, and previous authentication state
  - Initial logins, cookie deletion, or incognito/private browsing modes trigger username pre-prompts
  - System supports account selection from previous sessions on "Pick an account" page for returning users

- **Two Documented Login Scenarios**: Scenario 1 requires "Use another account" selection before credential entry; Scenario 2 uses direct Client Centre ID submission—both conclude with "Stay signed in" confirmation, indicating persistent session capability

- **Troubleshooting Pattern**: Documentation explicitly recommends private/incognito sessions and strict adherence to @central1client.com domain format as primary diagnostic steps, suggesting credential format mismatches are common failure points

- **Application Grouping Model**: Applications are categorized by type (Admin & Support, Payments) with favorite-starring capability, indicating a hierarchical application discovery model architects should account for when adding new integrations