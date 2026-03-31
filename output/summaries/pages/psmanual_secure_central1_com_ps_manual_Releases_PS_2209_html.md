# Payment Solutions Release 22:09 Summary

- **Overview**: March 16, 2022 release updating Form 3597 (Country-Specific Guidelines and Instructions) with revised sanctions requirements, payment instruction specifications, and field formatting rules across multiple jurisdictions.

- **Sanctions Framework Changes**: Removed sanctions requirements for 8 countries (Anguilla, Comoros, Dominica, Ecuador, Ghana, Nigeria, Seychelles, Tunisia); added for 4 countries (Ethiopia, Eritrea, Jordan, Kosovo); updated language for Afghanistan, Burundi, Russia, and Ukraine with compliance officer consultation directives and OFAC/Global Affairs Canada references.

- **Data Structure Requirements**: Payment details now use standardized line-based input format (lines 1-4) for structured field mapping, with country-specific schemas including: Tax ID formats (NIT, Cedula, RNC, IIN/BIN), account type codes (/ACC/TYPE CA|SA|current|savings), identification codes (CLABE 18-digit, RIB 24-digit), and purpose-of-payment classifications (EKNP 10-digit for Kazakhstan, XXX 3-digit codes for Uganda/UAE).

- **Mandatory Field Additions**: 16 countries now require "Purpose of Payment" field; Kazakhstan mandates EKNP classification code; Dominican Republic requires account type and phone number; Uganda requires all 4 payment detail lines populated with specific purpose codes (Form 9415 reference); Malaysia makes phone number mandatory for financial transactions.

- **Integration Dependencies**: Form 3597 updates synchronized with Wires application; references external forms (9471 for Kazakhstan EKNP codes, 9415 for Uganda purpose codes); compliance validation requires cross-reference with Global Affairs Canada and OFAC sanctions lists; correspondent bank non-CAD currency transaction filtering required.

- **Validation Constraints**: Strict formatting rules—no spaces in Colombia NIT (TAXID + 10-12 digits), leading zeros mandatory for multi-country ID formats (Dominican Republic 11-digit Cedula, 9-digit passport), Jamaica requires 5-digit Branch/Transit + 9-digit account concatenation for JMD 1M+ Scotiabank payments; Morocco RIB structure: 3-digit bank + 3-digit location + 16-digit account + 2-digit checksum.

- **Architect Considerations**: Payment instruction validation logic must be country-contextual with conditional field requirements (e.g., phone mandatory only for financial payments in Malaysia); sandbox/test data needed for all 16+ updated country schemas; API responses should map line-based input to backend transaction detail records; compliance workflow integration for