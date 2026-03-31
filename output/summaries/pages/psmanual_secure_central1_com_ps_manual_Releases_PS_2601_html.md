# Payment Solutions Release 26:01 Summary

- **Release scope**: Updated wire transfer documentation and regulatory compliance for six Central African countries (Cameroon, Central African Republic, Chad, Republic of the Congo, Equatorial Guinea, Gabon) within the CEMAC economic zone.

- **Key regulatory driver**: CEMAC countries now mandate IBAN acceptance in payment instructions; IBAN format is fixed at 27 alphanumeric characters (4-char country code + 23-digit RIB identifier per Banque des Etats de l'Afrique Centrale governance).

- **Updated/new forms**:
  - Form 3597 (Country Specific Guidelines and Instructions): revised for 3 countries, new instructions added for 3 countries
  - Form 9252 (IBAN Countries): all 6 countries added to IBAN-regulated list
  - Form 10130 (Purpose of Payment and Category Codes): newly created for CEMAC zone

- **Data structure constraint**: Wire payment processing must validate IBAN format (27 chars: CM/CG/CF/TD/GQ/GA + 23-digit RIB) for these six countries; legacy non-IBAN formats likely deprecated for CEMAC transactions.

- **Currency/zone context**: XAF (Central African franc) is common currency; correspondent bank relationship with BEAC implies settlement routing dependencies on CEMAC-compliant payment rails.

- **Integration dependency**: Form 10130 introduction suggests purpose-of-payment code validation logic may need updates to support CEMAC-specific category codes not previously required.

- **Architect consideration**: Wire transfer validation rules, country-to-IBAN routing, and payment code lookups likely require configuration updates; confirm backward compatibility for non-CEMAC wire flows.