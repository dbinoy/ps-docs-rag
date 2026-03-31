# Summary: 14 Considerations for Outgoing Wires

**Overview:** Documentation of requirements, constraints, and compliance controls for international outgoing wire processing through Central 1's Wires application, covering IBAN validation, country-specific rules, sanctions screening, and fraud detection.

**Key Concepts & Processes:**
- **IBAN Validation**: Mandatory for IBAN-regulated countries (determined via Form 9252); Wires validates format/length but **cannot verify correctness** and does not prevent submission of invalid IBANs—downstream fees fall to sender
- **Country-Specific Requirements**: Dynamic notification system displays payment codes and documentation requirements (government ID, wire purpose, etc.) based on destination country at Payment Details entry; notifications are best-effort only (see Forms 3597-10130 for 20+ country code mappings)
- **Wire Status Lifecycle**: Approved → Scanned → Frozen (during scanning) → Pending/Sent/Under Investigation/Cancelled; status transitions tied to compliance outcomes, not application logic
- **Intermediary Financial Institution Processing**: Once forwarded by Central 1, transaction control transfers to intermediary; fee deduction and currency conversion rates are unknown and uncontrollable; recall/amendment requests are best-effort with no guarantee

**Integration Points & Dependencies:**
- **Enterprise Fraud Management (EFM) System**: Monitors approved wires asynchronously; alerts change status to Pending without user notification; authorized EFM users access investigation details via separate Enterprise Fraud Management Part (not visible in Wires app)
- **Sanctions Screening**: Automated scanning against Canadian lists + receiving bank's country lists + OFAC (for US-routed wires); frozen status triggers 1-business-day confirmation window; matched wires escalate to "Under Investigation" and Central 1 Compliance + customer security departments
- **PCMLTFA Compliance**: Information disclosure on reported/investigated transactions is prohibited; no user/customer alerts for frozen/pending status per PCMLTFA restrictions

**Critical Constraints for Architects:**
- Wires application **not connected to customer banking systems**—internal reconciliation required for fraud cancellations
- **No wire recall guarantee** once released; receiving institution voluntary return only
- Funds held at Central 1 during frozen/investigation status; customer debited but funds unavailable
- Best-effort notifications (country warnings, IBAN validation, EFM status) create incomplete visibility—application assumes external compliance responsibility