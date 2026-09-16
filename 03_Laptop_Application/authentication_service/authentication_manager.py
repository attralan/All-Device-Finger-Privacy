"""
Fingerprint Laptop Unlock System

Authentication Manager

Controls complete authentication workflow.

Flow:

Request
 |
Validator
 |
Device Check
 |
Replay Protection
 |
Proof Verification
 |
Windows Unlock
 |
Response

Version:
1.0
"""


import logging



from protocol import (
    Status,
    ErrorCode
)



class AuthenticationManager:
    """
    Main authentication controller.
    """



    def __init__(
        self,
        validator,
        device_registry,
        proof_verifier,
        replay_protection,
        result_handler,
        unlock_manager
    ):


        self.validator = validator

        self.device_registry = (
            device_registry
        )

        self.proof_verifier = (
            proof_verifier
        )

        self.replay_protection = (
            replay_protection
        )

        self.result_handler = (
            result_handler
        )

        self.unlock_manager = (
            unlock_manager
        )



    def authenticate(
        self,
        request
    ):
        """
        Authenticate Android device request.
        """


        logging.info(
            "Authentication request received: %s",
            request.request_id
        )


        # -----------------------
        # 1. Validate Request
        # -----------------------

        if not self.validator.validate(request):

            return self.result_handler.create_failure_response(

                request.request_id,

                ErrorCode.INVALID_REQUEST.value

            )



        # -----------------------
        # 2. Check Device
        # -----------------------

        if not self.device_registry.verify_device(

            request.device_id

        ):


            return self.result_handler.create_failure_response(

                request.request_id,

                ErrorCode.UNKNOWN_DEVICE.value

            )



        # -----------------------
        # 3. Replay Protection
        # -----------------------

        if not self.replay_protection.validate_request(

            request.request_id

        ):


            return self.result_handler.create_failure_response(

                request.request_id,

                ErrorCode.EXPIRED_REQUEST.value

            )



        # -----------------------
        # 4. Verify Proof
        # -----------------------

        if not self.proof_verifier.verify(

            request

        ):


            return self.result_handler.create_failure_response(

                request.request_id,

                ErrorCode.SECURITY_VERIFICATION_FAILED.value

            )



        # -----------------------
        # 5. Unlock Windows
        # -----------------------

        unlock_result = (
            self.unlock_manager.unlock()
        )



        if not unlock_result:


            return self.result_handler.create_failure_response(

                request.request_id,

                ErrorCode.AUTHENTICATION_FAILED.value

            )



        logging.info(
            "Authentication successful"
        )



        return self.result_handler.create_success_response(

            request.request_id

        )