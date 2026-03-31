# Summary: Inter-Branch Transfers in Wires

**Overview:** Documents the wire system's capability to facilitate same-currency fund transfers between branches, with associated fee structures and routing logic.

**Key Concepts & Rules:**
- Inter-branch transfers via wires require **currency parity** between sending and receiving accounts; cross-currency transfers must be routed through provincial central Treasury Departments
- Standard wire fees apply to inter-branch transfers; sender branch is debited, receiver branch is credited
- **Real-time settlement** available for authorized users at BC/Ontario credit unions and other Central 1 clients via Treasury Connect (not standard wire processing)

**Integration Points & Dependencies:**
- **Treasury Connect application** (Form 6444) provides near-real-time alternative for eligible institutions; integrates with Central 1 account infrastructure
- **ServiceNow platform** serves as secondary integration path for inter-branch transfers for certain client classes
- **Provincial central Treasury Departments** act as intermediaries for cross-currency and out-of-scope transfer requests
- References Central 1 Current Accounts and High Interest Savings Accounts product documentation for procedural details

**Architectural Constraints:**
- Wire system lacks native cross-currency transfer capability—requires external routing
- Access to Treasury Connect/ServiceNow pathways is role-based and institution-type dependent (BC/Ontario credit unions, Central 1 clients, corporate clients have access; others must contact provincial central)
- Fee calculation logic must account for inter-branch wire classification vs. standard wires