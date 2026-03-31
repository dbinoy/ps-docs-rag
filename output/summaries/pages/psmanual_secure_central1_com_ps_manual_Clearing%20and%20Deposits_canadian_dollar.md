# Summary: Canadian Dollar Money Orders Reconciliation & Tracing

- **Purpose**: Defines daily reconciliation and tracing procedures for Canadian dollar money orders drawn directly on credit unions, with settlement through standard clearing channels.

- **Core Process**: Money orders are debited from the credit union upon presentation/cashing and settled with regular Canadian dollar clearing items; credit unions must reconcile cashed items daily and monitor for fraud within CPA-specified timelines.

- **Key Data Structure**: Money orders identified by MICR-encoded account number on the physical item; reconciliation involves tracking serial numbers and maintaining two file states (Outstanding and Completed).

- **Integration Point - Online Return System (ORS)**: Critical dependency for retrieving cleared money order images; ORS serves as the authoritative source for payment status verification and image retrieval using MICR account number as lookup key.

- **Reconciliation Workflow**: Three-step process—(1) print cleared item image from ORS, (2) remove copy 3 from Outstanding file and attach image, (3) file sequentially by serial number in Completed file; no external trace requests required since items clear through internal systems.

- **Regulatory Constraint**: Credit unions bear responsibility for fraud detection and returns compliance with CPA timelines; daily reconciliation is mandatory, not optional.

- **No External Tracing Required**: Unlike other payment types, Canadian dollar money orders don't require trace request issuance since credit unions have direct online access to cleared images via ORS.