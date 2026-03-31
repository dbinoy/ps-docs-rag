# PS Manual Section: AFT Exception Processing & Operations

## Purpose

This section documents Automated Funds Transfer (AFT) exception handling across the Central 1 clearing and settlement infrastructure for Canadian credit unions. It covers four primary workflows: file/transaction rejection and re-routing, transaction recalls (pre-posting intervention), error corrections (post-posting reversal), and trace request management. The documentation establishes regulatory compliance requirements, operational deadlines, data structures, and escalation procedures required to maintain settlement integrity across the payment network.

## Key Concepts

**Transaction Classes**: AFT distinguishes Debit Transactions (Pre-authorized Debits/PADs with 4 regulatory categories: Business, Cash Management, Funds Transfer, Personal) and Credit Transactions (Direct Deposits), each governed by distinct CPA Rules with different lead times, recall windows, and recourse periods.

**Exception Taxonomy**: File-level exceptions (formatting, structural errors) vs. transaction-level exceptions (invalid codes, account numbers); rejects occur at Central 1 or Receiving Institution data centres; recalls target unposted transactions; error corrections reverse already-posted transactions using opposing entry types (C↔E for credits, D↔F for debits).

**Settlement Mechanics**: Rejected/recalled/corrected transactions generate offsetting entries (type 900 for rejects, 903 for recalls) on standardized reports (ICRR/UCRR, ICSE/UCSE, CCD/UCD) and auto-post to originator or financial institution accounts; settlement obligations flow through Direct Clearer (Central 1 for BC/Ontario).

**Deadline Criticality**: Time-based state machine—File Recalls (2 pm, 2 business days pre-Due Date), Transaction Recalls (10:30 am, 1 business day pre-Due Date), Error Corrections (2 pm, 3 business days post-Settlement Date); missed deadlines move transactions into immutable states with no recovery options.

## How It Works

1. **Rejection Flow**: Central 1 or Receiving Institution validates transaction format/codes; invalid transactions rejected with 2-digit Invalid Field Number code; originator discovers via manual monitoring of PaymentStream confirmation email or Activity Log (no proactive notification); must reconcile daily via ICRR/UCRR reports.

2. **Recall Flow**: Originator submits recall request (File/Single/Multiple transaction) via ServiceNow or Form 3295 before deadline; Central 1 attempts to prevent data centre forwarding; settles via return code 903; debit recalls prohibited post-forwarding.

3. **Error Correction Flow**: Originator submits correction request via ServiceNow (Form 3386 template) or Form 3295 within 3 business days of Settlement Date; generates reversing transaction; disputable for 90 days; prohibited on returned (I/J record) transactions.

4. **Trace Flow**: Originator queries missing transaction via ServiceNow or Form 3296; Central 1 searches clearing reports (CCD/UCD by Run number); responds within 2–5 business days; non-obligatory for items ≤$20 or requests >12 months post-settlement.

## Integration Points

- **ServiceNow**: Primary submission channel for recalls, error corrections, trace requests; generates tickets; Form 3295/3296/3386 provide manual fallback
- **CPA Rule F1/H1**: Regulatory enforcement for procedures, deadlines, settlement mechanics
- **Clearing Reports** (ICRR/