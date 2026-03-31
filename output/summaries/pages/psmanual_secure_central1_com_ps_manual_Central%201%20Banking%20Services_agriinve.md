# Summary: AgriInvest Reporting to Central 1

- **Purpose**: Documents the bi-monthly reporting workflow for Financial Institutions to submit AgriInvest Activity Files to Central 1, which aggregates them into regional files for transmission to AAFC.

- **Reporting Cadence**: Two fixed reporting periods per month (1st-15th, 16th-end); submissions accepted on first three business days following each period, with pickups every 30 minutes between 6 AM–6 PM PT.

- **File Format & Structure**: Activity Files must be submitted as CSV format (`AG01MMDD.dat`); Excel template (Form 3793) contains Layout sheet (for data entry) and Validation Summary sheet (for schema validation); all accounts reported regardless of activity status.

- **Transaction Types & Reversals**: Three transaction types with distinct sign conventions—Deposits (D), Withdrawals (W), Interest (I)—where corrections use reversal logic (e.g., negative sign for deposit reversals, positive sign for withdrawal reversals); critical for accurate accounting.

- **Central 1 Validation & Notifications**: System performs schema validation post-pickup and sends email notifications indicating success, file rejection, or account/transaction rejection; Financial Institutions have until end of third business day to resubmit; regional file transmission to AAFC blocked until all constituent Financial Institution files received.

- **Error Detection & Correction Split**: Central 1 detects file format and schema errors; AAFC detects missing accounts, missing transactions, and incorrect transaction entries—requiring liaison through Central 1 AgriInvest Officer for corrections submitted in subsequent reporting periods.

- **Date Field Distinction**: Two critical date fields exist—original transaction date (when posted to member account) vs. entry date (when recorded on Activity File)—essential for handling late-reported or corrected transactions spanning multiple reporting periods.

- **Integration Dependencies**: SFTP and File & Report Exchange (Client Centre portal) are submission channels; regional file aggregation depends on receipt of all institution files; backup Excel files enable error correction workflows within or across reporting cycles.