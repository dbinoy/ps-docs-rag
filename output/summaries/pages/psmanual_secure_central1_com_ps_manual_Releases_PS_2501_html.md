# PS 25:01 Release Summary (January 2, 2025)

- **Release scope**: Documentation update to Country-Specific Guidelines and Instructions (Form 3597) effective January 2, 2025, with no apparent system code changes indicated

- **Key update**: Addition of Kuwait payment processing guidance, specifically integrating Purpose of Payment Codes (Form 10061) into Kuwait payment instruction workflows

- **Data structure impact**: Form 3597 now includes a new reference dependency on Form 10061 for Kuwait transactions—architects should verify this form's code mappings and validation rules are available in payment processing systems

- **Compliance/regulatory**: Kuwait Purpose of Payment Codes represent country-specific regulatory requirements; payment systems must validate outbound transactions to Kuwait against this code set during payment instruction generation

- **Integration dependency**: Payment instruction generation modules targeting Kuwait require access to Form 10061 code tables; this likely impacts data validation pipelines and payment instruction templates

- **No technical migration noted**: This appears documentation-driven; verify whether underlying payment processing rules engines, code tables, or form mappings require updates independent of documentation

- **Support/governance**: Changes managed through Client Support Services (1-888-889-7878 Option 1 or support@central1.com)—confirm change control process and whether downstream integrations require notification