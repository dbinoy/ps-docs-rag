# Payment Solutions Release 20:11 Summary (April 29, 2020)

- **Purpose**: Release announcement introducing biller transaction limit functionality for the Electronic Bill Payment System, enabling financial institutions to cap transaction volumes per biller.

- **Key Constraint**: Biller transaction limits are **real-time clients only** and explicitly incompatible with batch integration architectures; limits only enforce on online, telephone banking, ATM, and in-branch channels.

- **New Capability**: Central 1 now offers configurable per-biller transaction limits as an optional service, requiring explicit enrollment/configuration by financial institutions.

- **Configuration Mechanism**: Two forms govern this feature:
  - **Form 9116** (new): Biller Transaction Limit Modification Request—allows FIs to set/modify limits on selected billers
  - **Form 2424** (revised): Financial Institution Transaction Limit Modification Request—operates at FI account level

- **Documentation Updates**: Electronic Bill Payments System Part expanded with new Section 1.2 (Biller Transaction Limits) and updated Section 1.4 (Document Library) to include Form 9116.

- **Integration Point**: Transaction limit validation occurs at payment authorization time within real-time processing path; batch payments bypass this logic entirely.

- **Support**: Client Support Services handles implementation questions (1-888-889-7878 Option 1 or support@central1.com).