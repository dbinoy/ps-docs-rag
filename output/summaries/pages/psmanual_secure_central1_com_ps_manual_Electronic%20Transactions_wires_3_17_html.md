# Bank to Bank Wire Creation - Technical Summary

- **Scope**: Step-by-step procedural documentation for creating outgoing wires that credit receiving financial institutions (not individual customers) via the Wires application, covering field completion, validation, and confirmation workflows.

- **Financial Institution Identification**: Wire routing requires SWIFT code, transit number, or ABA number lookup; alternatively, Advanced Search by name/address. Search results must be selected from system database, indicating integration with a Financial Institution Directory or master reference table.

- **Multi-Currency Support**: Wire currency selection varies by beneficiary institution; non-CAD/USD currencies trigger real-time foreign exchange rate calculation (including Central 1 rate + customer FX spread) with countdown-expiring quotes requiring explicit confirmation before transaction completion.

- **Intermediary Bank Requirement**: Non-domestic currency wires (e.g., GBP to France) or certain beneficiary institutions mandate intermediary bank selection from dropdown or manual search; intermediary selection is mandatory for transaction progression when applicable.

- **Geopolitical Compliance Controls**: Destination country validation against prohibited/sanctioned/high-risk lists; prohibited countries block wire progression with error message post-submission, while warning messages for tax havens/high-risk destinations are best-effort (not guaranteed).

- **Canadian Domestic Wire Features**: Wire Priority (Regular vs. High for Lynx participants only) and Future Dated scheduling (up to 14 days) are conditional sections displayed only for CAD-denominated wires to Canadian beneficiaries; both require authorized user approval and incur additional processing fees.

- **Approval & Cancellation Workflow**: All wires require approval before processing (Chapter 22 dependency); future-dated wires can only be cancelled via trace request to Central 1 by 2:15 PM PT the business day prior; post-release recalls/amendments are best-effort with no guarantee of receiving institution compliance.

- **Payment Metadata & Compliance**: Payment Details section (Related Reference Number) and mandatory Sender FI to Receiver FI Line 1 field carry wire metadata through payment rails; architects must reference Prohibited Remittance Content Procedure to enforce content restrictions on remittance information fields.