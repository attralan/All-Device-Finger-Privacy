"""
Fingerprint Laptop Unlock System

Pairing Manager

Handles trusted device pairing.

Version:
2.0
"""


import logging



class PairingManager:
    """
    Handles new device registration.
    """



    def __init__(
        self,
        device_registry
    ):

        self.device_registry = device_registry





    def pair_device(
        self,
        device_id,
        device_name,
        public_key
    ):
        """
        Add a trusted device.
        """

        try:


            result = self.device_registry.register_device(

                device_id,

                device_name,

                public_key

            )



            if result:


                logging.info(

                    "Device paired: %s",

                    device_id

                )



            return result



        except Exception as error:


            logging.error(

                "Pairing failed: %s",

                error

            )


            return False