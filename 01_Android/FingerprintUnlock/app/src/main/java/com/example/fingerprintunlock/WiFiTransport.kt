package com.example.fingerprintunlock

import java.io.BufferedReader
import java.io.InputStreamReader
import java.io.PrintWriter
import java.net.InetSocketAddress
import java.net.Socket
import java.util.concurrent.Executors
import java.util.concurrent.Future

class WiFiTransport : CommunicationTransport {

    companion object {
        private const val CONNECT_TIMEOUT_MS = 5000
        private const val READ_TIMEOUT_MS = 10000
    }

    private var socket: Socket? = null
    private var writer: PrintWriter? = null
    private var reader: BufferedReader? = null

    private val executor =
        Executors.newSingleThreadExecutor()

    @Volatile
    private var connected = false

    override fun connect(
        host: String,
        port: Int
    ): Boolean {

        if (connected) {
            return true
        }

        return try {
            val newSocket = Socket()

            newSocket.connect(
                InetSocketAddress(host, port),
                CONNECT_TIMEOUT_MS
            )

            newSocket.soTimeout =
                READ_TIMEOUT_MS

            socket = newSocket

            writer = PrintWriter(
                newSocket.getOutputStream(),
                true
            )

            reader = BufferedReader(
                InputStreamReader(
                    newSocket.getInputStream()
                )
            )

            connected = true

            true

        } catch (_: Exception) {

            disconnect()

            false
        }
    }

    override fun send(
        message: String
    ): Boolean {

        if (!connected || writer == null) {
            return false
        }

        return try {

            val task: Future<*> =
                executor.submit {

                    writer?.println(message)
                }

            task.get()

            !task.isCancelled

        } catch (_: Exception) {

            false
        }
    }

    override fun receive(): String? {

        if (!connected || reader == null) {
            return null
        }

        return try {

            reader?.readLine()

        } catch (_: Exception) {

            null
        }
    }

    override fun disconnect() {

        connected = false

        try {
            reader?.close()
        } catch (_: Exception) {
        }

        try {
            writer?.close()
        } catch (_: Exception) {
        }

        try {
            socket?.close()
        } catch (_: Exception) {
        }

        reader = null
        writer = null
        socket = null
    }

    override fun isConnected(): Boolean {
        return connected
    }
}