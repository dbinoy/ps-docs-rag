# FYI – April 2025 Summary

- **Purpose**: Documentation update notification for Payment Solutions Manual regarding file upload procedures in the Clearing and Deposits Volume module (April 2025 release)

- **Key Change**: Section 14.3 (Online Return System/ORS) removed automated script-based file upload instructions and replaced them with manual FTP server upload procedures via Central 1's FTP infrastructure

- **Integration Point**: ORS integrates with Central 1's FTP server as the primary file transfer mechanism; automated script workflows are no longer supported or documented

- **Operational Impact**: Organizations previously using automated scripts for ORS file uploads must transition to manual FTP server uploads—this represents a process change affecting batch file submission workflows

- **Support Contact**: Central 1 Client Support Services handles questions regarding the ORS upload changes (1-888-889-7878 Option 1, or support@central1.com)

- **Documentation Scope**: The update affects only ORS file upload procedures; other Clearing and Deposits Volume functionality remains unchanged

- **Architecture Consideration**: Any system integrations or automation workflows that rely on programmatic file submission to ORS require redesign to use FTP-based file transfers instead of API/script-based methods