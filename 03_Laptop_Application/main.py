"""
Fingerprint Laptop Unlock System

Backend Entry Point

Version:
3.0
"""


import logging
import signal
import sys



from database import DatabaseManager


from device_manager import (
    DeviceRegistry,
    PairingManager
)


from security_layer import (
    KeyManager,
    ProofVerifier,
    ReplayProtection
)


from windows_integration import (
    WindowsAPI,
    SessionManager,
    UnlockManager
)


from authentication_service import (
    AuthenticationManager,
    RequestValidator,
    ResultHandler
)


from communication_layer import (
    CommunicationServer
)





class LaptopUnlockBackend:


    def __init__(self):

        self.database = None

        self.communication_server = None

        self.running = False




    def initialize(self):

        logging.info(
            "Initializing backend"
        )


        # Database

        self.database = DatabaseManager()

        self.database.connect()

        self.database.create_tables()



        # Devices

        device_registry = DeviceRegistry(

            self.database

        )


        PairingManager(
            device_registry
        )



        # Security

        key_manager = KeyManager(

            self.database

        )


        proof_verifier = ProofVerifier(

            key_manager

        )


        replay_protection = ReplayProtection(

            self.database

        )



        # Windows

        windows_api = WindowsAPI()


        session_manager = SessionManager()


        session_manager.get_current_session()



        unlock_manager = UnlockManager(

            windows_api,

            session_manager

        )



        # Authentication

        authentication_manager = AuthenticationManager(

            RequestValidator(),

            device_registry,

            proof_verifier,

            replay_protection,

            ResultHandler(),

            unlock_manager

        )



        # Communication

        self.communication_server = CommunicationServer(

            authentication_manager

        )


        logging.info(
            "Backend initialized"
        )





    def start(self):


        self.initialize()


        self.running = True


        logging.info(
            "Backend started"
        )


        self.communication_server.start()





    def shutdown(self):


        logging.info(
            "Backend shutting down"
        )


        if self.communication_server:

            self.communication_server.stop()



        if self.database:

            self.database.close()



        sys.exit(0)







backend = LaptopUnlockBackend()




def shutdown_handler(
    signal_number,
    frame
):

    backend.shutdown()





signal.signal(

    signal.SIGINT,

    shutdown_handler

)





if __name__ == "__main__":


    logging.basicConfig(

        level=logging.INFO,

        format=
        "%(asctime)s | %(levelname)s | %(message)s"

    )


    backend.start()