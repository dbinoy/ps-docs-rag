# Release 24:04 (January 8, 2024) - Forms Infrastructure Migration Summary

- **Overview**: This release migrates the forms library from a secure internal site to SharePoint Online, introducing a new Forms experience on the Client Centre with updated URLs and search functionality.

- **Migration Impact**: All form URLs have changed; existing bookmarks are invalid. Forms are now accessed via SharePoint Online rather than the legacy secure site infrastructure, requiring URL replacement across documentation and integrations.

- **Search & Discovery Mechanism**: Forms searchable by form number or form name via dedicated search function on the Forms and Manuals page; results display in new tab with form links, instruction links, and contact information. Search results are sorted by date (most recent first).

- **Content Delivery Model**: PDFs render in-browser; Word/Excel documents auto-download. Completion instructions are linked separately in a "View instructions" column on search results. Form versioning tracked via internal revision dates in form footers.

- **Data Structure**: Forms are indexed with metadata including form number, form name, completion instructions availability, and last update date. Manual pages contain contextual links that route to form-specific search results pages.

- **Dependency & Platform**: Relies on SharePoint Online as backend repository; Client Centre is the primary access point. Forms and Manuals page acts as the central distribution hub.

- **Known Constraints & Roadmap**: Favorite/bookmarking functionality on new platform is not yet implemented; team is actively developing this feature. Support contact: Client Support Services (1-888-889-7878 Option 1 or support@central1.com).