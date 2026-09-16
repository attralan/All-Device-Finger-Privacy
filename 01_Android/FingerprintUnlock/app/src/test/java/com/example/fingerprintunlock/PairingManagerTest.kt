package com.example.fingerprintunlock

import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class PairingManagerTest {

    @Test
    fun createPairingMessage_createsValidJson() {

        val fakeTransport = FakeTransport()
        val fakeKeyStoreManager = FakeKeyStoreManager()

        val pairingManager = PairingManager(
            transport = fakeTransport,
            keyStoreManager = fakeKeyStoreManager
        )

        val message =
            pairingManager.createPairingMessage(
                deviceId = "test-device"
            )

        assertTrue(message.isNotEmpty())
        assertTrue(
            message.contains("PAIRING_REQUEST")
        )
        assertTrue(
            message.contains("test-device")
        )
        assertTrue(
            message.contains("TEST_PUBLIC_KEY")
        )
    }

    @Test
    fun sendPairingRequest_connectsAndSendsMessage() {

        val fakeTransport = FakeTransport()
        val fakeKeyStoreManager = FakeKeyStoreManager()

        val pairingManager = PairingManager(
            transport = fakeTransport,
            keyStoreManager = fakeKeyStoreManager
        )

        val result =
            pairingManager.sendPairingRequest(
                host = "127.0.0.1",
                port = 8080,
                deviceId = "test-device"
            )

        assertTrue(result)
        assertTrue(fakeTransport.connectCalled)
        assertTrue(fakeTransport.sendCalled)
        assertTrue(
            fakeTransport.lastMessage
                ?.contains("PAIRING_REQUEST") == true
        )
    }

    @Test
    fun sendPairingRequest_returnsFalseWhenConnectionFails() {

        val fakeTransport = FakeTransport()
        fakeTransport.shouldConnect = false

        val fakeKeyStoreManager = FakeKeyStoreManager()

        val pairingManager = PairingManager(
            transport = fakeTransport,
            keyStoreManager = fakeKeyStoreManager
        )

        val result =
            pairingManager.sendPairingRequest(
                host = "127.0.0.1",
                port = 8080,
                deviceId = "test-device"
            )

        assertFalse(result)
        assertTrue(fakeTransport.connectCalled)
        assertFalse(fakeTransport.sendCalled)
    }

    private class FakeTransport : CommunicationTransport {

        var shouldConnect = true
        var connectCalled = false
        var sendCalled = false
        var lastMessage: String? = null

        private var connected = false

        override fun connect(
            host: String,
            port: Int
        ): Boolean {

            connectCalled = true

            if (!shouldConnect) {
                return false
            }

            connected = true
            return true
        }

        override fun send(
            message: String
        ): Boolean {

            if (!connected) {
                return false
            }

            sendCalled = true
            lastMessage = message

            return true
        }

        override fun receive(): String? {
            return null
        }

        override fun disconnect() {
            connected = false
        }

        override fun isConnected(): Boolean {
            return connected
        }
    }

    private class FakeKeyStoreManager :
        AndroidKeyStoreManager() {

        override fun getPublicKeyBase64(): String {
            return "TEST_PUBLIC_KEY"
        }
    }
}