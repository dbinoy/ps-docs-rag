# 2-Step Security Token Troubleshooting Summary

- **Purpose**: Diagnostic guide for resolving user authentication failures related to 2-step security token validation during login

- **Token Assignment Model**: Tokens are profile-specific, not user-specific; users with multiple profiles cannot reuse the same token across profiles, creating a 1:1 mapping constraint between tokens and individual user profiles

- **Token Types**: System supports both soft tokens (software-based) and hard tokens (physical devices), with different validation approaches per type

- **Code Reuse Constraint**: System prevents replay attacks by rejecting token codes from failed login attempts; users must wait for token refresh cycle before retrying, implying time-based or counter-based token generation

- **Serial Number Validation**: Hard token verification requires cross-referencing the physical device serial number (on token back) against the serial number stored in the User Management system's 2-step security summary, indicating a critical data sync dependency

- **Integration Dependency**: 2-step security token configuration and validation is tightly coupled with User Management module; token lifecycle and profile assignment is managed there

- **Troubleshooting Logic**: Three-step diagnostic flow (profile verification → code reuse check → serial number validation for hard tokens) suggests architects must design for token state tracking and profile-aware token context in authentication workflows