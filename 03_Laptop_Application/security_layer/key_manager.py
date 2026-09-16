"""
Fingerprint Laptop Unlock System

Key Manager

Manages cryptographic keys using
persistent database storage.

Version:
1.0
"""


import logging

from datetime import datetime

from typing import Optional


from security_layer.encryption import (
    EncryptionManager
)


from database.database import (
    DatabaseManager
)


from database.models import (
    SecurityKeyModel
)



class KeyManager:
    """
    Manages device encryption keys.
    """



    def __init__(
        self,
        database: DatabaseManager
    ):

        self.database = database



    def generate_device_key(
        self,
        device_id: str
    ) -> bytes:
        """
        Generate and store encryption key.
        """


        existing_key = (
            self.get_device_key(
                device_id
            )
        )


        if existing_key:

            logging.warning(
                "Key already exists: %s",
                device_id
            )

            return existing_key



        key = (
            EncryptionManager
            .generate_key()
        )



        query = f"""

        INSERT INTO
        {SecurityKeyModel.TABLE_NAME}

        (
            device_id,
            encryption_key,
            created_at
        )

        VALUES
        (
            ?,
            ?,
            ?
        )

        """



        self.database.execute(

            query,

            (

                device_id,

                key.decode(
                    "utf-8"
                ),

                datetime.now()
                .isoformat()

            )

        )



        logging.info(
            "Encryption key stored: %s",
            device_id
        )


        return key



    def get_device_key(
        self,
        device_id: str
    ) -> Optional[bytes]:
        """
        Retrieve device encryption key.
        """


        query = f"""

        SELECT

            encryption_key

        FROM

            {SecurityKeyModel.TABLE_NAME}

        WHERE

            device_id = ?

        """



        result = self.database.execute(

            query,

            (
                device_id,
            )

        ).fetchone()



        if not result:

            return None



        return result[0].encode(
            "utf-8"
        )



    def remove_device_key(
        self,
        device_id: str
    ) -> bool:
        """
        Delete device encryption key.
        """


        query = f"""

        DELETE FROM

        {SecurityKeyModel.TABLE_NAME}

        WHERE

        device_id = ?

        """



        try:

            self.database.execute(

                query,

                (
                    device_id,
                )

            )


            logging.info(
                "Key removed: %s",
                device_id
            )


            return True



        except Exception as error:

            logging.error(
                "Key removal failed: %s",
                error
            )


            return False



    def has_key(
        self,
        device_id: str
    ) -> bool:
        """
        Check whether device has key.
        """


        return (
            self.get_device_key(
                device_id
            )
            is not None
        )