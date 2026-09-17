"""
Fingerprint Laptop Unlock System

GUI Application Entry Point

Initializes:
- Database
- Device Management
- Security
- Authentication
- Communication Server
- GUI

Version:
5.0
"""


import sys
import logging



from PySide6.QtWidgets import QApplication



from gui.main_window import MainWindow


from gui.styles import AppStyle



from application.controller import (
    ApplicationController
)



from database import (
    DatabaseManager
)



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





def create_backend():
    """
    Create backend services.
    """



    # ======================
    # Database
    # ======================


    database = DatabaseManager()


    database.connect()


    database.create_tables()



    logging.info(

        "Database initialized"

    )





    # ======================
    # Device Management
    # ======================


    device_registry = DeviceRegistry(

        database

    )


    pairing_manager = PairingManager(

        device_registry

    )



    logging.info(

        "Device manager initialized"

    )





    # ======================
    # Security
    # ======================


    key_manager = KeyManager(

        database

    )


    proof_verifier = ProofVerifier(

        key_manager

    )


    replay_protection = ReplayProtection(

        database

    )





    # ======================
    # Windows
    # ======================


    windows_api = WindowsAPI()


    session_manager = SessionManager()


    session_manager.get_current_session()



    unlock_manager = UnlockManager(

        windows_api,

        session_manager

    )





    # ======================
    # Authentication
    # ======================


    authentication_manager = AuthenticationManager(

        RequestValidator(),

        device_registry,

        proof_verifier,

        replay_protection,

        ResultHandler(),

        unlock_manager

    )





    # ======================
    # Communication
    # ======================


    communication_server = CommunicationServer(

        authentication_manager,

        pairing_manager

    )



    logging.info(

        "Communication initialized"

    )



    return (

        communication_server,

        device_registry,

        pairing_manager

    )







def main():



    logging.basicConfig(

        level=logging.INFO,

        format=

        "%(asctime)s | %(levelname)s | %(message)s"

    )



    app = QApplication(

        sys.argv

    )



    app.setStyleSheet(

        AppStyle.DARK_THEME

    )



    (
        communication_server,

        device_registry,

        pairing_manager

    ) = create_backend()





    controller = ApplicationController(

        communication_server,

        device_registry,

        pairing_manager

    )





    window = MainWindow(

        controller

    )


    window.show()



    logging.info(

        "GUI started"

    )



    sys.exit(

        app.exec()

    )







if __name__ == "__main__":

    main()