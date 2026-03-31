# wwparcel.html Summary for Solutions Architect

- **Page Purpose**: Comprehensive documentation for two primary payment solutions modules—FX Notes (foreign currency exchange management) and Currency Ordering & Precious Metals (cash services operations)—covering user access, transaction processing, settlement, and compliance frameworks.

- **Key Concepts & Processes**:
  - FX Notes: Foreign exchange spreads, transaction fees, retail rate modifiers, currency buying/selling workflows, and authentication via image verification
  - Cash Services: Standing orders, late orders, contingency orders, currency order lifecycle management, and counterfeit/discrepancy handling procedures
  - Both modules include strict legal/compliance layers (AML/CFT, economic sanctions, Globex 2000 rules)

- **Critical Data Flows**:
  - FX Notes: Customer ↔ FX Notes system → Globex 2000 (shipping/settlement); includes order editing, cancellation, and reconciliation workflows
  - Cash Services: Order creation → delivery verification → return processing (with deposit slip adjustments); separate settlement tracks for orders vs. returns
  - Precious Metals: Integrated buy/sell-back cycle with incoming parcel verification and settlement

- **Integration Dependencies**:
  - **ServiceNow**: External system for managing cash order locations, limits, standing/late/contingency orders
  - **Globex 2000**: Foreign currency clearinghouse (validates spreads, receives shipments, processes settlement)
  - **Client Centre**: User authentication and access gateway
  - **Central 1**: Password/account reset backend

- **User Management & Access Control**:
  - Role-based access: Client Centre Users, CPS Admin Security Officers, Cash Services user types with granular location-based permissions
  - Separate password policies for Client Centre; account unlock/reset workflows tied to Central 1
  - Audit trails via User Audit Reports

- **Constraints & Compliance Requirements**:
  - Order deadlines and delivery windows are fixed (not configurable per transaction)
  - Mandatory counterfeit/discrepancy handling procedures with documented workflows
  - Settlement processes differ by institution type (BC/Ontario members vs. non-member financial institutions)
  - Unfit, contaminated, and mutilated currency have dedicated return procedures

- **Architect Must Know**:
  - Two largely independent but parallel operational modules (FX Notes and Cash Services) with different settlement logic
  - Heavy reliance on external systems (ServiceNow, Globex 2000) means enhancement scope must account for inter-system dependencies
  - Regulatory/compliance burden is substantial—any process changes require legal review (AML/CFT, sanctions,