package com.example.fingerprintunlock

import org.junit.Assert.assertNotEquals
import org.junit.Assert.assertNotNull
import org.junit.Test

class AuthenticationRequestBuilderTest {

    @Test
    fun build_createsValidAuthenticationRequest() {
        val builder = AuthenticationRequestBuilder()

        val request = builder.build(
            deviceId = "test-device"
        )

        assertNotNull(request)
        assertNotEquals("", request.requestId)
        assertNotEquals("", request.challenge)
        assertNotEquals("", request.deviceId)
        assertNotEquals("", request.timestamp.toString())
    }

    @Test
    fun build_createsDifferentChallenges() {
        val builder = AuthenticationRequestBuilder()

        val firstRequest = builder.build(
            deviceId = "test-device"
        )

        val secondRequest = builder.build(
            deviceId = "test-device"
        )

        assertNotEquals(
            firstRequest.challenge,
            secondRequest.challenge
        )
    }
}