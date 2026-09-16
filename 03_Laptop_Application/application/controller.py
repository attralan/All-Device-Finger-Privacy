"""
Fingerprint Laptop Unlock System

Application Controller

Version:
6.0
"""


import logging
import threading



from application.state_manager import StateManager


from application.signals import ApplicationSignals


from application.log_manager import LogManager





class ApplicationController:


    def __init__(
        self,
        communication_server=None,
        device_registry=None,
        pairing_manager=None
    ):


        self.communication_server = communication_server


        self.device_registry = device_registry


        self.pairing_manager = pairing_manager



        self.state = StateManager()


        self.signals = ApplicationSignals()


        self.log_manager = LogManager()



        self.server_thread = None





    # ==========================
    # Server
    # ==========================


    def start_server(self):


        if not self.communication_server:


            return



        if self.server_thread and self.server_thread.is_alive():


            return



        self.server_thread = threading.Thread(

            target=self.communication_server.start,

            daemon=True

        )


        self.server_thread.start()



        self.state.set_server_status(True)


        self.signals.server_started.emit()


        self.log_manager.send_log(

            "Communication server started"

        )





    def stop_server(self):


        if self.communication_server:


            self.communication_server.stop()



        self.state.set_server_status(False)


        self.signals.server_stopped.emit()


        self.log_manager.send_log(

            "Communication server stopped"

        )





    # ==========================
    # Devices
    # ==========================


    def get_devices(self):


        if not self.device_registry:


            return []



        return self.device_registry.get_all_devices()





    def remove_device(
        self,
        device_id
    ):


        if not self.device_registry:


            return False



        result = self.device_registry.remove_device(

            device_id

        )



        if result:


            self.log_manager.send_log(

                f"Device removed: {device_id}"

            )



        return result





    def pair_device(
        self,
        device_id,
        device_name,
        public_key
    ):
        """
        Add new trusted device.
        """


        if not self.pairing_manager:


            return False



        result = self.pairing_manager.pair_device(

            device_id,

            device_name,

            public_key

        )



        if result:


            self.log_manager.send_log(

                f"Device paired: {device_id}"

            )



        return result





    def get_status(self):

        return self.state.get_state()