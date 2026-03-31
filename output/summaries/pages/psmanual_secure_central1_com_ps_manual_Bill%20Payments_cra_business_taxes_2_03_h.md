# Summary: Legal and Policy Considerations for Business Taxes

**Overview:** Documentation of CPA Rule G4 compliance requirements and internal control policies governing CRA payment acceptance for GST/HST, Excise, Taxation, and Customs remittances.

## Key Points

- **CPA Rule G4 Compliance Requirements:**
  - Off-hours payments must be date-stamped as next business day transactions (temporal handling constraint)
  - Remittance vouchers only valid when submitted by the presenter (authentication/authorization requirement)
  - Dual-part voucher stamping mandatory (both parts require financial institution date stamp)
  - Dishonoured cheque recovery protocol: attempt collection, escalate to federal reimbursement if unsuccessful (exception handling workflow)

- **Data Structure - Remittance Voucher:** Two-part document requiring synchronized date stamping; currently managed as paper artifacts with no CRA mandate on retention vs. destruction (indicates potential digitalization opportunity)

- **Integration Dependencies:** PaymentStream™ Direct platform handles Business Taxes processing and remittance voucher lifecycle; architects must reference that module for internal control policies and processing workflows

- **Institutional Responsibility Boundary:** Financial institutions own security practices, internal controls implementation, and disposal policy definition—not prescriptive CRA requirements (design flexibility but audit accountability)

- **Architectural Consideration:** Current paper-based remittance voucher handling creates compliance risk around secure destruction; digital workflow redesign could improve auditability and reduce manual process fragility