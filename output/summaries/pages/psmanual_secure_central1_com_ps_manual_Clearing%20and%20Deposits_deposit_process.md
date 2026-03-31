# Summary: Accepting Cheques on Collection

**Overview:** This page defines the manual process for collecting cheques ineligible for Central 1 deposit by directly requesting settlement from drawee financial institutions, including eligibility criteria, collection request workflows, and settlement handling.

**Key Concepts & Rules:**
- Cheques ineligible for Central 1 deposit (e.g., non-USD foreign currency) can be sent "on collection" directly to the drawee branch, but Central 1 does not process these requests
- Collections are costly (drawee branch charges can exceed item value); Central 1 recommends against collecting items ≤$300 CAD equivalent
- No conventional recourse rights apply; settlement delays are expected and can be lengthy
- Foreign cheques become stale-dated after 6 months; items <1 month from stale-date risk return
- Endorsement requirements vary by drawee jurisdiction (US/foreign banks require payee name + account number; domestic may accept "deposited to account of" stamp)

**Data Structures & Reference Formats:**
- **Collection Reference Number Format:** `COLL[branch#][YY][sequential#]` (e.g., COLL62002-16-01)
- **Tracking Forms:** Outgoing Deposit Collection Items Register (Form 1089, Excel-based); Outgoing Collection Request (Form 1061)
- **Required Documentation:** Cheque (front/back copies), completed Form 1061, routing instructions, identification stamp, endorsement guarantee stamp with teller signature

**Process Flow & Integration Points:**
- Financial institution initiates collection request directly with drawee branch (no Central 1 involvement in routing)
- Settlement typically received via incoming wire transfer; triggers customer account credit
- Unpaid items returned by drawee branch; institution debits customer for associated charges
- Pending vs. completed collection request folders for lifecycle tracking

**Architectural Constraints:**
- No automated Central 1 processing—this is a manual, branch-level workflow with external dependency on drawee branch responsiveness
- Settlement delivery mechanism (wire transfer) requires integration with wire processing system
- Form 1061 may or may not be returned by drawee branch (no guaranteed two-way confirmation)
- Monitoring/follow-up logic relies on institution-defined time limits for payment/non-acceptance response