package com.example.fingerprintunlock

data class AuthenticationRequest(
    val protocolVersion: String,
    val messageType: String,
    val requestId: String,
    val deviceId: String,
    val challenge: String,
    val timestamp: Long,
    val authenticationProof: String
)