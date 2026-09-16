"""
Fingerprint Laptop Unlock System

Replay Protection

Prevents reuse of previously processed
authentication requests.

Uses persistent database storage.

Version:
1.0
"""


import logging

from datetime import datetime, timezone


from database.database import (
    DatabaseManager
)


from database.models import (
    AuthenticationLogModel
)



class ReplayProtection:
    """
    Provides replay attack protection.
    """



    def __init__(
        self,
        database: DatabaseManager
    ):

        self.database = database



    def is_replay(
        self,
        request_id: str
    ) -> bool:
        """
        Check if request was already processed.
        """


        query = f"""

        SELECT

            request_id

        FROM

            {AuthenticationLogModel.TABLE_NAME}

        WHERE

            request_id = ?

        """



        result = self.database.execute(

            query,

            (
                request_id,
            )

        ).fetchone()



        return result is not None



    def register_request(
        self,
        request_id: str,
        device_id: str,
        status: str,
        error_code: str | None = None
    ):
        """
        Store authentication attempt.
        """


        query = f"""

        INSERT INTO

        {AuthenticationLogModel.TABLE_NAME}

        (

            request_id,

            device_id,

            status,

            error_code,

            timestamp

        )

        VALUES

        (

            ?,

            ?,

            ?,

            ?,

            ?

        )

        """



        self.database.execute(

            query,

            (

                request_id,

                device_id,

                status,

                error_code,

                datetime.now(
                    timezone.utc
                )
                .isoformat()

            )

        )



        logging.info(
            "Authentication request logged: %s",
            request_id
        )



    def validate_request(
        self,
        request_id: str
    ) -> bool:
        """
        Validate request freshness.

        Returns:

        True:
            New request

        False:
            Replay detected
        """


        if self.is_replay(
            request_id
        ):


            logging.warning(
                "Replay detected: %s",
                request_id
            )


            return False



        return True