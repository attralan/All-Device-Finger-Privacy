"""
Fingerprint Laptop Unlock System

Connection Manager

Responsible for managing active
Android device connections.

Protocol Reference:
00_Common/Communication_Protocol.md

Version:
1.0
"""


import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional

from protocol.status import Status



@dataclass
class DeviceConnection:
    """
    Represents one connected device.
    """

    device_id: str

    address: str

    connected_at: str

    status: Status




class ConnectionManager:
    """
    Manages Android device connections.

    Responsibilities:

    - Add connections
    - Remove connections
    - Check connection status
    - Track connected devices
    """


    def __init__(self):

        self.connections: Dict[
            str,
            DeviceConnection
        ] = {}



    def add_connection(
        self,
        device_id: str,
        address: str
    ) -> bool:
        """
        Register a new device connection.

        Returns:
            True if added successfully
        """


        if device_id in self.connections:

            logging.warning(
                "Device already connected: %s",
                device_id
            )

            return False



        connection = DeviceConnection(

            device_id=device_id,

            address=address,

            connected_at=(
                datetime.now()
                .isoformat()
            ),

            status=Status.CONNECTED
        )


        self.connections[
            device_id
        ] = connection



        logging.info(
            "Device connected: %s",
            device_id
        )


        return True



    def remove_connection(
        self,
        device_id: str
    ) -> bool:
        """
        Remove device connection.
        """


        if device_id not in self.connections:

            logging.warning(
                "Device not found: %s",
                device_id
            )

            return False



        self.connections.pop(
            device_id
        )


        logging.info(
            "Device disconnected: %s",
            device_id
        )


        return True



    def update_status(
        self,
        device_id: str,
        status: Status
    ) -> bool:
        """
        Update device connection status.
        """


        connection = (
            self.connections.get(
                device_id
            )
        )


        if not connection:

            logging.error(
                "Cannot update unknown device: %s",
                device_id
            )

            return False



        connection.status = status


        logging.info(
            "Device %s status changed to %s",
            device_id,
            status
        )


        return True



    def get_connection(
        self,
        device_id: str
    ) -> Optional[DeviceConnection]:
        """
        Get connection details.
        """


        return self.connections.get(
            device_id
        )



    def is_connected(
        self,
        device_id: str
    ) -> bool:
        """
        Check whether device is connected.
        """


        return device_id in self.connections



    def get_all_connections(
        self
    ) -> Dict[str, DeviceConnection]:
        """
        Return all active connections.
        """


        return self.connections