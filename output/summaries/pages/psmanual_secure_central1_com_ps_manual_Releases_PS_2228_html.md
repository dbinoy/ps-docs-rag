# Summary: Payment Solutions v22.28 Release Notes – Currency Ordering Updates

- **Release scope**: Updates to currency ordering procedures in Cash Services, focusing on new Canadian bank note ordering capabilities and currency trace request handling (November 18, 2022)

- **Key business rule change**: New Canadian bank notes now orderable directly in Cash Services with bundled denominations (100 notes per bundle) instead of previous block-based minimums (10 bundles/block); subject to additional fees

- **Dual-system ordering architecture**: ServiceNow (New Currency and Coin Order System) remains the system of record for standing orders, late orders, and contingency orders; Cash Services handles spot orders for new notes and standard currency—integration between systems required for standing order selections

- **Currency trace request process redesign**: Primary contact is now armoured car service provider for missing shipments at specified delivery locations; Central 1 escalation only required if armoured car service cannot locate order—implies new SLA/escalation dependency chain

- **Documentation updates spanning three functional areas**: Password reset validation (Section 6.5), Cash Services access procedures (Section 5.2), and currency ordering workflows (Chapters 7, 9, 13) indicate potential UI/UX changes and validation rule implementations

- **Integration constraint**: Minimum order threshold removed for new notes (now 1 bundle vs. 10 minimum)—may impact inventory forecasting, fulfillment logistics, and fee calculation engines

- **Support contact dependency**: Client Support Services (1-888-889-7878, Option 1) designated as escalation point—critical for defining SLA and incident management workflows