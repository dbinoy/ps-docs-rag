# AFT Notice of Change Transactions - Architecture Summary

- **Purpose**: AFT NOC transactions are non-financial notification messages that update Transit Number or account number routing information for AFT Originators when changes occur (branch closures, acquisitions, account transfers, or correction of initial routing data).

- **Scope Constraint**: NOC transactions are created only for routing updates within the same financial institution; institution-to-institution Payor/Payee migrations do not trigger NOC creation per CPA Rule F1 and H1.

- **Creation Flow**: Financial institutions originate AFT NOC transactions via the Online Return System (ORS), with origination tracked in the NOC – Originated by Credit Union (NCOC/NUOC) report.

- **Reception & Processing Flow**: Originating Direct Clearers send NOC transactions to AFT Originators; institutions must review the Notice of Change (AFT) Detailed Listing (NCDL/NUDL) report and update their AFT routing databases (either PaymentStream AFT or alternative software) immediately upon receipt—this is a mandated regulatory requirement under CPA Rules F1 and H1.

- **Integration Dependencies**: System must integrate with ORS for NOC creation, generate/distribute NCDL/NUDL reports to institutions and originators, and synchronize with downstream AFT transaction processing systems (PaymentStream AFT, alternative software) to prevent routing delays.

- **Data Accuracy Responsibility**: Originating Direct Clearers are accountable for NOC transaction accuracy; immediate database updates by receiving institutions are required to prevent processing failures in subsequent AFT transactions.