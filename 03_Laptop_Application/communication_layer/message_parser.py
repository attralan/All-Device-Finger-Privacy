"""
Fingerprint Laptop Unlock System

Message Parser

Converts received JSON messages into
protocol objects.

Version:
1.0
"""


import logging


from protocol import (
    AuthenticationRequest
)



class MessageParser:
    """
    Converts JSON dictionaries into
    protocol request objects.
    """



    def parse_authentication_request(
        self,
        data: dict
    ) -> AuthenticationRequest:
        """
        Convert dictionary to
        AuthenticationRequest.
        """


        try:

            request = AuthenticationRequest(

                protocol_version=
                    data.get(
                        "protocol_version"
                    ),


                message_type=
                    data.get(
                        "message_type"
                    ),


                request_id=
                    data.get(
                        "request_id"
                    ),


                device_id=
                    data.get(
                        "device_id"
                    ),


                challenge=
                    data.get(
                        "challenge"
                    ),


                timestamp=
                    data.get(
                        "timestamp"
                    ),


                authentication_proof=
                    data.get(
                        "authentication_proof"
                    )

            )


            return request



        except Exception as error:


            logging.error(
                "Message parsing failed: %s",
                error
            )


            raise