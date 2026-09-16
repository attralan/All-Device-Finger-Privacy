package com.example.fingerprintunlock

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Test

class PairingResponseParserTest {

    @Test
    fun parse_validResponse_returnsPairingResponse() {

        val json = """
            {
                "protocol_version": "1.0",
                "message_type": "PAIRING_RESPONSE",
                "request_id": "test-request-id",
                "status": "CONNECTED",
                "error_code": null,
                "timestamp": 123456789
            }
        """.trimIndent()

        val response =
            PairingResponseParser.parse(json)

        assertNotNull(response)

        assertEquals(
            "1.0",
            response?.protocolVersion
        )

        assertEquals(
            "PAIRING_RESPONSE",
            response?.messageType
        )

        assertEquals(
            "test-request-id",
            response?.requestId
        )

        assertEquals(
            "CONNECTED",
            response?.status
        )

        assertNull(
            response?.errorCode
        )

        assertEquals(
            123456789L,
            response?.timestamp
        )
    }

    @Test
    fun parse_responseWithErrorCode_readsErrorCode() {

        val json = """
            {
                "protocol_version": "1.0",
                "message_type": "PAIRING_RESPONSE",
                "request_id": "test-request-id",
                "status": "REJECTED",
                "error_code": "E001",
                "timestamp": 123456789
            }
        """.trimIndent()

        val response =
            PairingResponseParser.parse(json)

        assertNotNull(response)

        assertEquals(
            "REJECTED",
            response?.status
        )

        assertEquals(
            "E001",
            response?.errorCode
        )
    }

    @Test
    fun parse_invalidJson_returnsNull() {

        val invalidJson =
            "this is not valid json"

        val response =
            PairingResponseParser.parse(
                invalidJson
            )

        assertNull(response)
    }

    @Test
    fun parse_missingRequiredField_returnsNull() {

        val json = """
            {
                "protocol_version": "1.0",
                "message_type": "PAIRING_RESPONSE",
                "request_id": "test-request-id",
                "status": "CONNECTED"
            }
        """.trimIndent()

        val response =
            PairingResponseParser.parse(json)

        assertNull(response)
    }
}