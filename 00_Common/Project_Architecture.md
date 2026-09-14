# Project Architecture

## 1. Project Overview

All-Device-Finger-Privacy is a smartphone-based authentication system designed to help a user securely authenticate and unlock a Windows laptop using the biometric authentication capability of a trusted Android smartphone.

The smartphone performs biometric verification using the Android operating system's biometric authentication framework. The fingerprint data itself is not collected, stored, or transmitted to the laptop.

After successful biometric authentication, the Android application creates a secure authentication request and communicates with the laptop. The laptop verifies the request and, if all required security checks pass, proceeds with the Windows authentication and unlock process.

---

## 2. System Components

The system consists of the following major components:

### Android Application

Responsible for:

- User interface
- Biometric authentication
- Trusted laptop pairing
- Phone-side communication
- Creating authentication requests
- Receiving authentication responses

### Laptop Application

Responsible for:

- Receiving communication from the trusted Android phone
- Validating authentication requests
- Verifying the trusted device
- Performing security checks
- Integrating with the Windows authentication mechanism

### Communication Layer

Responsible for:

- Phone-to-laptop communication
- Request transmission
- Response transmission
- Connection management

The communication technology will be selected during the research and design phase.

### Security Layer

Responsible for:

- Device identity
- Secure pairing
- Cryptographic keys
- Authentication proof
- Request freshness
- Replay protection
- Unauthorized-device rejection

---

## 3. Overall Authentication Flow

```text
User
  |
  v
Android Application
  |
  v
Check Biometric Availability
  |
  v
Android Biometric Authentication
  |
  +------ Authentication Failed ------> Stop
  |
  v
Authentication Successful
  |
  v
Create Secure Authentication Request
  |
  v
Secure Communication
  |
  v
Laptop Application
  |
  v
Verify Device
  |
  +------ Unknown Device -----------> Reject
  |
  v
Verify Authentication Request
  |
  +------ Invalid Request ----------> Reject
  |
  v
Perform Security Checks
  |
  +------ Security Check Failed ----> Reject
  |
  v
Windows Authentication / Unlock
  |
  v
Return Result to Android
  |
  v
Display Result to User
