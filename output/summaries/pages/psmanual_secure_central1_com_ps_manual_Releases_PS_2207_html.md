# PS 2207 Release Summary (March 14, 2022)

- **Release scope**: Maintenance update addressing obsolete payment instruments and documentation revisions for bill payment reversal workflows across Electronic Bill Payments and CRA Business Taxes modules.

- **Deprecated billers removed from Central 1 system**: Three prepaid card products deactivated (Biller codes 3985, 3936, 8204), requiring downstream systems to validate against updated biller master data and prevent routing to invalid payment channels.

- **Bill Payment Reversal Request process** (Form 1793): Documentation updated across two functional areas (Section 12.2 Electronic Bill Payments, Section 8.2 CRA Business Taxes), indicating this is a critical shared artifact; architects should verify Form 1793 schema/fields are consistently referenced in reversal request APIs and ServiceNow integration points.

- **ServiceNow integration dependency**: Same-day reversal requests processed through ServiceNow platform for CRA module—architects must understand ticketing workflows, SLA requirements for same-day processing, and potential integration gaps between payment system and ITSM platform.

- **Document library governance**: Form 1793 marked "Revised"—suggests version control mechanisms exist for payment forms; verify artifact versioning strategy and whether legacy form versions require backward compatibility in payment validation logic.

- **Support escalation path**: Client Support Services (1-888-889-7878, support@central1.com) is owner of user-facing reversal request handling; architects should clarify SLAs and what triggers escalation to support vs. automated processing.