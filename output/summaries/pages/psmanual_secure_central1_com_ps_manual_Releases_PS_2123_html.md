# PaymentStream AFT v21.23 Release Summary

- **Release scope**: June 30, 2021 update introducing scheduled notification functionality for PaymentStream AFT (Automatic File Transfer) pending task workflows and UI revisions across three user guides.

- **Key feature**: Scheduled email notifications for pending tasks—delivers three consolidated daily digests to approvers instead of per-action notifications. Requestable via ServiceNow ticketing by financial institutions and originators on behalf of Data Entry Automatic Release (DEAR) originators.

- **Affected data flows**: Approval workflow notifications; impacts task pending state email distribution logic in the AFT system.

- **UI/UX changes**: New "Match" field added to search criteria sections across Automatic Release, Manual Release, and File Upload AFT modules. Updated figures: 2.8, 2.23, 2.28, 6.4, 6.6, 6.8 (Auto Release); 7.4, 7.6, 7.8 (Manual Release); 5.2, 5.5 (File Upload).

- **Integration dependencies**: Feature request workflow routes through ServiceNow ticketing system and Central 1 Support; configuration managed at financial institution level.

- **Documentation artifacts**: Three user guides (doc IDs 5598, 5599, 5600) require version alignment; Section 1.4 and 12.1 updated in AFT Volume originating guide.

- **Architectural constraint**: Notification scheduling is opt-in per institution; requires support ticket submission—not self-service configuration—indicating backend control rather than client-side settings.