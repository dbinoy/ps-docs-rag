# Summary: PS 24:15 Release Notes - Enterprise Fraud Management Updates

- **Overview**: April 11, 2024 release documenting updates to Enterprise Fraud Management module to support Monitor Mode expansion for wire transactions alongside existing electronic transaction volume coverage.

- **Key Concept - Monitor Mode**: Newly operationalized capability for wire transactions that triggers email notifications, activity timelines, and manual alert creation workflows previously available only for other transaction types (Interac e-Transfer®).

- **Core Processes Updated**:
  - Incident detection and management (Incidents Page, Open List views) with revised UI/navigation
  - Transaction alert workflows including email notifications for Auto Risk-flagged wire transactions
  - Manual alert creation on previously unalerted wire transactions
  - Wire transaction fund recovery request procedures

- **Data Flow Integration Point**: Wire transaction data now flows through the same alerting and incident management pipeline as electronic transactions, suggesting unified data schema or adapter layer for heterogeneous transaction types.

- **Constraints & Operational Considerations**:
  - Wire transaction search functionality has specific behavioral considerations (Section 8.7) requiring architect awareness
  - Recovery of funds workflows differ between transaction types based on section-specific guidance

- **Architectural Implications**: Monitor Mode availability across multiple transaction types indicates feature flagging or transaction-type-based business logic branching; fund recovery pathways may require transaction-specific handling logic.

- **Support Dependencies**: Escalation paths: Client Support (1-888-889-7878) for general inquiries; Enterprise Fraud Management team (efm@central1.com) for specialized issues.