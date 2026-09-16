"""
Fingerprint Laptop Unlock System

Request Validator

Validates incoming authentication requests
before security verification.

Protocol Reference:
00_Common/Communication_Protocol.md

Version:
1.0
"""


import logging
from datetime import datetime, timezone


from protocol.request_model import AuthenticationRequest
from protocol.message_types import MessageType
from protocol.error_codes import ErrorCode



class RequestValidator:
    """
    Validates authentication requests.
    """


    CURRENT_PROTOCOL_VERSION = "1.0"


    MAX_REQUEST_AGE_SECONDS = 30



    def validate(
        self,
        request: AuthenticationRequest
    ) -> tuple[bool, str | None]:
        """
        Validate authentication request.

        Returns:

        (
            validation_result,
            error_code
        )

        """


        checks = [

            self.validate_protocol_version,

            self.validate_message_type,

            self.validate_required_values,

            self.validate_timestamp

        ]


        for check in checks:

            result, error = check(request)


            if not result:

                return False, error



        return True, None



    def validate_protocol_version(
        self,
        request: AuthenticationRequest
    ) -> tuple[bool, str | None]:
        """
        Check protocol compatibility.
        """


        if (
            request.protocol_version
            !=
            self.CURRENT_PROTOCOL_VERSION
        ):

            logging.warning(
                "Protocol mismatch"
            )


            return (
                False,
                ErrorCode.PROTOCOL_MISMATCH.value
            )



        return True, None



    def validate_message_type(
        self,
        request: AuthenticationRequest
    ) -> tuple[bool, str | None]:
        """
        Check message type.
        """


        if (
            request.message_type
            !=
            MessageType.AUTHENTICATION_REQUEST.value
        ):

            logging.warning(
                "Invalid message type"
            )


            return (
                False,
                ErrorCode.INVALID_REQUEST.value
            )



        return True, None



    def validate_required_values(
        self,
        request: AuthenticationRequest
    ) -> tuple[bool, str | None]:
        """
        Check required fields.
        """


        required_values = [

            request.request_id,

            request.device_id,

            request.challenge,

            request.timestamp,

            request.authentication_proof

        ]



        if any(
            value is None or value == ""
            for value in required_values
        ):

            logging.warning(
                "Missing required values"
            )


            return (
                False,
                ErrorCode.INVALID_REQUEST.value
            )



        return True, None



    def validate_timestamp(
        self,
        request: AuthenticationRequest
    ) -> tuple[bool, str | None]:
        """
        Prevent expired requests.

        Protects against replay attacks.
        """


        try:

            request_time = datetime.fromisoformat(
                request.timestamp
            )


            current_time = datetime.now(
                timezone.utc
            )



            difference = (
                current_time
                -
                request_time
            ).total_seconds()



            if (
                abs(difference)
                >
                self.MAX_REQUEST_AGE_SECONDS
            ):

                logging.warning(
                    "Request expired"
                )


                return (
                    False,
                    ErrorCode.EXPIRED_REQUEST.value
                )



        except Exception:

            logging.warning(
                "Invalid timestamp format"
            )


            return (
                False,
                ErrorCode.INVALID_REQUEST.value
            )



        return True, None