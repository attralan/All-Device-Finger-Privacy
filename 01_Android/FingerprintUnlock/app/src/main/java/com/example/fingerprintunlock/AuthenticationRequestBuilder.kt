package com.example.fingerprintunlock

import java.security.SecureRandom
import java.util.UUID

class AuthenticationRequestBuilder {

    private val secureRandom = SecureRandom()

    fun build(
        deviceId: String
    ): AuthenticationRequest {

        val requestId = UUID.randomUUID().toString()

        val challengeBytes = ByteArray(32)
        secureRandom.nextBytes(challengeBytes)

        val challenge = challengeBytes.joinToString("") {
            "%02x".format(it)
        }

        return AuthenticationRequest(
            protocolVersion = "1.0",
            messageType = "AUTHENTICATION_REQUEST",
            requestId = requestId,
            deviceId = deviceId,
            challenge = challenge,
            timestamp = System.currentTimeMillis(),
            authenticationProof = ""
        )
    }
}