"""
Fingerprint Laptop Unlock System

Status Definitions

This module contains all possible
communication and authentication states.

Protocol Reference:
00_Common/Communication_Protocol.md

Version:
1.0
"""


from enum import Enum



class Status(str, Enum):
    """
    Defines application status values.

    These values are shared between
    Android and Laptop applications.
    """

    # Connection states

    CONNECTED = "CONNECTED"

    DISCONNECTED = "DISCONNECTED"



    # Authentication states

    AUTHENTICATING = "AUTHENTICATING"

    AUTHENTICATED = "AUTHENTICATED"



    # Failure states

    REJECTED = "REJECTED"

    ERROR = "ERROR"



    def __str__(self) -> str:
        """
        Return status value as string.
        """

        return self.value