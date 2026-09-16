"""
Fingerprint Laptop Unlock System

Unlock Manager

Controls Windows unlock workflow.

Version:
1.0
"""


import logging


from windows_integration.windows_api import (
    WindowsAPI
)


from windows_integration.session_manager import (
    SessionManager
)



class UnlockManager:
    """
    Manages Windows unlock operations.
    """



    def __init__(
        self,
        windows_api: WindowsAPI,
        session_manager: SessionManager
    ):

        self.windows_api = (
            windows_api
        )


        self.session_manager = (
            session_manager
        )



    def unlock(
        self
    ) -> bool:
        """
        Start unlock process.

        Returns:

        True:
            Unlock successful

        False:
            Unlock failed
        """



        logging.info(
            "Unlock request received"
        )



        # Check operating system

        if not self.windows_api.is_windows():

            logging.error(
                "Unsupported operating system"
            )

            return False



        # Check session

        if not self.session_manager.is_session_active():

            logging.warning(
                "No active Windows session"
            )

            return False



        # Execute Windows unlock

        result = (
            self.windows_api
            .execute_unlock_action()
        )



        if result:

            logging.info(
                "Windows unlock successful"
            )

        else:

            logging.error(
                "Windows unlock failed"
            )


        return result