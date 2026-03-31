# Release 22:21 (September 2, 2022) - Wires Customization & Access Control Updates

- **Page Purpose:** Documents updates to Wire transfer customization capabilities (Form 6493) and user access control requirements for the Wires application within the Electronic Transactions Volume.

- **Customization Scope Clarification:** Customizable text is limited to **Confirmation and Receipt message boxes within the Wires application UI only**; printable confirmation/receipt terms and conditions are **not customizable** and remain fixed.

- **Authentication Requirement:** 2-step security token is now **mandatory** for users requiring access to Pending Incoming or Pending Outgoing menu options in Wires (integration point with User Management part/secure site profiles).

- **Beneficiary Financial Institution Data Population:** When users enter SWIFT/transit codes or select from search results, the **beneficiary's financial institution information auto-populates** in Wires—suggests read/cache mechanism from institution reference data store.

- **Key Data Elements:** Form 6493 (Wires Customization Request) is the control document; references to Sender 3rd Party Details vs. Beneficiary 3rd Party Details sections indicate separate data schemas for third-party wire origination/beneficiary scenarios.

- **Architectural Considerations:** Distinguish between application UI customization (dynamic) and document generation (static); security token enforcement creates dependency on User Management system; institution lookup/population suggests microservice or shared data layer for financial institution reference data.