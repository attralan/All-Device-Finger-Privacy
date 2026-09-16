"""
Fingerprint Laptop Unlock System

Device Management Package

Responsible for:

- Trusted device management
- Android-Laptop pairing
- Device verification

Version:
1.0
"""


from device_manager.device_registry import (
    DeviceRegistry
)


from device_manager.pairing_manager import (
    PairingManager
)



__all__ = [

    "DeviceRegistry",

    "PairingManager"

]