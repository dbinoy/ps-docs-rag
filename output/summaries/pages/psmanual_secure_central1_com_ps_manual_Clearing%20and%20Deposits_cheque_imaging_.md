# MICR Cheque Testing Summary

- **Purpose**: Documentation for credit unions to request validation that MICR (Magnetic Ink Character Recognition) encoding on cheques conforms to CPA Standard 006 specifications before production use or to diagnose high rejection rates from automated sorting equipment.

- **Trigger scenarios**: New cheque stock paper, new printer deployment, new vendor engagement, or persistent high cheque rejection rates from sorting equipment indicating readability issues.

- **Process flow**: Credit union submits Form 3600 (MICR Cheque Testing Request) with 10 voided sample cheques per account → Central 1 performs testing → Central 1 emails results confirming pass/fail status; supports batch requests (multiple accounts on single form).

- **Critical constraints**: 
  - MICR must be printed with magnetic ink (not substitute inks)
  - MICR encoded area must have no stamps or additional printing that could interfere with readability
  - These requirements map directly to CPA Standard 006 compliance validation

- **Data handling option**: Form 3600 includes disposition choice—cheques can be returned to credit union or destroyed by Central 1 post-testing (no default implied).

- **Integration dependency**: Central 1 operates the automated sorting equipment that rejects unreadable cheques; MICR testing acts as quality gate before cheque stock enters production circulation to prevent downstream rejections.

- **Related artifact**: Form 3600 is the sole structured request vehicle; no API or digital submission method mentioned in this documentation section.