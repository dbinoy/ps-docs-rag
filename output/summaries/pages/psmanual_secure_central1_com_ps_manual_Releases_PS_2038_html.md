# Payment Solutions 20:38 Release Summary

- **Release scope**: October 7, 2020 update enabling return wire creation directly within the Wires application, eliminating dependency on MTS (Money Transfer System) for wire returns

- **Key functional change**: Authorized users can now initiate return wires from two transaction states—Pending Incoming list and Received Wires list—with new status type "Returned" reflecting across both Wires and MTS systems

- **Data structure impact**: Status Type enumeration expanded to include "Returned" status; return wire transactions must synchronize status state between Wires application and MTS for consistency

- **System integration**: Wires application maintains bidirectional data synchronization with MTS; wire returns initiated in Wires must propagate status updates to MTS without requiring manual intervention or MTS-side operations

- **Access control constraint**: Return wire functionality restricted to authorized users only; user set up procedures in Chapter 5 define authorization scope and capability assignment for this feature

- **Documentation scope**: Updates span Chapters 5, 10.1, and 17 covering access administration, status type definitions, and return procedures—indicates architectural touch points across authentication, data models, and transaction workflows