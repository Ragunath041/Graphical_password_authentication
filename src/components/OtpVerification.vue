<template>
  <div class="otp-container">
    <div class="otp-card">
      <div class="otp-header">
        <h2>OTP Verification</h2>
        <p>Enter the 6-digit code to verify your account</p>
      </div>
      
      <div class="otp-input-container">
        <input 
          v-for="(digit, index) in 6" 
          :key="index"
          type="text"
          maxlength="1"
          v-model="otpDigits[index]"
          @input="handleInput($event, index)"
          @keydown="handleKeydown($event, index)"
          :ref="'digit' + index"
          class="otp-digit"
        >
      </div>

      <div class="error-message" v-if="errorMessage">
        {{ errorMessage }}
      </div>

      <button @click="verifyOTP" class="verify-button" :disabled="!isComplete">
        Verify & Continue
      </button>

      <div class="resend-section">
        <p>Didn't receive the code?</p>
        <button @click="resendOTP" class="resend-button" :disabled="countdown > 0">
          {{ countdown > 0 ? `Resend in ${countdown}s` : 'Resend OTP' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const otpDigits = ref(Array(6).fill(''))
const errorMessage = ref('')
const countdown = ref(30)

const isComplete = computed(() => {
  return otpDigits.value.every(digit => digit !== '')
})

const handleInput = (event, index) => {
  const value = event.target.value
  // Only allow numbers
  if (!/^\d*$/.test(value)) {
    otpDigits.value[index] = ''
    return
  }
  
  // Move to next input if available
  if (value && index < 5) {
    const nextInput = document.querySelector(`input[ref="digit${index + 1}"]`)
    if (nextInput) nextInput.focus()
  }
}

const handleKeydown = (event, index) => {
  // Handle backspace
  if (event.key === 'Backspace' && !otpDigits.value[index] && index > 0) {
    const prevInput = document.querySelector(`input[ref="digit${index - 1}"]`)
    if (prevInput) {
      prevInput.focus()
      otpDigits.value[index - 1] = ''
    }
  }
}

const startCountdown = () => {
  countdown.value = 30
  const timer = setInterval(() => {
    if (countdown.value > 0) {
      countdown.value--
    } else {
      clearInterval(timer)
    }
  }, 1000)
}

const resendOTP = () => {
  // Reset OTP digits
  otpDigits.value = Array(6).fill('')
  errorMessage.value = ''
  startCountdown()
}

const verifyOTP = () => {
  const enteredOTP = otpDigits.value.join('')
  // For demo purposes, any 6-digit number is accepted
  if (enteredOTP.length === 6) {
    router.push('/main')
  } else {
    errorMessage.value = 'Please enter a valid 6-digit OTP'
  }
}

onMounted(() => {
  startCountdown()
})
</script>

<style scoped>
.otp-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f5f5f5;
  padding: 20px;
}

.otp-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

.otp-header {
  text-align: center;
  margin-bottom: 2rem;
}

.otp-header h2 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
  font-size: 1.8rem;
}

.otp-header p {
  color: #666;
  font-size: 0.9rem;
}

.otp-input-container {
  display: flex;
  gap: 8px;
  justify-content: center;
  margin-bottom: 1.5rem;
}

.otp-digit {
  width: 45px;
  height: 45px;
  border: 2px solid #ddd;
  border-radius: 8px;
  text-align: center;
  font-size: 1.2rem;
  font-weight: bold;
  color: #2c3e50;
  transition: all 0.3s ease;
}

.otp-digit:focus {
  border-color: #42b983;
  outline: none;
  box-shadow: 0 0 0 2px rgba(66, 185, 131, 0.2);
}

.verify-button {
  width: 100%;
  padding: 12px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.verify-button:disabled {
  background-color: #a8d5c2;
  cursor: not-allowed;
}

.verify-button:hover:not(:disabled) {
  background-color: #3aa876;
}

.error-message {
  color: #dc3545;
  text-align: center;
  margin-bottom: 1rem;
  font-size: 0.9rem;
}

.resend-section {
  margin-top: 1.5rem;
  text-align: center;
}

.resend-section p {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}

.resend-button {
  background: none;
  border: none;
  color: #42b983;
  cursor: pointer;
  font-size: 0.9rem;
  padding: 0;
}

.resend-button:disabled {
  color: #666;
  cursor: not-allowed;
}

@media (max-width: 480px) {
  .otp-digit {
    width: 40px;
    height: 40px;
    font-size: 1rem;
  }
  
  .otp-card {
    padding: 1.5rem;
  }
}
</style> 