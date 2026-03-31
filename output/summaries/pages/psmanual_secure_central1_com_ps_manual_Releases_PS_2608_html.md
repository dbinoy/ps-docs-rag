# PS Release 26:08 (March 30, 2026) Summary

- **Release scope**: Minor update to Enterprise Fraud Management (EFM) module, specifically bill payment adjudication workflows in Decision Mode

- **Primary change**: Section 8.10 documentation revised to clarify bill payment adjudication procedures within the EFM decision engine—indicates process logic or UI/UX modifications to how fraud decisions are rendered for bill payment transactions

- **Affected transaction type**: Bill Payments specifically flagged as the electronic transaction category impacted; suggests EFM rules, thresholds, or decision routing may have changed for this payment type

- **Decision Mode dependency**: Update targets Decision Mode functionality—architects should understand this is an interactive fraud analyst workflow component, not automated rule-based processing; changes may affect analyst workload, case routing, or case attributes

- **Documentation-only update**: Release appears to be instructional clarification rather than API/schema changes; however, underlying EFM business logic or decision tree for bill payments may have been modified upstream

- **No breaking changes indicated**: Framing as "update to instructions" suggests backwards compatibility maintained; safe for existing implementations but analysts will require training on new adjudication procedures

- **Support escalation**: Direct client support contact provided (1-888-889-7878 Opt 1, support@central1.com)—indicates potential for customer questions on EFM decision behavior post-release