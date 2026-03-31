# Payment Solutions Release Summary: PS 21:30

- **Release Overview**: August 5, 2021 patch introducing Limit Group 17 expansion for Interac e-Transfer® transaction processing

- **Key Concept - Limit Groups**: Interac e-Transfer implements tiered limit groups as a control mechanism; introduction of Limit Group 17 extends the existing limit classification system (suggesting at least 17 distinct limit tier configurations)

- **Data Structure Impact**: New limit group adds a discrete classification code (17) to the Interac e-Transfer Limit Groups taxonomy; architects should verify this identifier propagates through transaction validation and authorization workflows

- **Integration Dependency**: Changes affect the Interac e-Transfer subsystem specifically; limits likely enforce constraints on transaction amounts, frequency, or user tier eligibility, requiring synchronization across authorization engines and reporting systems

- **Constraint to Consider**: New limit group must be integrated into existing validation rules engine—architects need to confirm how limit groups are evaluated during transaction processing and whether this requires configuration updates to downstream systems

- **Documentation Reference**: Related technical specification available in Document Library record 9369 ("Interac e-Transfer Limit Groups"); revision status indicates this is a formal documentation update requiring version control tracking

- **Support and Escalation**: Client configuration and operational questions route through Central1 Client Support Services (1-888-889-7878, support@central1.com)—indicates limit group assignments may require client-specific setup or maintenance