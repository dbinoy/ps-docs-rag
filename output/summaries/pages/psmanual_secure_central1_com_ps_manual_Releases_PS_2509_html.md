# Summary: PS 25:09 Release – IBAN Support for Mongolia

- **Purpose**: Release notes documenting addition of Mongolia to IBAN-regulated countries list in Form 9252, effective April 1, 2025

- **Regulatory Requirement**: Bank of Mongolia mandates IBAN for all MNT (Mongolian Tugrik) currency wire transfers; payments without valid IBAN will be rejected by correspondent banking system

- **IBAN Structure for Mongolia**: Fixed 20-character format: CC(2) + CheckDigit(2) + BankCode(4) + AccountNumber(12)
  - Example: MN580050099123456789
  - Country code: MN
  - Account number field must be exactly 12 digits (pad domestic 10-digit accounts with leading zeros)

- **Data Integration Point**: Form 9252 (IBAN Countries reference document) requires update in Payment Solutions system to recognize Mongolia as IBAN-mandatory jurisdiction; likely impacts wire validation rules and payment instruction processing for MNT transactions

- **Downstream Dependency**: Client onboarding and beneficiary management workflows must support IBAN collection and validation for Mongolia; missing/invalid IBANs will cause payment failures, necessitating end-client communication and re-submission

- **Critical Constraint**: April 1, 2025 hard cutover date—no grace period for non-compliant transactions; architects should ensure validation logic and error handling are in place before go-live

- **Support**: Client Support Services (1-888-889-7878, Option 1) owns client inquiries regarding IBAN requirements and beneficiary data collection