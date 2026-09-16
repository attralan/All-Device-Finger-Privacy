package com.example.fingerprintunlock

import android.os.Bundle
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.material3.Button
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

        val biometricAuthenticator = BiometricAuthenticator(this)
        val requestBuilder = AuthenticationRequestBuilder()

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
    ) -> Unit
) {
    var message by remember {
        mutableStateOf("Ready to authenticate")
    }

    var isAuthenticated by remember {
        mutableStateOf(false)
    }

    Column(
        modifier = Modifier.fillMaxSize(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {

        Text(text = message)

        Spacer(
            modifier = Modifier.height(16.dp)
        )

        Button(
            onClick = {
                message = "Waiting for fingerprint..."
                isAuthenticated = false

                onAuthenticate(
                    { authenticatedRequest ->
                        message =
                            "Fingerprint verified successfully!"

                        isAuthenticated = true

                        // The authenticated request is now ready
                        // for the future laptop communication layer.
                        println(
                            "Authentication request: " +
                                    authenticatedRequest
                        )
                    },
                    {
                        message = "Fingerprint authentication failed"
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
    }
}