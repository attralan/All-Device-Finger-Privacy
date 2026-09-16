"""
Fingerprint Laptop Unlock System

Communication Server

Responsible for:
- Receiving Android authentication requests
- Parsing incoming messages
- Sending authentication responses
- Managing TCP connection lifecycle

Version:
1.1
"""


import socket
import json
import logging



from communication_layer.message_parser import (
    MessageParser
)


from communication_layer.response_sender import (
    ResponseSender
)



class CommunicationServer:
    """
    TCP communication server.
    """



    def __init__(
        self,
        authentication_manager,
        host="127.0.0.1",
        port=8080
    ):
        """
        Initialize communication server.

        Args:

            authentication_manager:
                Handles authentication workflow

            host:
                Server address

            port:
                Listening port
        """


        self.authentication_manager = (
            authentication_manager
        )


        self.host = host


        self.port = port


        self.server_socket = None


        self.running = False



        self.message_parser = MessageParser()


        self.response_sender = ResponseSender()



    def start(self):
        """
        Start communication server.
        """


        try:


            self.server_socket = socket.socket(

                socket.AF_INET,

                socket.SOCK_STREAM

            )



            self.server_socket.setsockopt(

                socket.SOL_SOCKET,

                socket.SO_REUSEADDR,

                1

            )



            self.server_socket.bind(

                (
                    self.host,
                    self.port
                )

            )



            self.server_socket.listen(5)



            # Important:
            # Allows shutdown checking

            self.server_socket.settimeout(1)



            self.running = True



            logging.info(

                "Communication server started on %s:%s",

                self.host,

                self.port

            )



            while self.running:


                try:


                    client_socket, address = (

                        self.server_socket.accept()

                    )



                    logging.info(

                        "Client connected: %s",

                        address

                    )



                    self.handle_client(

                        client_socket

                    )



                except socket.timeout:


                    continue



                except OSError:


                    if self.running:

                        logging.error(

                            "Socket error occurred"

                        )


                    break



        except Exception as error:


            logging.error(

                "Server error: %s",

                error

            )



        finally:


            self.stop()



    def handle_client(
        self,
        client_socket
    ):
        """
        Handle Android client request.
        """


        try:


            received_data = (

                client_socket.recv(
                    4096
                )

            )



            if not received_data:

                return



            json_data = json.loads(

                received_data.decode(
                    "utf-8"
                )

            )



            logging.info(

                "Received message: %s",

                json_data

            )



            request = (

                self.message_parser
                .parse_authentication_request(

                    json_data

                )

            )



            response = (

                self.authentication_manager
                .authenticate(

                    request

                )

            )



            self.response_sender.send(

                client_socket,

                response

            )



        except Exception as error:


            logging.error(

                "Communication handling error: %s",

                error

            )



            error_response = {


                "protocol_version":

                    "1.0",



                "message_type":

                    "AUTHENTICATION_RESPONSE",



                "status":

                    "ERROR",



                "error_code":

                    str(error)

            }



            try:


                client_socket.send(

                    json.dumps(
                        error_response
                    )
                    .encode(
                        "utf-8"
                    )

                )


            except Exception:


                pass



        finally:


            client_socket.close()



    def stop(self):
        """
        Stop server safely.
        """


        if not self.running:

            return



        logging.info(

            "Stopping communication server"

        )



        self.running = False



        if self.server_socket:


            try:


                self.server_socket.close()



            except Exception:


                pass



            self.server_socket = None



        logging.info(

            "Communication server stopped"

        )