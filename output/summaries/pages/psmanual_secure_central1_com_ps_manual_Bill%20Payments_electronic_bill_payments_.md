# Electronic Bill Payment Reversals and Trace Requests – Architecture Summary

- **Purpose**: Documents procedures for cancelling bill payment transactions (reversals) and initiating payment inquiries/adjustments (trace requests) through Central 1's payment processing system.

- **Key Process Rule**: Reversal requests must be submitted same-day before biller-specific deadlines (4:00 PM PT standard, 2:00 PM PT for Community Visa 650); Central 1 can only reverse if it holds the FI's e-bill database or payment is pre-uploaded before deadline. Ontario FIs using batch file uploads cannot use reversal service.

- **System Constraints & Exclusions**: Three billers reject reversals (Vancity Visa 28, Vancity Com. Inv. Bank Visa 274, International Transfers 13364); all CRA billers reject same-day reversals (full list external); reversals incur service charges per Form 2725.

- **Data Flow Integration**: ServiceNow is primary submission channel for reversal requests (fallback: Form 1793); OLT (Online Tracing System) is primary channel for trace requests and biller-initiated adjustments; financial institutions generate BPCV and BPRE reports to resolve customer inquiries before escalation.

- **Critical Dependencies**: Central 1's electronic bill payments database must be current and synchronized; reversal processing depends on payment upload timing relative to deadline; OLT and ServiceNow ticket systems must maintain bidirectional notification of outcomes.

- **Architect Must Know**: FI account credit is manual post-reversal and not automatic; reversal success is transaction-level only (Central 1 system); biller-initiated trace requests bypass OLT and are entered directly by Central 1.