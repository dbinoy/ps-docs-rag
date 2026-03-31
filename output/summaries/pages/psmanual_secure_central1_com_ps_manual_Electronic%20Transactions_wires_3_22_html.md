# Summary: Approving Outgoing Wires

**Overview:** This section defines the authorization workflow and approval requirements for outgoing wire transfers based on wire amount, creation source, and MTS branch-level configuration settings.

**Key Concepts & Rules:**
- **Two-tier approval model** based on MTS authorization levels (Level 1 and Level 2) with different requirements for in-branch vs. MDB/Forge Commercial wires
- **In-branch wires:** require 1 approval if amount ≤ Level 2; require 2 approvals if amount > Level 2 (Level 1 field ignored)
- **MDB/Forge Commercial wires:** require 0 approvals if amount ≤ Level 1; require 1 approval if Level 1 < amount ≤ Level 2; require 2 approvals if amount > Level 2
- **Authorization limits are user-agnostic**—all Wires users are subject to the same MTS-defined thresholds regardless of individual role permissions

**Critical Constraints & Permissions:**
- Approvers must hold "Authorize Outgoing Transfers" permission in MTS and have a 2-step security token assigned to their Client Centre ID
- Users cannot approve wires they created or edited; self-approval is blocked
- Wire visibility is scoped to branches assigned to the user in MTS
- Approved wires cannot be cancelled in-application; only recalls, amendments, or traces (future-dated only) are available on best-efforts basis

**Integration Points & Data Dependencies:**
- **MTS branch settings** drive all authorization logic (Section 9.5)—MTS is the source of truth for Level 1 and Level 2 authorization thresholds
- **Source System field** tracks wire origin (PSD, MDB, Forge Commercial) to determine approval pathway
- **Disconnected settlement:** Wires application is not integrated with institution's banking system; manual internal settlement procedures required post-approval
- **Central 1 as clearing intermediary:** once approved, funds are released by Central 1 to receiving institution; no real-time recall capability

**Architect Must Know:**
- Approval workflows are stateful (status field tracks "1 Approval Required" vs. fully approved)
- 2-step security token is a hard requirement for approval operations, not optional
- Wire release is irreversible at the Wires application layer—design must account for post-send settlement reconciliation outside this system