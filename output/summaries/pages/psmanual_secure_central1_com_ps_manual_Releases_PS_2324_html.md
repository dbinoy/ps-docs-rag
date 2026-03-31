# PS Release 23:24 (October 5, 2023) Summary

- **Overview**: Royal Bank of Canada updated currency submission policies and handling procedures for discrepancy claims and unfit/contaminated currency; documentation reflects these changes and replaces "secure site" terminology with "Client Centre."

- **Key Process Changes**:
  - Discrepancy cash claims now **require armoured car transport only** (registered mail no longer accepted at any RBC cash centre)
  - Unfit US notes acceptable as regular notes if full bill present and value discernible
  - Non-US foreign currency that is contaminated, mutilated, unfit, or out of circulation **must be rejected**

- **Financial Thresholds & Constraints**:
  - Contaminated/mutilated US notes: minimum shipment value **$100 USD**, minimum processing fee **$50 USD** (variable based on submission amount)
  - Foreign currency bank notes valued **≤$0.50 CAD** and all foreign coins rejected
  - $10 Frontier Series polymer notes (2013 issuance) reclassified as unfit

- **Documentation Updates**: Sections 10.5, 10.6, 11.3, 11.7, 11.9, and 12.1 modified to reflect new submission routing, fitness criteria, return minimums, and foreign note acceptance rules

- **Integration Point**: Currency ordering and discrepancy handling workflows depend on RBC cash centre submission policies; transport method selection (armoured car vs. mail) is now a hard constraint in operational logic

- **Architect Consideration**: Any enhancement to currency handling modules must validate submission methods against transport type requirements and enforce geographic/currency-specific acceptance rules (US vs. non-US handling differs significantly)