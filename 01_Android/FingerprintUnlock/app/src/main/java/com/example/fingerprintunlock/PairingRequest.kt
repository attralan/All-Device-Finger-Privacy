package com.example.fingerprintunlock

data class PairingRequest(
    val protocolVersion: String,
    val messageType: String,
    val requestId: String,
    val deviceId: String,
    val publicKey: String,
    val timestamp: Long
)