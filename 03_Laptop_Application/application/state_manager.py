"""
Fingerprint Laptop Unlock System

Application State Manager

Stores runtime application state.
"""


class StateManager:
    """
    Global application state.
    """

    def __init__(self):

        self.server_running = False

        self.connected_devices = 0

        self.last_authentication = None

        self.system_status = "READY"



    def set_server_status(
        self,
        status
    ):

        self.server_running = status



    def set_device_count(
        self,
        count
    ):

        self.connected_devices = count



    def set_last_authentication(
        self,
        value
    ):

        self.last_authentication = value



    def get_state(self):

        return {

            "server_running":
                self.server_running,

            "connected_devices":
                self.connected_devices,

            "last_authentication":
                self.last_authentication,

            "system_status":
                self.system_status

        }