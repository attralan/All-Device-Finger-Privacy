package com.example.fingerprintunlock

data class PairingResponse(
    val protocolVersion: String,
    val messageType: String,
    val requestId: String,
    val status: String,
    val errorCode: String?,
    val timestamp: Long
)