"""
Fingerprint Laptop Unlock System

Log Manager

Handles application log messages
for GUI display.

Version:
1.0
"""


from PySide6.QtCore import QObject, Signal




class LogManager(QObject):
    """
    Central logging signal manager.
    """


    log_received = Signal(str)



    def __init__(self):

        super().__init__()



    def send_log(
        self,
        message
    ):
        """
        Send log message to GUI.
        """


        self.log_received.emit(
            message
        )