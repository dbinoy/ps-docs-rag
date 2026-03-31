# Payment Solutions 24:31 Release Summary

- **Release scope**: Documentation updates to Deposit Processing workflows effective September 6, 2024, clarifying processing timelines and deposit constraints for Canadian financial institutions.

- **Corporate Capture enrollment timeline**: Business customer enrollment requests submitted to Central 1 require up to 10 business days for processing and activation—critical constraint for integration planning and customer onboarding workflows.

- **Imprest cheque face value constraint**: $3,000 maximum face value applies to Imprest cheques issued by British Columbia Ministry of Social Development and Poverty Reduction or Ministry of Children and Family Development—impacts validation rules in deposit acceptance and clearing logic.

- **Section 5.6 (BC Employment and Assistance Cheques)**: Prior documentation gap corrected; this section now fully specifies provincial cheque handling requirements and must be referenced in cheque validation and routing logic.

- **Section 11.3 (Corporate Capture enrollment)**: Details enrollment request submission mechanics to Central 1—integration point where business customer onboarding depends on external processing queue with defined SLA.

- **No new data structures introduced**: Updates clarify existing constraints rather than define new fields; existing deposit processing schemas remain unchanged.

- **Support contact**: Client Support Services (1-888-889-7878 Option 1 or support@central1.com) handles questions regarding enrollment timelines and cheque acceptance rules.