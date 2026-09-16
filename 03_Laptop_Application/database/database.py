"""
Fingerprint Laptop Unlock System

Database Manager

SQLite storage layer.

Version:
2.0
"""


import sqlite3
import logging





class DatabaseManager:
    """
    Handles SQLite database operations.
    """



    def __init__(
        self,
        path="fingerprint_unlock.db"
    ):


        self.path = path

        self.connection = None





    def connect(self):
        """
        Connect database.
        """


        self.connection = sqlite3.connect(

            self.path,

            check_same_thread=False

        )


        logging.info(

            "Database connected"

        )





    def close(self):
        """
        Close database.
        """


        if self.connection:


            self.connection.close()



            logging.info(

                "Database closed"

            )





    def create_tables(self):
        """
        Create database tables.
        """


        cursor = self.connection.cursor()



        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS devices
            (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                device_id TEXT UNIQUE,

                device_name TEXT,

                public_key TEXT,

                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
            """
        )



        self.connection.commit()



        logging.info(

            "Database tables created"

        )





    def add_device(
        self,
        device_id,
        device_name,
        public_key
    ):
        """
        Add trusted device.
        """


        cursor = self.connection.cursor()



        cursor.execute(

            """
            INSERT OR REPLACE INTO devices
            (
                device_id,
                device_name,
                public_key
            )

            VALUES
            (
                ?,
                ?,
                ?
            )

            """,

            (
                device_id,
                device_name,
                public_key
            )

        )



        self.connection.commit()





    def device_exists(
        self,
        device_id
    ):


        cursor = self.connection.cursor()



        cursor.execute(

            """
            SELECT device_id
            FROM devices
            WHERE device_id=?

            """,

            (
                device_id,
            )

        )



        return cursor.fetchone() is not None





    def get_device(
        self,
        device_id
    ):


        cursor = self.connection.cursor()



        cursor.execute(

            """
            SELECT *
            FROM devices
            WHERE device_id=?

            """,

            (
                device_id,
            )

        )



        return cursor.fetchone()





    def get_all_devices(self):
        """
        Return all devices.
        """


        cursor = self.connection.cursor()



        cursor.execute(

            """
            SELECT *
            FROM devices

            """

        )



        return cursor.fetchall()





    def remove_device(
        self,
        device_id
    ):


        cursor = self.connection.cursor()



        cursor.execute(

            """
            DELETE FROM devices
            WHERE device_id=?

            """,

            (
                device_id,
            )

        )



        self.connection.commit()