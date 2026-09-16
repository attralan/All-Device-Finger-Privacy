"""
Fingerprint Laptop Unlock System

Error Code Definitions

This module contains all error codes
used for communication responses.

Protocol Reference:
00_Common/Communication_Protocol.md

Version:
1.0
"""


from enum import Enum



class ErrorCode(str, Enum):
    """
    Defines all possible system errors.

    Values must match the common
    communication protocol.
    """

    # Device related errors

    UNKNOWN_DEVICE = "E001"



    # Authentication errors

    AUTHENTICATION_FAILED = "E002"



    # Request validation errors

    INVALID_REQUEST = "E003"

    EXPIRED_REQUEST = "E004"



    # Communication errors

    CONNECTION_FAILED = "E005"



    # Protocol errors

    PROTOCOL_MISMATCH = "E006"



    # Security errors

    SECURITY_VERIFICATION_FAILED = "E007"



    def __str__(self) -> str:
        """
        Return error code value.
        """

        return self.value