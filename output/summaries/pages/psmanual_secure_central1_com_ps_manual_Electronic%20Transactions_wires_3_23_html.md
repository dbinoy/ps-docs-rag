# Summary: Cancelling Outgoing Wires

**Overview:** This page documents the wire cancellation workflows in the Wires application, distinguishing between cancellations of pending vs. approved wires, with different processes and guarantees for each.

## Key Points for Architects

- **Two cancellation pathways with different permissions and guarantees:**
  - Pending wires (pre-approval): Cancellable directly in Wires application by wire creator or users with "Authorize Outgoing Transfers" MTS permission; immediate execution with no best-efforts clause
  - Approved/future-dated wires: Require ServiceNow trace request submission to Central 1; processed best-efforts basis only; deadline of 2:15 PM PT / 11:15 AM ET business day before value date

- **EFM integration point:** Approved outgoing wires are monitored in Enterprise Fraud Management (EFM) system; wires flagged as fraud are automatically cancelled in Wires with status change to "Cancelled" and no customer debit; EFM authorized users can access cancellation details but Wires application does not expose cancellation reason

- **Critical architectural constraint:** Wires application maintains no bidirectional sync with core banking/settlement systems; internal procedures required to settle with wire sender; cancellation in Wires does not guarantee fund return—receiving bank must voluntarily agree post-release by Central 1

- **Two-step authentication requirement:** Required for users with approval permissions accessing "Pending Outgoing" queue; not required for wire creators accessing "Submitted Wires" queue; authentication token code entry precedes wire selection

- **Reference number as primary identifier:** Wire reference number is the key lookup field for wire selection and cancellation action; no mention of alternative identifiers (e.g., transaction ID, beneficiary name)

- **Recall/amendment escalation:** Once wire transmitted to receiving institution, cancellation converts to recall or amendment request via Chapter 25 workflows; separate fee structure applies; no SLA on best-efforts processing