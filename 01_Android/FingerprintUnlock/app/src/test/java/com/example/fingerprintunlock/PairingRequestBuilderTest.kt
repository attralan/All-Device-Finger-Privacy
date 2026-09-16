package com.example.fingerprintunlock

import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotEquals
import org.junit.Assert.assertTrue
import org.junit.Test

class PairingRequestBuilderTest {

    @Test
    fun build_createsValidPairingRequest() {
        val fakeKeyStoreManager = FakeKeyStoreManager()
        val builder = PairingRequestBuilder(fakeKeyStoreManager)

        val request = builder.build(
            deviceId = "test-device"
        )

        assertEquals("1.0", request.protocolVersion)
        assertEquals("PAIRING_REQUEST", request.messageType)
        assertNotEquals("", request.requestId)
        assertEquals("test-device", request.deviceId)
        assertNotEquals("", request.publicKey)
        assertTrue(request.timestamp > 0)
    }

    @Test
    fun build_doesNotExposePrivateKey() {
        val fakeKeyStoreManager = FakeKeyStoreManager()
        val builder = PairingRequestBuilder(fakeKeyStoreManager)

        val request = builder.build(
            deviceId = "test-device"
        )

        assertTrue(
            !request.publicKey.contains("PRIVATE")
        )
    }

    private class FakeKeyStoreManager : AndroidKeyStoreManager() {

        override fun getPublicKeyBase64(): String {
            return "TEST_PUBLIC_KEY"
        }
    }
}