# Incoming Clearing Reports Summary

- **Purpose**: Documents seven clearing report types (CHQ4, CLI, CLO, CLSR, CLUS, PADB, SUSC, UADB) that provide credit unions visibility into incoming clearing items processed by Central 1, with reports available within 24 hours of processing.

- **Report Distribution Model**: All reports delivered via MERG files in File and Report Exchange with currency-based folder hierarchy (CAD/USD subfolders); PDF formats stored in Banking (CHQ4), Clearing (CLI/CLO/CLSR/CLUS/SQC/SUSC), and AFT (PADB/UADB) folders.

- **Item Classification Hierarchy**: Incoming items categorized as Qualified/Unqualified, In-Province (Vancouver/Toronto/Montreal/Halifax) vs. Out-of-Province (Calgary/Winnipeg), with separate Canadian dollar (CAD) and US dollar (USD) processing tracks and distinct handling for Business PADs vs. standard cheques/drafts/chargebacks.

- **Postability Logic**: CLI/CLO reports segment items into Unpostables (unreadable/missing account numbers) and Postables (readable by Central 1 equipment), with special marking for paper business pre-authorized debits; Unqualified Items excluded from all clearing list reports.

- **Branch-Level Debiting**: Summary reports (SQC, SUSC, CLSR) organize debits by branch rather than posting grand totals to master accounts; this branch-level granularity is critical for reconciliation workflows and account posting logic.

- **Cross-Border and Currency Rules**: CLUS report handles three item types: US dollar account draws, Canadian dollar account draws marked "US Funds," and foreign chargebacks; US Non-Account 6404 section specifically supports manual member account debiting for cross-currency scenarios.

- **Business PAD Recourse Differentiation**: PADB and UADB reports separately distinguish paper vs. electronic Business PADs because recourse periods differ from standard PAD types; reports generated even when zero electronic transactions exist (forcing downstream consumption logic to handle empty datasets).