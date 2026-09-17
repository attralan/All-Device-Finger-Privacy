"""
Fingerprint Laptop Unlock System

Communication Message Handler

Handles:
- PAIRING_REQUEST
- AUTHENTICATION_REQUEST

Version:
1.0
"""


import logging





class MessageHandler:


    def __init__(
        self,
        authentication_manager,
        pairing_manager
    ):


        self.authentication_manager = (
            authentication_manager
        )


        self.pairing_manager = (
            pairing_manager
        )





    def handle(
        self,
        message
    ):
        """
        Process incoming JSON message.
        """


        message_type = message.get(
            "message_type"
        )



        if message_type == "PAIRING_REQUEST":


            return self.handle_pairing(
                message
            )



        elif message_type == "AUTHENTICATION_REQUEST":


            return self.handle_authentication(
                message
            )



        else:


            return {

                "protocol_version":"1.0",

                "message_type":
                    "ERROR",

                "status":
                    "ERROR",

                "error_code":
                    "E003"

            }





    def handle_pairing(
        self,
        message
    ):


        try:


            result = self.pairing_manager.pair_device(

                message.get(
                    "device_id"
                ),

                message.get(
                    "device_name",
                    "Android Device"
                ),

                message.get(
                    "public_key"
                )

            )



            if result:


                return {

                    "protocol_version":"1.0",

                    "message_type":
                        "PAIRING_RESPONSE",

                    "request_id":
                        message.get(
                            "request_id"
                        ),

                    "status":
                        "CONNECTED"

                }



            else:


                return {

                    "protocol_version":"1.0",

                    "message_type":
                        "PAIRING_RESPONSE",

                    "request_id":
                        message.get(
                            "request_id"
                        ),

                    "status":
                        "REJECTED",

                    "error_code":
                        "E002"

                }



        except Exception as error:


            logging.error(
                "Pairing error: %s",
                error
            )


            return {

                "protocol_version":"1.0",

                "message_type":
                    "PAIRING_RESPONSE",

                "request_id":
                    message.get(
                        "request_id"
                    ),

                "status":
                    "ERROR",

                "error_code":
                    "E003"

            }





    def handle_authentication(
        self,
        message
    ):

        request = (
            message
        )


        response = self.authentication_manager.authenticate(

            request

        )


        return response