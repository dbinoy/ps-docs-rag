# Summary: Section 15 - Reports (PaymentStream AFT)

- **Purpose**: Documents three categories of AFT reports (PaymentStream AFT Reports, PaymentStream Direct Reports, and Central 1 Reports) with access procedures and creation workflows for financial institution and business member users.

- **Report Categories & Data Sources**:
  - PaymentStream AFT Reports: generated from user-entered or uploaded transaction data; purged per Section 13.2 schedule (data deletion impacts report availability)
  - PaymentStream Direct Reports: authorized FI users only; includes AFT Originator ID Listing, Deleted AFT Originator ID, and AFT Forecast reports
  - Central 1 Reports: settlement data, rejections, recalls; downloaded via File and Report Exchange (FIs) or PaymentStream AFT (business members)

- **Critical Business Rule**: Originator IDs inactive >12 months are automatically deleted by Central 1; AFT Originator ID Listing Report CSV export includes Last File Creation Date field to identify at-risk IDs approaching deletion threshold.

- **Integration Points**: 
  - PaymentStream Direct accessible via https://clients.central1.com with federated authentication
  - File and Report Exchange as distribution channel for Central 1 Reports to financial institutions
  - Report generation tied to Originator Type, Currency Type, and Branch organization filters

- **Key Data Elements**: Originator ID (financial institution and business member variants), Currency Type, Branch designation, settlement values (debit/credit), Last File Creation Date, and 7-day settlement forecast horizon based on approved + pending transactions.

- **Access Control Constraint**: PaymentStream AFT report access controlled by user's assigned Originator ID scope; PaymentStream Direct reports restricted to authorized financial institution users only.