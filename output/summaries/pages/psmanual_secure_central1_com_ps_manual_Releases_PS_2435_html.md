# Release 24:35 Summary for Solutions Architect

- **Overview**: September 16, 2024 release updating Country-Specific Guidelines and Instructions (Form 3597) with synchronized changes to the Wires application

- **Form 3597 Scope**: Document defines country-level compliance metadata including sanctions/warning messages and payment instructions; serves as master reference for wire transfer processing rules

- **Sanctions/Warning Message Management**: 
  - Added for 13 countries (Albania, Comoros, Curaçao, Djibouti, Guatemala, Guyana, Laos, Liberia, Monaco, Namibia, Sierra Leone, Sint Maarten, Suriname)
  - Updated for 7 countries (Belarus, China, Ethiopia, F.Y.R. Macedonia, Montenegro, Serbia, Tunisia)
  - Removed for 7 countries (Bahamas, Belize, Brazil, Cayman Islands, Israel, Seychelles, Turks and Caicos)

- **Payment Instructions Data**: Added country-specific payment routing/format rules for Australia and Denmark; revised instructions for Bahrain, Kuwait, Pakistan, Uganda, and Viet Nam—suggest these are wire format templates or routing specifications

- **Integration Dependency**: Wires application is a synchronized consumer of Form 3597 changes; requires bi-directional consistency between Payment Solutions documentation and Wires operational system

- **Architect Considerations**: Country-level rule changes appear configuration-driven rather than code-driven; design should support rapid country metadata updates without application deployment. Verify whether Wires application pulls Form 3597 as external reference or maintains local cache requiring sync validation

- **Support Contact**: Client Support Services (1-888-889-7878 Option 1 or support@central1.com) for implementation or clarification questions