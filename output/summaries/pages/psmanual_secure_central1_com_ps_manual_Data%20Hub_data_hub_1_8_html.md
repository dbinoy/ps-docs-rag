# Summary: Dashboard Export Functionality

- **Purpose**: Documents two export pathways for Payments Dashboard visualizations—PowerPoint and PDF formats—enabling stakeholders to extract and share dashboard snapshots and live data.

- **PowerPoint Export Modes**: Supports three distinct workflows: (1) embedding live data via URL copy-paste into existing presentations, (2) creating new presentations via "Open in PowerPoint" with on-screen guidance, and (3) static image export with configurable options. Live data embedding is the default selection.

- **PDF Export Process**: Single workflow—select export options, initiate export, and render dashboard image as browser-viewable PDF. Export rendering is asynchronous (multi-minute processing time) and relies on browser-native save/download functionality, introducing OS and browser-dependent variability.

- **Export Artifacts & Output**: PowerPoint exports auto-generate presentations with title page plus dashboard image; PDF exports produce browser-rendered documents. Both support configurable export options but documentation does not specify what those options include (resolution, date ranges, metric filters, etc.).

- **Live Data Integration Point**: PowerPoint's "Embed live data" feature generates URLs that reference live dashboard state, implying a data binding mechanism between exported presentations and backend dashboard service. Architecture must clarify URL lifecycle, refresh semantics, and access control for embedded links.

- **Processing Constraints**: Multi-minute export latency suggests server-side rendering or image generation pipeline. Architects should validate capacity planning for concurrent exports and identify whether this blocks user interactions or runs async.

- **Browser Dependency & UX Risk**: PDF save behavior is delegated entirely to client-side browser controls, creating potential support friction around download paths, naming conventions, and cross-browser inconsistency.