# Payment Solutions 20:42 Release Summary

- **Release scope**: Introduction of Form 9252 (IBAN Country List) as a new standalone form, decoupling IBAN regulatory data from the Money Transfer System (MTS).

- **Key concept**: IBAN Country List provides a reference database mapping International Bank Account Number (IBAN) regulations to supported countries and their corresponding IBAN code formats—previously accessible only through MTS.

- **Data structure**: Form 9252 contains country-level IBAN metadata including country identifiers and IBAN code information; structure and required fields not specified in release notes.

- **System dependency eliminated**: This change removes a direct user dependency on MTS for IBAN lookups, suggesting Form 9252 may serve as a lighter-weight reference service or API endpoint independent of full MTS functionality.

- **Integration consideration**: Architects should verify whether Form 9252 replaces MTS IBAN lookups entirely or operates in parallel; bidirectional data sync requirements between systems should be clarified.

- **Constraints/scope gaps**: Release notes do not specify IBAN validation rules, code formats by country, update frequency for regulatory changes, or API specifications for programmatic access.

- **Support contact**: Client Support Services (1-888-889-7878, Option 1, or support@central1.com) for implementation questions and known issues.