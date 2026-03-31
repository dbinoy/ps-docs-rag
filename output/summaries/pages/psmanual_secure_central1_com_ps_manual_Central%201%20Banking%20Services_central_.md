# Central 1 High Interest Savings Accounts - Technical Summary

- **Overview**: Central 1 HISAs are CAD-denominated, low-risk deposit instruments managed via Treasury Connect with liquidity access and near-real-time transaction visibility (7-year history).

- **Account Lifecycle**: HISA creation requires Form 10133 (High Interest Savings Account Agreement) with dual authorized officer signatures submitted to Central 1; closure via direct contact to treasury@central1.com. Central 1 manages provisioning notification.

- **Key Constraints**:
  - Maximum deposit cap: $10,000,000.00 CAD per contribution
  - Redemptions must be scheduled 31-90 calendar days in advance; non-cancellable/non-reversible once scheduled
  - Redemptions process business days only (statutory holidays trigger next-day settlement)
  - External fund transfers explicitly blocked (HISA transits not registered with Payments Canada)

- **Integration Points**:
  - **Treasury Connect** (Form 6444 governs procedures): Primary user interface for account summary viewing, fund transfers, and transaction export
  - **Client Centre ID**: Required for Treasury Connect application assignment
  - **Permissions Model**: Role-based access via "Account Summary" and "Transfer Funds" permissions; intra-bank transfers only between Central 1 CAD accounts

- **Data & Settlement**: Account data updated near-real-time throughout business day; opening balances available by 5:30 AM PT (8:30 AM ET). Transits cannot be issued or registered with Payments Canada—critical architectural constraint for payment routing.

- **Architect Must Know**: HISA is a segregated account entity (displays separately from CAD current accounts); fund movement is strictly internal to Central 1 ecosystem and subject to rigid scheduling constraints—design integrations anticipating 31-90 day redemption lead times and business-day-only settlement.