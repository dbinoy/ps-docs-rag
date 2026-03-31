# AFT Reports Summary

- **Overview**: Documents six core AFT reporting types (AIBC/AIBU/AIOC/AIOU, AFTD/UFTD, AFMS/UFMS, L003/U003, AFTM/UFTM, CCD/UCD) that provide transaction visibility, fee tracking, and reconciliation for financial institutions and originators across CAD and USD currencies.

- **Currency & Regional Segregation**: All reports dual-report by currency (Canadian on primary code, US on secondary code) and by charter/branch; AFMS/UFMS and L003/U003 are BC-only; CCD/UCD reports per CR file in BC and per ON file in Ontario—architecture must support parallel report streams per currency and region.

- **Fee Processing Models**: Two distinct billing patterns exist—daily (AFTD/UFTD, next business day distribution) vs. monthly (AFMS/UFMS, AFTM/UFTM)—with setup fees always charged in CAD regardless of file currency; financial institutions manually post charges to originator accounts, requiring integration with GL/billing systems.

- **Key Data Structures**: Reports organize around Originator ID, branch/charter hierarchy, file creation numbers, and transaction record types (C/D/E/F/I/J records per ATS standard); AIBC/AIOU report opening/closing balances and net activity; CCD/UCD report offsetting entries and return codes (e.g., 903 for recalls).

- **Reconciliation & Offsetting Logic**: Net AFT activity of zero prevents posting; non-zero activity posts debit or credit entry; offsetting entries are system-generated except in specific return scenarios (ORS/Batch Return Service) where financial institutions may submit manual offsets—architects must handle conditional offsetting logic.

- **System Dependencies**: Reports reference CAS Online for account data access, PaymentStream AFT for file uploads, ORS (Outbound Return Service) and Batch Return Service for returns, and the File and Report Exchange; CCD/UCD is optional/request-enabled and requires tracing integration for manual posting workflows.

- **Distribution Schedule & Constraints**: AIBC/AIOU produced daily (available next business day); AFTD/UFTD produced only if activity exists; L003/U003 monthly on last business day; AFMS/UFMS and AFTM/UFTM monthly—distribution timing impacts downstream reconciliation windows and settlement cycles.