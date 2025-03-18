<template>
  <div class="otp-container">
    <div class="otp-box">
      <h2>Enter OTP</h2>
      <p class="timer">Time remaining: {{ formatTime(timeLeft) }}</p>
      <div class="otp-input-container">
        <input
          v-for="(digit, index) in 6"
          :key="index"
          type="text"
          maxlength="1"
          v-model="otpDigits[index]"
          @input="handleInput($event, index)"
          @keydown="handleKeydown($event, index)"
          ref="otpInputs"
          :disabled="timeLeft === 0"
        >
      </div>
      <p class="error-message" v-if="errorMessage">{{ errorMessage }}</p>
      <button @click="verifyOTP" :disabled="!isOtpComplete || timeLeft === 0" class="verify-btn">
        Verify OTP
      </button>
      <button @click="resendOTP" :disabled="timeLeft > 0" class="resend-btn">
        Resend OTP
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const otpDigits = ref(['', '', '', '', '', ''])
const timeLeft = ref(60)
const errorMessage = ref('')
const timer = ref(null)
const otpInputs = ref([])

const isOtpComplete = computed(() => {
  return otpDigits.value.every(digit => digit !== '')
})

const formatTime = (seconds) => {
  const mins = Math.floor(seconds / 60)
  const secs = seconds % 60
  return `${mins}:${secs.toString().padStart(2, '0')}`
}

const startTimer = () => {
  timeLeft.value = 60
  if (timer.value) clearInterval(timer.value)
  
  timer.value = setInterval(() => {
    if (timeLeft.value > 0) {
      timeLeft.value--
    } else {
      clearInterval(timer.value)
      errorMessage.value = 'OTP has expired. Please request a new one.'
    }
  }, 1000)
}

const handleInput = (event, index) => {
  const input = event.target
  const value = input.value

  // Ensure only numbers are entered
  if (!/^\d*$/.test(value)) {
    otpDigits.value[index] = ''
    return
  }

  // Move to next input if available
  if (value && index < 5) {
    otpInputs.value[index + 1].focus()
  }
}

const handleKeydown = (event, index) => {
  // Handle backspace
  if (event.key === 'Backspace' && !otpDigits.value[index] && index > 0) {
    otpInputs.value[index - 1].focus()
  }
}

const verifyOTP = async () => {
  const otp = otpDigits.value.join('')
  
  try {
    // Here you would typically make an API call to verify the OTP
    // For demo purposes, we'll use a mock verification
    if (otp === '123456') { // Replace with actual OTP verification
      router.push('/main')
    } else {
      errorMessage.value = 'Invalid OTP. Please try again.'
    }
  } catch (error) {
    errorMessage.value = 'Error verifying OTP. Please try again.'
  }
}

const resendOTP = () => {
  // Reset OTP inputs
  otpDigits.value = ['', '', '', '', '', '']
  errorMessage.value = ''
  startTimer()
  // Here you would typically make an API call to resend the OTP
}

onMounted(() => {
  startTimer()
})

onUnmounted(() => {
  if (timer.value) clearInterval(timer.value)
})
</script>

<style scoped>
.otp-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f5f5f5;
}

.otp-box {
  background: white;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 100%;
  max-width: 400px;
}

h2 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.timer {
  color: #666;
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
}

.otp-input-container {
  display: flex;
  gap: 0.5rem;
  justify-content: center;
  margin-bottom: 1.5rem;
}

input {
  width: 40px;
  height: 40px;
  text-align: center;
  font-size: 1.2rem;
  border: 2px solid #ddd;
  border-radius: 8px;
  outline: none;
  transition: border-color 0.3s;
}

input:focus {
  border-color: #42b983;
}

input:disabled {
  background-color: #f5f5f5;
  cursor: not-allowed;
}

.error-message {
  color: #dc3545;
  margin-bottom: 1rem;
  font-size: 0.9rem;
}

.verify-btn, .resend-btn {
  width: 100%;
  padding: 0.75rem;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.verify-btn {
  background-color: #42b983;
  color: white;
  margin-bottom: 0.5rem;
}

.verify-btn:hover:not(:disabled) {
  background-color: #3aa876;
}

.resend-btn {
  background-color: #e9ecef;
  color: #2c3e50;
}

.resend-btn:hover:not(:disabled) {
  background-color: #dee2e6;
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style> 