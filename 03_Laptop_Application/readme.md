03_Laptop_Application
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env
├── main.py
│
├── communication_layer
│   ├── __init__.py
│   ├── server.py
│   ├── connection_manager.py
│   ├── message_parser.py
│   └── response_sender.py
│
├── protocol
│   ├── __init__.py
│   ├── message_types.py
│   ├── status.py
│   ├── error_codes.py
│   ├── request_model.py
│   └── response_model.py
│
├── authentication_service
│   ├── __init__.py
│   ├── authentication_manager.py
│   ├── request_validator.py
│   └── result_handler.py
│
├── security_layer
│   ├── __init__.py
│   ├── encryption.py
│   ├── key_manager.py
│   ├── proof_verifier.py
│   └── replay_protection.py
│
├── device_manager
│   ├── __init__.py
│   ├── device_registry.py
│   └── pairing_manager.py
│
├── database
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   └── fingerprint_system.db
│
├── windows_integration
│   ├── __init__.py
│   ├── unlock_manager.py
│   ├── windows_api.py
│   └── session_manager.py
│
├── config
│   ├── config.json
│   ├── devices.json
│   └── security.json
│
├── logs
│   └── system.log
│
└── tests
    ├── test_server.py
    ├── test_authentication.py
    ├── test_security.py
    └── test_unlock.py
