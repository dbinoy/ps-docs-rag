# Payment Solutions 22:19 Release Summary

- **Release scope**: August 15, 2022 update introducing Ontario-qualified debit clearing file specifications and replacing legacy "Posting File" terminology with standardized DCPA/QCPA/XDREC/XQREC file references across BC and Ontario regions.

- **File specification updates**: Four clearing item file formats now documented:
  - DREC/QREC (BC only)
  - XDREC/XQREC (BC and Ontario, XML message format)
  - DCPA/QCPA (Ontario only, supports CAD and USD cheques)

- **Deprecated functionality**: Late unqualified clearing items processing removed from settlement workflows; legacy "Posting File" (Ontario) terminology eliminated in favor of DCPA/QCPA references.

- **Settlement and reconciliation logic**: Clarified statement reporting for credit union Central 1 account settlement; updated member account settlement references to use Ontario-specific clearing file codes (DCPA/QCPA) with XDREC/XQREC as applicable alternatives.

- **Integration dependencies**: Clearing item processing flows depend on correct file format selection by region (BC vs. Ontario); XML-based XDREC/XQREC formats available as alternatives in both regions; file specifications document (9528) is newly published control point.

- **Architect consideration**: Any clearing item routing logic, validation rules, or settlement reconciliation algorithms must implement region-aware file format selection and reference current DCPA/QCPA/XDREC/XQREC specifications, not legacy Posting File definitions.