# Summary: Selling Unmatured Marketable Bonds

**Overview:** This page documents the process for Canadian credit unions to submit Government of Canada bonds and Treasury Bills for sale through Central 1 on a collection (consignment) basis at market value.

**Key Processes & Rules:**
- Three-step workflow: (1) obtain bondholder signature on redemption application; (2) secure Power of Attorney (Form 3788) with guaranteed signatures; (3) package and courier to Central 1 Payment Services
- Bearer bonds exempt from Power of Attorney requirement; registered bonds require signatures to match registration exactly or face rejection
- Deceased bondholder transactions require executor/administrator signatures with specific authentication phrase ("Signature of transferor and authority to sign guaranteed") in guarantor space
- Coupons cannot be sold separately; only intact bonds accepted
- Signature guarantee must be from credit union officer authorized per Central 1's maintained list; bonds require over-guarantee per Section 4.4

**Key Data Structures & Forms:**
- Form 3788: Power of Attorney to Sell and Transfer Securities
- Form 1323: Notification of Bond Sale (describes bond details; original copy required with submission)
- Critical field: "redemption value box" — incorrect entries delay credit settlement up to one month via Bank of Canada adjustment process

**Integration Points & Dependencies:**
- Central 1 Canadian Dollar current account receives settlement proceeds daily (upon settlement receipt)
- Bank of Canada processes adjustments; minimum threshold $6.99 (amounts ≤$6.99 not processed)
- Central 1 returns photocopy of transaction to credit union for member CRA income reporting
- **Key constraint:** Central 1 cannot predict receiving credit amount for marketable bonds (market-dependent); settlement routing differs from Canada Savings Bonds

**Critical Architectural Consideration:**
- Settlement timing and amount unpredictability for marketable bonds creates asynchronous reconciliation workflow distinct from standard bond redemption processes