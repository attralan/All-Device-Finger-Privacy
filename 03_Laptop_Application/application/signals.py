"""
Fingerprint Laptop Unlock System

Qt Signal Manager

Used for communication between:
Backend threads and GUI.

Version:
1.0
"""


from PySide6.QtCore import QObject, Signal




class ApplicationSignals(QObject):
    """
    Global GUI update signals.
    """


    server_started = Signal()

    server_stopped = Signal()

    authentication_success = Signal(str)

    authentication_failed = Signal(str)

    device_connected = Signal(str)

    log_message = Signal(str)