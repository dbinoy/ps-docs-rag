# PS 21:25 Release Summary (July 12, 2021)

- **Release scope**: Documentation consolidation incorporating FAQs from Corporate Capture and Mobile Deposit (Deposit Anywhere) product pages into the centralized Deposit Processing Part of the manual.

- **Key documentation update**: Section 2.2 (Frequently Asked Questions) expanded with 27 new FAQ entries—Questions 11-17 for Mobile Deposits (Deposit Anywhere) and Questions 24-38 for Corporate Capture—suggesting parallel feature parity across two deposit channels.

- **Integration point dependency**: This release reflects content parity between two distinct deposit capture mechanisms (corporate batch processing vs. mobile/remote deposit capture), indicating these are separate code paths requiring aligned documentation and likely shared deposit processing workflows downstream.

- **Data flow relevance**: The consolidation implies both Corporate Capture and Mobile Deposit feed into a common Deposit Processing workflow, though they may have channel-specific handling rules documented separately in the Deposit Processing Part.

- **Architectural constraint**: FAQ numbering gaps (Questions 1-10 for Mobile, 11-23 for Corporate baseline) suggest deposit channel-specific logic; architects should expect conditional processing rules based on deposit source classification.

- **Support handoff**: Client Support (1-888-889-7878 Option 1, support@central1.com) is the point of contact—suggests potential SLA implications for deposit processing issues spanning both channels.