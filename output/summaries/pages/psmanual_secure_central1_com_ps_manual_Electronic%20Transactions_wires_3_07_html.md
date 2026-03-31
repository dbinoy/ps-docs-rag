# Summary: MTS Administrator Management for Wires

- **Purpose**: Defines role-based administration framework for managing Wires Users, MTS Administrators, and branch settings through the Money Transfer System (MTS), with dual-system setup requirements and mandatory change authorization workflows.

- **Dual-System Architecture**: MTS Administrators require Client Centre user profiles (set up in User Management with MTS application access and 2-step security tokens assigned first) plus corresponding MTS Administrator profiles created in MTS—dependency on User Management application for prerequisite credential establishment.

- **Permission Model**: Eight granular permission flags control administrator capabilities (Admin U/A, Brn U/A, User U/A, Linked Transit Assignment); first two administrators provisioned by Central 1 via Form 2119 with all permissions; subsequent administrators created within MTS by existing administrators with appropriate "Update Administrator Profile" permission.

- **Processing Model Dependency**: MTS Administrator home transit numbers and permission assignments are influenced by selected Wires processing model (centralized, partially centralized, or decentralized environments per Chapter 5), indicating architectural constraints tied to institutional topology.

- **Mandatory Authorization Gate**: All User, Administrator, and branch changes require secondary MTS Administrator authorization via Change List queue before activation; architects must account for asynchronous state management (pending vs. active profiles) and cannot modify profiles with pending changes.

- **Data Fields & Constraints**: User ID must match Client Centre username (20 character max); transit numbers pulled from dropdown linked to home transit with branch linking permissions; Daily/Transfer Limits (Canadian dollar basis with currency conversion for non-CAD wires) apply to "Authorize Outgoing Transfers" permission only.

- **Integration Point**: User Management application is critical upstream dependency—removing MTS application access or deleting Client Centre profiles must be coordinated with MTS Administrator deletion; no standalone MTS user deletion without downstream User Management cleanup.