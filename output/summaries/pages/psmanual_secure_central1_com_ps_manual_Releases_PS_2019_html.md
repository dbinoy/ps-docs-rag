# PS 2019 Release Summary – Cash Services Procedures Update

- **Purpose**: Documents updates to the Manage Cash Order Locations form in ServiceNow and Form 9031 (Cash Services Procedures – Quick Reference Guide) effective June 5, 2020

- **Migration Status & Constraint**: Two parallel systems in operation—institutions on Cash Services system use Form 9031; institutions not yet migrated continue using legacy Currency and Coin Order form in ServiceNow. This dual-system requirement will persist until all institutions complete migration

- **Key Data Model Changes**: Form 9031 clarifies required field content in the Manage Cash Order Locations form; Section 3.1 introduces delivery date flexibility for institutions with set armoured carrier schedules, with cut-off times mapped to configured "days in transit" parameters

- **New Location Management Architecture**: Procedures reorganized into separate sections (5.1 for creation, 5.2 for updates), indicating potential schema changes to location record structure in ServiceNow

- **Integration Point**: Tight coupling between ServiceNow workflows (Standing Orders, Late Orders, location management) and Cash Services system; armoured carrier scheduling data must integrate with delivery date logic

- **Future State**: Form 9031 is explicitly temporary; requires consolidation into unified Payment Solutions Manual when 100% migration complete. Architects should design current solutions for eventual deprecation of Form 9031 and legacy Currency/Coin Order workflows

- **Training & Support Surface**: Cash Services Training Videos provided as supplementary resource; client support via 1-888-889-7878 or support@central1.com