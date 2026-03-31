# FX Drafts User Management Summary

- **Purpose**: Documents the two-tier user access model for the FX Drafts application—Client Centre user provisioning followed by FX Drafts-specific permission assignment

- **Two-layer access control architecture**: Initial access granted via User Management system to Client Centre users/security officers, then FX Drafts admins configure granular permissions within the FX Drafts application itself

- **Critical data mapping constraint**: External user IDs created in FX Drafts must exactly match Client Centre user IDs—this is a required synchronization point between systems with no apparent reconciliation mechanism documented

- **Permission administration**: FX Drafts User with admin permissions owns user setup and permission definition; separate from Client Centre user management (see Form 9182 for procedures)

- **Offboarding dependency**: User deletion requires modification/deletion at the Client Centre profile level in User Management system—FX Drafts does not appear to have independent deprovisioning capability

- **Integration points**: Tight coupling between User Management system and FX Drafts application; Client Centre acts as the authoritative identity source

- **Architectural gap**: No documented procedure for handling ID mismatches, sync failures, or orphaned accounts when Client Centre user IDs change or are deleted