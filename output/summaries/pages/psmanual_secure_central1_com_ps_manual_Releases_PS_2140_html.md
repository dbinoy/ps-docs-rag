# Payment Solutions Release 21:40 Summary (December 9, 2021)

- **Overview**: This release updates warrant and cheque reimbursement policies for Government of Canada and BC provincial payments, primarily affecting CPA Rule G8 implementation and BC Employment and Assistance cheque claim documentation requirements.

- **Key Rule Change - CPA Rule G8**: Counterfeit Receiver General Warrants are now indemnified up to $1,500 maximum if the financial institution demonstrates recovery attempts before claiming reimbursement; however, materially altered warrants remain unindemnified (critical constraint for validation logic).

- **BC Employment and Assistance Cheque Claims - New Data Requirements**: Claims must now include: original cheque/certified copy/bank RRD with customer signature; reimbursement letter detailing recovery attempts and cashing diligence; two-piece ID proof matching Ministry standards; signature verification between ID and cheque endorsement (expands document validation workflows).

- **Warrant Processing Indemnification Scope**: Credit unions receive indemnification for counterfeit Government of Canada warrants under Rule G8, but material alteration detection remains an exclusion—requires document examination capability to distinguish counterfeits from altered instruments at processing intake.

- **Documentation System Updates**: Three reimbursement request forms updated (IDs: 1294, 1299, 2303) with revised instructions and expanded documentation sections; form 2303 renamed from "Cheques" to "Warrants" indicating potential downstream system/database taxonomy changes.

- **Integration Dependencies**: Changes affect Clearing and Deposits processing (Section 5.5) and Dishonour/Return workflows (Sections 3.1, 7.1, 7.3)—any enhancement must coordinate with cheque validation pipelines, ID verification systems, and indemnification claim processing.

- **Architect Must Know**: Implement conditional indemnification logic based on warrant authenticity classification (counterfeit vs. altered) and maintain audit trail for recovery attempt documentation; design claims submission to enforce all seven new BC cheque requirements before acceptance.