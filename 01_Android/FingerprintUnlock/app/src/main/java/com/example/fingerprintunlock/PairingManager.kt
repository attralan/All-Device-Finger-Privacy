package com.example.fingerprintunlock

class PairingManager(
    private val transport: CommunicationTransport,
    private val keyStoreManager: AndroidKeyStoreManager
) {

    private val requestBuilder =
        PairingRequestBuilder(keyStoreManager)

    fun createPairingMessage(
        deviceId: String
    ): String {

        val pairingRequest =
            requestBuilder.build(deviceId)

        return MessageSerializer.serializePairingRequest(
            pairingRequest
        )
    }

    fun sendPairingRequest(
        host: String,
        port: Int,
        deviceId: String
    ): Boolean {

        if (!transport.isConnected()) {

            val connected =
                transport.connect(
                    host,
                    port
                )

            if (!connected) {
                return false
            }
        }

        val message =
            createPairingMessage(deviceId)

        return transport.send(message)
    }

    fun receivePairingResponse(): PairingResponse? {

        val responseMessage =
            transport.receive()
                ?: return null

        return PairingResponseParser.parse(
            responseMessage
        )
    }

    fun disconnect() {
        transport.disconnect()
    }

    fun isConnected(): Boolean {
        return transport.isConnected()
    }
}