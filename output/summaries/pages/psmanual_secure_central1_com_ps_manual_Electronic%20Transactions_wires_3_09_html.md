# MTS Branch Management for Wires - Technical Summary

- **Purpose**: MTS Administrators configure wire authorization thresholds at the branch level to enforce single or dual-approval requirements based on transaction amount and processing model (centralized, partially centralized, or decentralized).

- **Authorization Threshold Model**: Two mandatory fields (Level 1 and Level 2) define approval requirements—wires ≤ Level 1 may bypass approval (MDB/Forge only), Level 1-to-Level 2 range requires one approval, and amounts > Level 2 require two approvals; in-branch wires always require minimum one approval regardless of Level 1 setting.

- **Multi-Transit Architecture**: Supports linked transit numbers where a home transit can be associated with multiple branches; authorization limits are evaluated against the user's home transit, not the transaction origination branch; linked transits require "Use Linked Transits" permission on MTS profile.

- **Foreign Currency Conversion Dependency**: Outgoing wires in non-CAD currencies are converted to Canadian dollars at live rates (or last-available rate) to compare against authorization thresholds; conversion is advisory only and does not affect wire settlement currency.

- **Change Authorization Workflow**: All branch setting modifications require a two-step authorization—initial entry by one MTS Administrator, then explicit approval by a second MTS Administrator via Change List queue; pending changes block branch visibility in the main Branch queue until resolved.

- **Integration with Wires Processing**: Wires processing model selection (Chapter 5) determines whether settings are configured per-branch or head-office-only; wire fee management is decoupled (Chapter 11) and does not reside in MTS; Financial Institution File (FIF) from Payment Canada is the authoritative source for institution/branch data (read-only in MTS).

- **Critical Constraint**: Authorization limits must be established before the first wire transaction is created for a branch; due diligence requirement emphasizes ensuring large-value wires receive dual approvals.