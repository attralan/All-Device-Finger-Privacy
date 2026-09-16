"""
Fingerprint Laptop Unlock System

Response Sender

Responsible for sending protocol-compliant
responses from Laptop to Android.

Protocol Reference:
00_Common/Communication_Protocol.md

Version:
1.0
"""


import json
import logging
import socket

from protocol.response_model import AuthenticationResponse



class ResponseSender:
    """
    Handles sending responses to Android devices.
    """



    def send(
        self,
        client_socket: socket.socket,
        response: AuthenticationResponse
    ) -> bool:
        """
        Send authentication response.

        Args:
            client_socket:
                Active client connection

            response:
                AuthenticationResponse object


        Returns:
            True if sent successfully
        """

        try:

            response_data = (
                response.to_dict()
            )


            json_message = json.dumps(
                response_data
            )


            client_socket.send(
                json_message.encode(
                    "utf-8"
                )
            )


            logging.info(
                "Response sent: %s",
                json_message
            )


            return True



        except Exception as error:

            logging.error(
                "Failed to send response: %s",
                error
            )


            return False