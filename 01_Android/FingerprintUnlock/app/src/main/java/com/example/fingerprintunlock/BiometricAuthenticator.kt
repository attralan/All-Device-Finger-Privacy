package com.example.fingerprintunlock

import androidx.biometric.BiometricManager
import androidx.biometric.BiometricPrompt
import androidx.core.content.ContextCompat
import androidx.fragment.app.FragmentActivity
import java.nio.charset.StandardCharsets
import java.security.KeyStore
import java.security.Signature
import java.util.concurrent.Executor

class BiometricAuthenticator(
    private val activity: FragmentActivity
) {

    private val executor: Executor =
        ContextCompat.getMainExecutor(activity)

    private val keyStoreManager = AndroidKeyStoreManager()

    fun isBiometricAvailable(): Boolean {
        val biometricManager = BiometricManager.from(activity)

        return biometricManager.canAuthenticate(
            BiometricManager.Authenticators.BIOMETRIC_STRONG
        ) == BiometricManager.BIOMETRIC_SUCCESS
    }

    fun authenticate(
        challenge: String,
        onSuccess: (authenticationProof: String) -> Unit,
        onFailure: () -> Unit
    ) {
        try {
            val keyPair = keyStoreManager.getOrCreateKeyPair()

            val signature = Signature.getInstance("SHA256withECDSA")

            signature.initSign(keyPair.private)

            val cryptoObject = BiometricPrompt.CryptoObject(signature)

            val biometricPrompt = BiometricPrompt(
                activity,
                executor,
                object : BiometricPrompt.AuthenticationCallback() {

                    override fun onAuthenticationSucceeded(
                        result: BiometricPrompt.AuthenticationResult
                    ) {
                        super.onAuthenticationSucceeded(result)

                        try {
                            val authenticatedSignature =
                                result.cryptoObject?.signature
                                    ?: throw IllegalStateException(
                                        "Cryptographic signature unavailable"
                                    )

                            authenticatedSignature.update(
                                challenge.toByteArray(StandardCharsets.UTF_8)
                            )

                            val signedChallenge =
                                authenticatedSignature.sign()

                            val authenticationProof =
                                android.util.Base64.encodeToString(
                                    signedChallenge,
                                    android.util.Base64.NO_WRAP
                                )

                            onSuccess(authenticationProof)

                        } catch (_: Exception) {
                            onFailure()
                        }
                    }

                    override fun onAuthenticationFailed() {
                        super.onAuthenticationFailed()
                        onFailure()
                    }

                    override fun onAuthenticationError(
                        errorCode: Int,
                        errString: CharSequence
                    ) {
                        super.onAuthenticationError(
                            errorCode,
                            errString
                        )
                        onFailure()
                    }
                }
            )

            val promptInfo = BiometricPrompt.PromptInfo.Builder()
                .setTitle("Fingerprint Authentication")
                .setSubtitle(
                    "Verify your fingerprint to authenticate the laptop"
                )
                .setNegativeButtonText("Cancel")
                .build()

            biometricPrompt.authenticate(
                promptInfo,
                cryptoObject
            )

        } catch (_: Exception) {
            onFailure()
        }
    }
}