"""
Fingerprint Laptop Unlock System

Windows Session Manager

Handles Windows user session information.

Version:
1.0
"""


import logging
import os
import socket

from dataclasses import dataclass
from datetime import datetime



@dataclass
class WindowsSession:
    """
    Represents current Windows session.
    """


    username: str

    computer_name: str

    session_time: str

    active: bool



class SessionManager:
    """
    Manages Windows session information.
    """



    def __init__(self):

        self.session = None



    def get_current_session(
        self
    ) -> WindowsSession:
        """
        Get current Windows user session.
        """


        username = (
            os.getlogin()
        )


        computer_name = (
            socket.gethostname()
        )


        session = WindowsSession(

            username=username,

            computer_name=computer_name,

            session_time=datetime.now()
            .isoformat(),

            active=True

        )


        self.session = session



        logging.info(
            "Windows session detected: %s",
            username
        )


        return session



    def is_session_active(
        self
    ) -> bool:
        """
        Check whether Windows session exists.
        """


        return (
            self.session is not None
            and
            self.session.active
        )



    def close_session(
        self
    ):
        """
        Mark session inactive.
        """


        if self.session:

            self.session.active = False


            logging.info(
                "Windows session closed"
            )