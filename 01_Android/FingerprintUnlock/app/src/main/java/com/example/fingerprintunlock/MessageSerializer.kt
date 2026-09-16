package com.example.fingerprintunlock

import org.json.JSONObject

object MessageSerializer {

    fun serializePairingRequest(
        request: PairingRequest
    ): String {

        val json = JSONObject()

        json.put(
            "protocol_version",
            request.protocolVersion
        )

        json.put(
            "message_type",
            request.messageType
        )

        json.put(
            "request_id",
            request.requestId
        )

        json.put(
            "device_id",
            request.deviceId
        )

        json.put(
            "public_key",
            request.publicKey
        )

        json.put(
            "timestamp",
            request.timestamp
        )

        return json.toString()
    }
}