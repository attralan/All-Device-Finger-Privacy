"""
Fingerprint Laptop Unlock System

Encryption Service

Provides symmetric encryption and
decryption functionality.

Technology:
AES-256 Fernet Encryption

Version:
1.0
"""


import logging

from cryptography.fernet import Fernet, InvalidToken



class EncryptionManager:
    """
    Handles encryption and decryption.

    Uses Fernet symmetric encryption.

    Same key is required for:
    - Encryption
    - Decryption
    """



    def __init__(
        self,
        key: bytes
    ):
        """
        Initialize encryption manager.

        Args:
            key:
                Encryption key generated
                by Fernet
        """


        self.cipher = Fernet(
            key
        )



    def encrypt(
        self,
        data: str
    ) -> str:
        """
        Encrypt plaintext data.

        Args:
            data:
                Original message

        Returns:
            Encrypted string
        """


        try:

            encrypted_data = (
                self.cipher
                .encrypt(
                    data.encode("utf-8")
                )
            )


            return encrypted_data.decode(
                "utf-8"
            )



        except Exception as error:

            logging.error(
                "Encryption failed: %s",
                error
            )

            raise



    def decrypt(
        self,
        encrypted_data: str
    ) -> str:
        """
        Decrypt encrypted message.

        Args:
            encrypted_data:
                Encrypted string

        Returns:
            Original message
        """


        try:

            decrypted_data = (
                self.cipher
                .decrypt(
                    encrypted_data.encode(
                        "utf-8"
                    )
                )
            )


            return decrypted_data.decode(
                "utf-8"
            )



        except InvalidToken:

            logging.error(
                "Invalid encryption token"
            )

            raise ValueError(
                "Unable to decrypt message"
            )



        except Exception as error:

            logging.error(
                "Decryption failed: %s",
                error
            )

            raise



    @staticmethod
    def generate_key() -> bytes:
        """
        Generate new encryption key.

        Used during device pairing.
        """


        return Fernet.generate_key()