# Summary: CRA Business Tax Reports and Reconciliation

- **Overview**: Financial institutions in BC and Ontario reconcile CRA business tax bill payments against Central 1 settlement amounts using standardized daily and monthly reports; institutions outside these provinces follow provincial central procedures.

- **Daily reconciliation workflow**: FIs must match BPRS (Bill Payments Remitted Summary) transaction totals to Central 1 settlement amounts, cross-reference rejected items in BPRT (Bill Payments Rejected Transactions) reports, and verify posted amounts in CAS Online align with BPRE/BPRS totals.

- **Key reports and data structures**:
  - **TPRE** (Tax Payment Remitted Transactions): Daily report isolating CRA business tax transactions from general bill payments; sorted by customer account number with item counts and dollar totals
  - **TXMC** (Tax Payments Monthly Billing): Monthly vendor-level billing report showing charges, transaction counts, and dollar amounts per CRA/Hydro-Quebec vendor; sorted by vendor number

- **System dependencies**: TPRE totals roll into BPRS summary figures; settlement data flows from Central 1 via File and Report Exchange; posting verification occurs in CAS Online; BPRT exceptions must be cross-referenced for reconciliation accuracy.

- **Distribution channels**: BC institutions access TPRE via current Bill Payment report file (Bill file); Ontario institutions access via dedicated FTP folder (Bill_Pmt/TPRE_In_Branch_Tax_Remitted); reports generated daily (next business day) and monthly respectively.

- **Critical constraint**: Rejected transactions at Central 1 are excluded from settlement amounts, requiring exception handling logic that cannot assume all submitted items post successfully.