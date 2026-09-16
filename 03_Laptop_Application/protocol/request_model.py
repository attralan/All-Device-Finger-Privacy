"""
Fingerprint Laptop Unlock System

Authentication Request Model

Defines the structure of authentication
requests received from Android.

Protocol Reference:
00_Common/Communication_Protocol.md

Version:
1.0
"""


from dataclasses import dataclass



@dataclass
class AuthenticationRequest:
    """
    Represents an authentication request
    received from Android device.
    """


    protocol_version: str

    message_type: str

    request_id: str

    device_id: str

    challenge: str

    timestamp: str

    authentication_proof: str



    def to_dict(self) -> dict:
        """
        Convert request object into dictionary.

        Used when processing or logging data.
        """

        return {

            "protocol_version":
                self.protocol_version,


            "message_type":
                self.message_type,


            "request_id":
                self.request_id,


            "device_id":
                self.device_id,


            "challenge":
                self.challenge,


            "timestamp":
                self.timestamp,


            "authentication_proof":
                self.authentication_proof

        }