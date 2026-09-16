"""
Fingerprint Laptop Unlock System

Database Models

Defines database table structures.

Database:
SQLite

Version:
1.0
"""



class DatabaseTables:
    """
    Contains database table names.
    """



    TRUSTED_DEVICES = (
        "trusted_devices"
    )


    SECURITY_KEYS = (
        "security_keys"
    )


    AUTHENTICATION_LOGS = (
        "authentication_logs"
    )





class TrustedDeviceModel:
    """
    Trusted device table model.
    """


    TABLE_NAME = (
        DatabaseTables.TRUSTED_DEVICES
    )


    COLUMNS = {

        "id":
            "INTEGER PRIMARY KEY AUTOINCREMENT",

        "device_id":
            "TEXT UNIQUE NOT NULL",

        "device_name":
            "TEXT NOT NULL",

        "public_key":
            "TEXT NOT NULL",

        "created_at":
            "TEXT NOT NULL",

        "enabled":
            "INTEGER DEFAULT 1"
    }





class SecurityKeyModel:
    """
    Security key table model.
    """


    TABLE_NAME = (
        DatabaseTables.SECURITY_KEYS
    )


    COLUMNS = {

        "id":
            "INTEGER PRIMARY KEY AUTOINCREMENT",

        "device_id":
            "TEXT UNIQUE NOT NULL",

        "encryption_key":
            "TEXT NOT NULL",

        "created_at":
            "TEXT NOT NULL"
    }





class AuthenticationLogModel:
    """
    Authentication log table model.
    """


    TABLE_NAME = (
        DatabaseTables.AUTHENTICATION_LOGS
    )


    COLUMNS = {

        "id":
            "INTEGER PRIMARY KEY AUTOINCREMENT",

        "request_id":
            "TEXT NOT NULL",

        "device_id":
            "TEXT NOT NULL",

        "status":
            "TEXT NOT NULL",

        "error_code":
            "TEXT",

        "timestamp":
            "TEXT NOT NULL"
    }