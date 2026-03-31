# Summary: Stop Payment Requests for PADs

- **Purpose**: Enables Payors to prevent unauthorized PAD debits by requesting financial institutions apply stop payments, with returns processed via code 903 (Payment Stopped/Recalled) within one business day.

- **Key Process Flow**: Payor completes Form 3386 (Stop Pre-authorized Debit Request) → Financial institution enters stop payment into banking system → System matches incoming AFT against stop payment register → If matched, returns PAD as code 903 to originating FI.

- **Critical Business Rule**: Stop payment is **amount-specific**—only effective if PAD amount exactly matches Form 3386 amount; different amounts bypass the stop payment and post to account. No fuzzy matching logic.

- **Stop Payment is Supplementary, Not Replacement**: Cannot substitute for direct Payor-to-Payee agreement cancellation; must be used *in addition to* formal PAD cancellation notification to prevent liability exposure.

- **Integration Dependencies**: 
  - Form 3386 as authoritative stop payment instruction document (must be signed and retained)
  - Banking system's PAD stop payment capability is prerequisite (feature not universal)
  - Online Return System (ORS) required for processing code 903 returns to originating FI
  - Real-time matching against incoming AFT file from Central 1

- **Architectural Constraints**: One business day SLA for return processing; stop payment mechanism operates at financial institution banking system layer, not centralized platform layer.

- **Data Field of Note**: Code 903 (Payment Stopped/Recalled) is mandatory return code; no alternative codes documented for stop payment scenarios.