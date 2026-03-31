# Release 23:14 Summary (June 22, 2023)

- **Overview:** Documentation relocation update for deposit processing workflows; two technical specification documents moved to Forms library with URL changes but no content modifications.

- **Relocated Documents:** 
  - Mobile Deposit (Deposit Anywhere) and Corporate Capture specifications now indexed in Payment Solutions Manual Forms library; existing links require updates.

- **Key Technical Specifications:**
  - **Form 6591:** ISO8583 Message Specifications for Mobile Deposit and Corporate Capture—defines message structure for deposit transaction interchange.
  - **Form 9353:** Corporate Capture File of XML Deposit Files Specifications—schema documentation for XML-based deposit file formats.

- **Integration Dependencies:** Form 9353 specification applies to multiple deposit processors including CUPS, CUCM, League Data, and third-party service providers consuming deposit files—critical for API/file-based integrations.

- **Data Flow Consideration:** Deposit processing pipeline spans Mobile Deposits → Corporate Capture → ISO8583/XML file formats → downstream clearing and deposits volume systems; architects designing enhancements must validate message/file format compatibility.

- **Maintenance Constraint:** No content changes in relocated documents, but documentation portal restructuring may affect external integrations referencing old bookmark paths—requires communication plan for dependent clients.

- **Support Reference:** Client Support Services (1-888-889-7878 Opt. 1 or support@central1.com) for specification questions.