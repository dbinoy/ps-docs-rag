# Payment Solutions 21:20 Release Summary (June 18, 2021)

- **Release scope**: Documentation update adding three new file specifications to the Payment Solutions Manual with links distributed across four volumes (Access & Administration, AFT, Clearing & Deposits, ORS).

- **New file specifications introduced**:
  - AFT Return File Specifications (Doc ID 9335)
  - Notice of Change (NOC) File Specifications (Doc ID 9336)
  - Corporate Capture XML Deposit File Specifications (Doc ID 9349)

- **Data flows affected**: AFT (Automated Funds Transfer) returns and NOC transactions now have formalized specifications; Corporate Capture XML represents an alternative deposit file format requiring distinct processing rules.

- **Integration points**: Specifications are referenced across multiple volumes indicating dependencies—AFT processing touches both AFT Volume and Online Return System (ORS), while Corporate Capture XML impacts Deposit Processing workflows in the Clearing & Deposits Volume.

- **Document structure constraint**: File specifications are centralized in Section 1.4 (File Specifications Document Library) within Access & Administration Volume, requiring all downstream sections to maintain links; broken references would impact system documentation consistency.

- **Architecture consideration**: Three distinct transaction/deposit types (AFT Returns, NOC, Corporate Capture XML) suggest different parsing, validation, and processing logic branches; architects should model these as separate data ingestion paths with format-specific handlers.

- **Support/validation**: Client Support Services (1-888-889-7878, support@central1.com) is the escalation point for specification interpretation issues during implementation.