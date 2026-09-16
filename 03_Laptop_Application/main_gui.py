"""
Fingerprint Laptop Unlock System

GUI Application Entry Point

Version:
3.0
"""


import sys
import logging



from PySide6.QtWidgets import QApplication



from gui.main_window import MainWindow


from gui.styles import AppStyle



from application.controller import (
    ApplicationController
)



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





def create_backend():



    database = DatabaseManager()


    database.connect()


    database.create_tables()



    device_registry = DeviceRegistry(

        database

    )


    PairingManager(

        device_registry

    )



    key_manager = KeyManager(

        database

    )


    proof_verifier = ProofVerifier(

        key_manager

    )


    replay_protection = ReplayProtection(

        database

    )



    windows_api = WindowsAPI()


    session_manager = SessionManager()


    session_manager.get_current_session()



    unlock_manager = UnlockManager(

        windows_api,

        session_manager

    )



    authentication_manager = AuthenticationManager(

        RequestValidator(),

        device_registry,

        proof_verifier,

        replay_protection,

        ResultHandler(),

        unlock_manager

    )



    server = CommunicationServer(

        authentication_manager

    )



    return (

        server,

        device_registry

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



    communication_server, device_registry = create_backend()



    controller = ApplicationController(

        communication_server,

        device_registry

    )



    window = MainWindow(

        controller

    )


    window.show()



    sys.exit(

        app.exec()

    )







if __name__ == "__main__":

    main()