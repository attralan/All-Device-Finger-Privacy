package com.example.fingerprintunlock

import android.os.Bundle
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.fragment.app.FragmentActivity
import com.example.fingerprintunlock.ui.theme.FingerprintUnlockTheme

class MainActivity : FragmentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        val biometricAuthenticator =
            BiometricAuthenticator(this)

        val requestBuilder =
            AuthenticationRequestBuilder()

        val pairingManager = PairingManager(
            transport = WiFiTransport(),
            keyStoreManager = AndroidKeyStoreManager()
        )

        setContent {
            FingerprintUnlockTheme {
                FingerprintUnlockScreen(
                    onAuthenticate = { onSuccess, onFailure ->

                        val request = requestBuilder.build(
                            deviceId = "android-device"
                        )

                        biometricAuthenticator.authenticate(
                            challenge = request.challenge,
                            onSuccess = { authenticationProof ->

                                val authenticatedRequest =
                                    request.copy(
                                        authenticationProof =
                                            authenticationProof
                                    )

                                onSuccess(authenticatedRequest)
                            },
                            onFailure = onFailure
                        )
                    },
                    onPair = { host, port, onResult ->

                        val result =
                            pairingManager.sendPairingRequest(
                                host = host,
                                port = port,
                                deviceId = "android-device"
                            )

                        onResult(result)
                    }
                )
            }
        }
    }
}

@Composable
fun FingerprintUnlockScreen(
    onAuthenticate: (
        onSuccess: (AuthenticationRequest) -> Unit,
        onFailure: () -> Unit
    ) -> Unit,
    onPair: (
        host: String,
        port: Int,
        onResult: (Boolean) -> Unit
    ) -> Unit
) {

    var message by remember {
        mutableStateOf("Ready to authenticate")
    }

    var isAuthenticated by remember {
        mutableStateOf(false)
    }

    var laptopIp by remember {
        mutableStateOf("")
    }

    var laptopPort by remember {
        mutableStateOf("8080")
    }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {

        Text(text = message)

        Spacer(
            modifier = Modifier.height(16.dp)
        )

        Button(
            onClick = {

                message =
                    "Waiting for fingerprint..."

                isAuthenticated = false

                onAuthenticate(
                    { authenticatedRequest ->

                        message =
                            "Fingerprint verified successfully!"

                        isAuthenticated = true

                        println(
                            "Authentication request: " +
                                    authenticatedRequest
                        )
                    },
                    {
                        message =
                            "Fingerprint authentication failed"

                        isAuthenticated = false
                    }
                )
            },
            enabled = !isAuthenticated
        ) {
            Text(
                text = if (isAuthenticated) {
                    "Authenticated ✓"
                } else {
                    "Unlock with Fingerprint"
                }
            )
        }

        Spacer(
            modifier = Modifier.height(32.dp)
        )

        Text(
            text = "Laptop Pairing"
        )

        Spacer(
            modifier = Modifier.height(12.dp)
        )

        OutlinedTextField(
            value = laptopIp,
            onValueChange = {
                laptopIp = it
            },
            label = {
                Text("Laptop IP Address")
            },
            singleLine = true
        )

        Spacer(
            modifier = Modifier.height(8.dp)
        )

        OutlinedTextField(
            value = laptopPort,
            onValueChange = {
                laptopPort = it
            },
            label = {
                Text("Laptop Port")
            },
            singleLine = true
        )

        Spacer(
            modifier = Modifier.height(12.dp)
        )

        Button(
            onClick = {

                val port = laptopPort.toIntOrNull()

                if (laptopIp.isBlank()) {

                    message =
                        "Enter laptop IP address"

                    return@Button
                }

                if (port == null ||
                    port !in 1..65535
                ) {

                    message =
                        "Enter a valid port"

                    return@Button
                }

                message =
                    "Connecting to laptop..."

                onPair(
                    laptopIp,
                    port
                ) { success ->

                    message =
                        if (success) {
                            "Pairing request sent"
                        } else {
                            "Could not connect to laptop"
                        }
                }
            }
        ) {
            Text(
                text = "Pair with Laptop"
            )
        }
    }
}