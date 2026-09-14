# Communication Protocol

## Communication Flow

Android Phone → Windows Laptop → Android Phone

## Message Types

CONNECTION_REQUEST
CONNECTION_RESPONSE

PAIRING_REQUEST
PAIRING_RESPONSE

AUTHENTICATION_REQUEST
AUTHENTICATION_RESPONSE

## Authentication Request

- protocol_version
- message_type
- request_id
- device_id
- challenge
- timestamp
- authentication_proof

## Authentication Response

- protocol_version
- message_type
- request_id
- status
- error_code

## Status

CONNECTED
DISCONNECTED
AUTHENTICATING
AUTHENTICATED
REJECTED
ERROR

## Error Codes

E001 = Unknown device
E002 = Authentication failed
E003 = Invalid request
E004 = Expired request
E005 = Connection failed
E006 = Protocol mismatch
E007 = Security verification failed

## Security Rules

- Raw fingerprint data must never be sent to the laptop.
- Only trusted paired devices are accepted.
- Authentication requests must be verified.
- Expired or repeated requests must be rejected.
- Cryptographic keys must be protected.
- Invalid messages must be rejected.

## Communication Technology

To be decided:

- Bluetooth
- Wi-Fi / LAN

## Protocol Version

Version: 1.0
Status: Initial Design
