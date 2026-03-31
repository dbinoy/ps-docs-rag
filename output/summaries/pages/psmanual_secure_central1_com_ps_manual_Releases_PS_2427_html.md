# PS 24:27 Release Summary (August 2, 2024)

- **Scope**: Documentation update to Enterprise Fraud Management (EFM) module focusing on wire transaction handling in Decision Mode, aligned with newly released job aid for wire scenario management.

- **Key Process Change**: Wire transactions now have distinct handling rules in Decision Mode vs. Monitor Mode; Monitor Mode wire guidance has been deprecated and removed from documentation to prevent operational confusion.

- **Critical Business Rule**: The No-risk Reason code "e-Transfer: Confirmed Legitimate – Customer Wants to Cancel" is explicitly prohibited for wire transactions, indicating separate risk classification logic between e-transfers and wires.

- **Documentation Scope**: Updates span transaction alert management (Section 8.1), legitimate transaction identification (Section 8.3), auto-risk alert classification (Section 8.4), and new wire-specific operational guidance (Section 8.7).

- **System Integration Point**: EFM system operates in dual environments alongside a separate Wires application; Section 8.7 defines interaction boundaries and data flow between these systems.

- **Visual/UI Updates**: Image references in Sections 8.1 were refreshed to match current system behavior, suggesting potential UI changes in the EFM alert management interface.

- **Support Contact**: EFM-specific questions route to efm@central1.com; architects should engage this team for wire scenario clarifications during design.