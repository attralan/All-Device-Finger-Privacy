package com.example.fingerprintunlock

interface CommunicationTransport {

    fun connect(
        host: String,
        port: Int
    ): Boolean

    fun send(
        message: String
    ): Boolean

    fun receive(): String?

    fun disconnect()

    fun isConnected(): Boolean
}