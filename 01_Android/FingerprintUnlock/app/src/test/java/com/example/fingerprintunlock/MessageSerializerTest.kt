package com.example.fingerprintunlock

import org.json.JSONObject
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class MessageSerializerTest {

    @Test
    fun serializePairingRequest_createsValidJson() {

        val request = PairingRequest(
            protocolVersion = "1.0",
            messageType = "PAIRING_REQUEST",
            requestId = "test-request-id",
            deviceId = "test-device",
            publicKey = "TEST_PUBLIC_KEY",
            timestamp = 123456789L
        )

        val jsonString =
            MessageSerializer.serializePairingRequest(request)

        val json = JSONObject(jsonString)

        assertEquals(
            "1.0",
            json.getString("protocol_version")
        )

        assertEquals(
            "PAIRING_REQUEST",
            json.getString("message_type")
        )

        assertEquals(
            "test-request-id",
            json.getString("request_id")
        )

        assertEquals(
            "test-device",
            json.getString("device_id")
        )

        assertEquals(
            "TEST_PUBLIC_KEY",
            json.getString("public_key")
        )

        assertEquals(
            123456789L,
            json.getLong("timestamp")
        )
    }

    @Test
    fun serializePairingRequest_doesNotContainPrivateKey() {

        val request = PairingRequest(
            protocolVersion = "1.0",
            messageType = "PAIRING_REQUEST",
            requestId = "test-request-id",
            deviceId = "test-device",
            publicKey = "TEST_PUBLIC_KEY",
            timestamp = System.currentTimeMillis()
        )

        val jsonString =
            MessageSerializer.serializePairingRequest(request)

        assertTrue(
            !jsonString.contains("private_key")
        )

        assertTrue(
            !jsonString.contains("PRIVATE")
        )
    }

    @Test
    fun serializePairingRequest_createsDifferentJsonForDifferentRequests() {

        val firstRequest = PairingRequest(
            protocolVersion = "1.0",
            messageType = "PAIRING_REQUEST",
            requestId = "request-1",
            deviceId = "device-1",
            publicKey = "PUBLIC_KEY_1",
            timestamp = 1000L
        )

        val secondRequest = PairingRequest(
            protocolVersion = "1.0",
            messageType = "PAIRING_REQUEST",
            requestId = "request-2",
            deviceId = "device-2",
            publicKey = "PUBLIC_KEY_2",
            timestamp = 2000L
        )

        val firstJson =
            MessageSerializer.serializePairingRequest(firstRequest)

        val secondJson =
            MessageSerializer.serializePairingRequest(secondRequest)

        assertNotEquals(
            firstJson,
            secondJson
        )
    }
}