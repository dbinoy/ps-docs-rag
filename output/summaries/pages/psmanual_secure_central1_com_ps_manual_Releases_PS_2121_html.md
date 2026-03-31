# PS 21:21 Release Summary (June 21, 2021)

- **Scope**: Correction to routing instructions for USD incoming wire transfers via Form 2606 (Beneficiary Bank Section)

- **Technical Change**: SWIFT BIC code updated from `CUCCATTVAN` (incorrect) to `CUCXCATTVAN` (correct) for Central 1 as the beneficiary bank

- **Affected Document**: Form 2606 (US Dollar Incoming Wires routing instructions) in the Document Library—marked as "Revised"

- **Integration Point**: This SWIFT BIC is a critical routing identifier used by upstream payment networks and correspondent banks to direct incoming USD wire transfers to the correct Central 1 entity; systems consuming this form must be updated to reflect the corrected code

- **Data Structure**: SWIFT BIC field in Beneficiary Bank Section must validate against the correct `CUCXCATTVAN` code; legacy systems may have cached the incorrect `CUCCATTVAN` value

- **Constraint**: Any existing wire routing rules, payment rails configuration, or reconciliation logic that reference the old BIC code will require remediation to prevent routing failures or settlement mismatches

- **Support Contact**: Client Support Services (1-888-889-7878 Option 1 or support@central1.com) for clarification on implementation scope and cutover timing