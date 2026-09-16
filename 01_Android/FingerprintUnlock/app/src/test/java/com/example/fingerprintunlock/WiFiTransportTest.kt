package com.example.fingerprintunlock

import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class WiFiTransportTest {

    @Test
    fun transport_isInitiallyDisconnected() {

        val transport = WiFiTransport()

        assertFalse(
            transport.isConnected()
        )
    }

    @Test
    fun sendWithoutConnection_returnsFalse() {

        val transport = WiFiTransport()

        val result =
            transport.send("TEST_MESSAGE")

        assertFalse(result)
    }

    @Test
    fun receiveWithoutConnection_returnsNull() {

        val transport = WiFiTransport()

        val result =
            transport.receive()

        assertTrue(
            result == null
        )
    }

    @Test
    fun connectToUnavailableServer_returnsFalse() {

        val transport = WiFiTransport()

        val result =
            transport.connect(
                host = "127.0.0.1",
                port = 65534
            )

        assertFalse(result)

        assertFalse(
            transport.isConnected()
        )

        transport.disconnect()
    }

    @Test
    fun disconnect_whenNotConnected_isSafe() {

        val transport = WiFiTransport()

        transport.disconnect()

        assertFalse(
            transport.isConnected()
        )
    }
}