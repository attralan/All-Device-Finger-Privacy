"""
Fingerprint Laptop Unlock System

Authentication Result Handler

Responsible for generating standard
authentication responses.

Protocol Reference:
00_Common/Communication_Protocol.md

Version:
1.0
"""


import logging


from protocol.response_model import (
    AuthenticationResponse
)

from protocol.message_types import (
    MessageType
)

from protocol.status import (
    Status
)



class ResultHandler:
    """
    Creates authentication responses.
    """



    PROTOCOL_VERSION = "1.0"



    def create_success_response(
        self,
        request_id: str
    ) -> AuthenticationResponse:
        """
        Create successful authentication response.

        Used when authentication succeeds.
        """


        logging.info(
            "Creating success response for %s",
            request_id
        )


        return AuthenticationResponse(

            protocol_version=
                self.PROTOCOL_VERSION,


            message_type=
                MessageType.AUTHENTICATION_RESPONSE.value,


            request_id=
                request_id,


            status=
                Status.AUTHENTICATED.value,


            error_code=None
        )



    def create_failure_response(
        self,
        request_id: str,
        error_code: str
    ) -> AuthenticationResponse:
        """
        Create failed authentication response.

        Used when authentication fails.
        """


        logging.warning(
            "Creating failure response for %s. Error: %s",
            request_id,
            error_code
        )


        return AuthenticationResponse(

            protocol_version=
                self.PROTOCOL_VERSION,


            message_type=
                MessageType.AUTHENTICATION_RESPONSE.value,


            request_id=
                request_id,


            status=
                Status.REJECTED.value,


            error_code=
                error_code
        )



    def create_error_response(
        self,
        request_id: str,
        error_code: str
    ) -> AuthenticationResponse:
        """
        Create system error response.

        Used for unexpected failures.
        """


        logging.error(
            "Creating error response for %s. Error: %s",
            request_id,
            error_code
        )


        return AuthenticationResponse(

            protocol_version=
                self.PROTOCOL_VERSION,


            message_type=
                MessageType.AUTHENTICATION_RESPONSE.value,


            request_id=
                request_id,


            status=
                Status.ERROR.value,


            error_code=
                error_code
        )