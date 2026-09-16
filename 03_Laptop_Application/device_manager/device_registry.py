"""
Fingerprint Laptop Unlock System

Device Registry

Manages trusted Android devices.

Version:
2.0
"""


import logging





class DeviceRegistry:
    """
    Handles trusted device registration.
    """



    def __init__(
        self,
        database
    ):

        self.database = database



    def register_device(
        self,
        device_id,
        device_name,
        public_key
    ):
        """
        Register a new trusted device.
        """

        try:

            self.database.add_device(

                device_id,

                device_name,

                public_key

            )


            logging.info(

                "Device registered: %s",

                device_id

            )


            return True



        except Exception as error:


            logging.error(

                "Device registration failed: %s",

                error

            )


            return False





    def device_exists(
        self,
        device_id
    ):
        """
        Check device existence.
        """


        try:

            return self.database.device_exists(

                device_id

            )


        except Exception as error:


            logging.error(

                "Device check failed: %s",

                error

            )


            return False





    def get_device(
        self,
        device_id
    ):
        """
        Get single device.
        """


        try:

            return self.database.get_device(

                device_id

            )


        except Exception as error:


            logging.error(

                "Device loading failed: %s",

                error

            )


            return None





    def get_all_devices(self):
        """
        Get all trusted devices.

        Used by GUI.
        """

        try:

            return self.database.get_all_devices()



        except Exception as error:


            logging.error(

                "Loading devices failed: %s",

                error

            )


            return []





    def remove_device(
        self,
        device_id
    ):
        """
        Remove trusted device.
        """

        try:

            self.database.remove_device(

                device_id

            )


            logging.info(

                "Device removed: %s",

                device_id

            )


            return True



        except Exception as error:


            logging.error(

                "Device removal failed: %s",

                error

            )


            return False