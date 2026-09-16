"""
Fingerprint Laptop Unlock System

Authentication Response Model

Defines the response structure sent
from Laptop Application to Android.

Protocol Reference:
00_Common/Communication_Protocol.md

Version:
1.0
"""


from dataclasses import dataclass
from typing import Optional



@dataclass
class AuthenticationResponse:
    """
    Represents an authentication response
    sent from Laptop to Android.
    """


    protocol_version: str

    message_type: str

    request_id: str

    status: str

    error_code: Optional[str] = None



    def to_dict(self) -> dict:
        """
        Convert response object into dictionary.

        Used for JSON communication.
        """

        return {

            "protocol_version":
                self.protocol_version,


            "message_type":
                self.message_type,


            "request_id":
                self.request_id,


            "status":
                self.status,


            "error_code":
                self.error_code

        }