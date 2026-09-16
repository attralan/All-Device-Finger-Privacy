package com.example.fingerprintunlock

import android.util.Base64
import android.security.keystore.KeyGenParameterSpec
import android.security.keystore.KeyProperties
import java.security.KeyPair
import java.security.KeyPairGenerator
import java.security.KeyStore

open class AndroidKeyStoreManager {

    companion object {
        private const val KEYSTORE_PROVIDER = "AndroidKeyStore"
        private const val KEY_ALIAS = "fingerprint_unlock_auth_key"
    }

    fun getOrCreateKeyPair(): KeyPair {
        val keyStore = KeyStore.getInstance(KEYSTORE_PROVIDER)
        keyStore.load(null)

        if (keyStore.containsAlias(KEY_ALIAS)) {
            val privateKey = keyStore.getKey(
                KEY_ALIAS,
                null
            ) as java.security.PrivateKey

            val publicKey = keyStore
                .getCertificate(KEY_ALIAS)
                .publicKey

            return KeyPair(
                publicKey,
                privateKey
            )
        }

        val keyPairGenerator = KeyPairGenerator.getInstance(
            KeyProperties.KEY_ALGORITHM_EC,
            KEYSTORE_PROVIDER
        )

        val keyGenParameterSpec = KeyGenParameterSpec.Builder(
            KEY_ALIAS,
            KeyProperties.PURPOSE_SIGN or
                    KeyProperties.PURPOSE_VERIFY
        )
            .setDigests(KeyProperties.DIGEST_SHA256)
            .setUserAuthenticationRequired(true)
            .setInvalidatedByBiometricEnrollment(true)
            .build()

        keyPairGenerator.initialize(keyGenParameterSpec)

        return keyPairGenerator.generateKeyPair()
    }

    fun getPublicKey(): java.security.PublicKey {
        val keyStore = KeyStore.getInstance(KEYSTORE_PROVIDER)
        keyStore.load(null)

        if (!keyStore.containsAlias(KEY_ALIAS)) {
            return getOrCreateKeyPair().public
        }

        return keyStore
            .getCertificate(KEY_ALIAS)
            .publicKey
    }

    open fun getPublicKeyBase64(): String {
        val publicKey = getPublicKey()

        return Base64.encodeToString(
            publicKey.encoded,
            Base64.NO_WRAP
        )
    }
}