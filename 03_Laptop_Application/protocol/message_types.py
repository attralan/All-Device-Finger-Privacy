"""
Fingerprint Laptop Unlock System

Message Type Definitions

This module contains all supported
communication message types used between
Android and Laptop applications.

Protocol Reference:
00_Common/Communication_Protocol.md

Version:
1.0
"""


from enum import Enum



class MessageType(str, Enum):
    """
    Defines all supported communication messages.

    Values must match Android side exactly.
    """

    # Connection messages

    CONNECTION_REQUEST = (
        "CONNECTION_REQUEST"
    )

    CONNECTION_RESPONSE = (
        "CONNECTION_RESPONSE"
    )


    # Device pairing messages

    PAIRING_REQUEST = (
        "PAIRING_REQUEST"
    )

    PAIRING_RESPONSE = (
        "PAIRING_RESPONSE"
    )


    # Authentication messages

    AUTHENTICATION_REQUEST = (
        "AUTHENTICATION_REQUEST"
    )

    AUTHENTICATION_RESPONSE = (
        "AUTHENTICATION_RESPONSE"
    )



    def __str__(self) -> str:
        """
        Return message value as string.
        """

        return self.value