package com.example.fingerprintunlock

import java.util.UUID

class PairingRequestBuilder(
    private val keyStoreManager: AndroidKeyStoreManager
) {

    fun build(deviceId: String): PairingRequest {
        val requestId = UUID.randomUUID().toString()

        val publicKey = keyStoreManager.getPublicKeyBase64()

        return PairingRequest(
            protocolVersion = "1.0",
            messageType = "PAIRING_REQUEST",
            requestId = requestId,
            deviceId = deviceId,
            publicKey = publicKey,
            timestamp = System.currentTimeMillis()
        )
    }
}