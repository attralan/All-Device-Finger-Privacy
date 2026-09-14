# Laptop Application

## Project

Fingerprint-Laptop-Unlock-System

## Module

Laptop Application

## Purpose

The Laptop Application is responsible for receiving authentication requests from the trusted Android device, verifying the request securely, and performing the Windows unlock process after successful authentication.

The laptop application does not receive or store fingerprint data.

Fingerprint verification is performed only on the Android device using the Android biometric framework.

---

# Responsibilities

The Laptop Application handles:

- Android device communication
- Authentication request verification
- Trusted device management
- Security validation
- Cryptographic verification
- Authentication logging
- Windows integration
- Unlock process control

---

# System Flow

```
Android Application

        |
        |
        | Authentication Request
        |
        v

Communication Layer

        |
        |
        v

Authentication Service

        |
        |
        v

Security Verification

        |
        |
        v

Windows Integration

        |
        |
        v

Laptop Unlock

        |
        |
        v

Authentication Response

        |
        |
        v

Android Application
```

---

# Folder Structure

```
03_Laptop_Application
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env
├── main.py
│
├── communication_layer
│   ├── __init__.py
│   ├── server.py
│   ├── connection_manager.py
│   ├── message_parser.py
│   └── response_sender.py
│
├── protocol
│   ├── __init__.py
│   ├── message_types.py
│   ├── status.py
│   ├── error_codes.py
│   ├── request_model.py
│   └── response_model.py
│
├── authentication_service
│   ├── __init__.py
│   ├── authentication_manager.py
│   ├── request_validator.py
│   └── result_handler.py
│
├── security_layer
│   ├── __init__.py
│   ├── encryption.py
│   ├── key_manager.py
│   ├── proof_verifier.py
│   └── replay_protection.py
│
├── device_manager
│   ├── __init__.py
│   ├── device_registry.py
│   └── pairing_manager.py
│
├── database
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   └── fingerprint_system.db
│
├── windows_integration
│   ├── __init__.py
│   ├── unlock_manager.py
│   ├── windows_api.py
│   └── session_manager.py
│
├── config
│   ├── config.json
│   ├── devices.json
│   └── security.json
│
├── logs
│   └── system.log
│
└── tests
    ├── test_server.py
    ├── test_authentication.py
    ├── test_security.py
    └── test_unlock.py
```

---

# Module Description

## communication_layer

Responsible for communication between Android and Laptop.

Handles:

- Connection establishment
- Receiving messages
- Sending responses
- Message parsing

Files:

```
server.py
connection_manager.py
message_parser.py
response_sender.py
```

---

## protocol

Contains communication protocol definitions shared with Android.

Based on:

```
00_Common/Communication_Protocol.md
```

Handles:

- Message types
- Status values
- Error codes
- Request format
- Response format

---

## authentication_service

Responsible for authentication decisions.

Handles:

- Request validation
- Device verification
- Authentication result generation

Files:

```
authentication_manager.py
request_validator.py
result_handler.py
```

---

## security_layer

Responsible for protecting communication and authentication.

Handles:

- Encryption
- Key management
- Authentication proof verification
- Replay attack protection

Files:

```
encryption.py
key_manager.py
proof_verifier.py
replay_protection.py
```

---

## device_manager

Manages trusted Android devices.

Handles:

- Device registration
- Pairing
- Device verification

Files:

```
device_registry.py
pairing_manager.py
```

---

## database

Stores application data.

Stores:

- Trusted devices
- Security keys
- Authentication logs

Files:

```
database.py
models.py
fingerprint_system.db
```

---

## windows_integration

Handles communication with Windows system.

Responsible for:

- User session management
- Unlock process
- Windows API communication

Files:

```
unlock_manager.py
windows_api.py
session_manager.py
```

---

## config

Stores application configuration.

Files:

```
config.json
devices.json
security.json
```

---

## logs

Stores application activity.

Example:

```
Connection successful

Authentication request received

Authentication successful

Unlock completed
```

---

## tests

Contains module testing files.

Tests:

```
test_server.py

test_authentication.py

test_security.py

test_unlock.py
```

---

# Development Order

Follow this order:

1. Create project structure

2. Configure Python environment

3. Implement communication layer

4. Implement protocol module

5. Implement authentication service

6. Implement database

7. Implement security layer

8. Implement device management

9. Implement Windows integration

10. Perform Android-Laptop integration testing

---

# Communication Reference

The Laptop Application follows:

```
00_Common/Communication_Protocol.md
```

Protocol rules must not be changed without discussion between Android and Laptop developers.

---

# Security Rules

- Fingerprint data must never be received by the laptop.
- Only trusted devices are accepted.
- Authentication requests must be verified.
- Expired requests must be rejected.
- Repeated requests must be prevented.
- Cryptographic keys must be protected.

---

# Technology Stack

## Programming Language

Python

## Communication

TCP Socket + JSON

## Database

SQLite

## Security

Cryptography Library

## Windows Integration

Windows API

---

# Developer

Laptop Application Developer:

Member 2
