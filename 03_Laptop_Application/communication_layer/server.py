"""
Fingerprint Laptop Unlock System

Communication Server

Handles:
- Android TCP connections
- JSON message receiving
- Message routing
- Response sending

Version:
2.0
"""


import socket
import json
import logging



from communication_layer.message_handler import (
    MessageHandler
)





class CommunicationServer:
    """
    TCP communication server.
    """



    def __init__(
        self,
        authentication_manager,
        pairing_manager=None,
        host="0.0.0.0",
        port=8080
    ):


        self.host = host

        self.port = port



        self.server_socket = None

        self.running = False



        self.message_handler = MessageHandler(

            authentication_manager,

            pairing_manager

        )





    def start(self):
        """
        Start TCP server.
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


                    break



        except Exception as error:


            logging.error(

                "Server start error: %s",

                error

            )



        finally:


            self.stop()





    def handle_client(
        self,
        client_socket
    ):
        """
        Receive and process Android messages.
        """


        try:


            data = client_socket.recv(

                4096

            )



            if not data:


                return



            message = json.loads(

                data.decode(

                    "utf-8"

                )

            )



            logging.info(

                "Received message: %s",

                message

            )



            response = self.message_handler.handle(

                message

            )



            client_socket.send(

                (
                    json.dumps(response)
                    + "\n"

                ).encode(

                    "utf-8"

                )

            )



            logging.info(

                "Response sent: %s",

                response

            )



        except Exception as error:


            logging.error(

                "Communication error: %s",

                error

            )



            error_response = {


                "protocol_version":
                    "1.0",


                "message_type":
                    "ERROR",


                "status":
                    "ERROR",


                "error_code":
                    "E003"

            }



            try:


                client_socket.send(

                    json.dumps(

                        error_response

                    ).encode(

                        "utf-8"

                    )

                )


            except Exception:


                pass



        finally:


            client_socket.close()





    def stop(self):
        """
        Stop server.
        """


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