package com.example.fingerprintunlock

import org.json.JSONObject

object PairingResponseParser {

    fun parse(
        jsonString: String
    ): PairingResponse? {

        return try {
            val json = JSONObject(jsonString)

            val protocolVersion =
                json.getString("protocol_version")

            val messageType =
                json.getString("message_type")

            val requestId =
                json.getString("request_id")

            val status =
                json.getString("status")

            val errorCode =
                if (json.has("error_code") &&
                    !json.isNull("error_code")
                ) {
                    json.getString("error_code")
                } else {
                    null
                }

            val timestamp =
                json.getLong("timestamp")

            PairingResponse(
                protocolVersion = protocolVersion,
                messageType = messageType,
                requestId = requestId,
                status = status,
                errorCode = errorCode,
                timestamp = timestamp
            )

        } catch (_: Exception) {
            null
        }
    }
}