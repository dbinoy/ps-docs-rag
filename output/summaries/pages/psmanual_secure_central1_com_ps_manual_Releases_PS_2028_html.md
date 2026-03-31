# PS 2028 Release Summary (August 24, 2020)

- **Purpose**: Establishes mandatory CEBA (Canada Emergency Business Account) loan administration fee reporting requirement for financial institutions to Central 1 via ServiceNow

- **Key Process**: Financial institutions must report loan administration fees quarterly using the "CEBA Program – Loan Administration Fee Report" tool in ServiceNow; timing tied to quarterly cycles

- **Regulatory Constraint**: Reporting is a compliance requirement—not optional; institutions must ensure timely quarterly submissions to avoid regulatory gaps

- **Documentation Update**: CEBA procedures document (Central 1 Facilitated CEBA Application Procedures – Quick Reference Guide, v9140) was revised to include Chapter 6 detailing the fee reporting workflow

- **Integration Point**: ServiceNow is the system of record for fee submissions; this implies data flows from originating loan systems into ServiceNow for aggregation and reporting to Central 1

- **Data Structure Implication**: Loan administration fee data must be structured to support quarterly aggregation and Central 1 reporting format (specific schema/fields not documented on this page)

- **Support/Governance**: Client Support Services (1-888-889-7878, Option 2) owns field questions; digitalbanking_support@central1.com for technical issues

- **Architect Consideration**: Any loan origination or administration system enhancement must account for quarterly fee extraction and ServiceNow integration; timing and data reconciliation are critical to compliance