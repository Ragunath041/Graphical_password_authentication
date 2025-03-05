<script setup>
import { ref } from 'vue'
import ImageSelection from './ImageSelection.vue'
import MainPage from './MainPage.vue'

const username = ref('')
const email = ref('')
const loginEmail = ref('')
const showImageSelection = ref(false)
const showLogin = ref(false)
const showDashboard = ref(false)
const randomImage = ref('')
const storedImage = ref('')

const handleSubmit = () => {
  if (username.value && email.value) {
    showImageSelection.value = true
  }
}

const handlePatternConfirmed = () => {
  showImageSelection.value = false
  showLogin.value = true
}

const handleLoginSubmit = async () => {
  if (loginEmail.value) {
    try {
      const response = await fetch('http://localhost:5000/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: loginEmail.value
        })
      })

      if (response.ok) {
        const data = await response.json()
        storedImage.value = data.selected_image
        showImageSelection.value = true
      } else {
        alert('User not found')
      }
    } catch (error) {
      console.error('Error:', error)
      alert('An error occurred')
    }
  }
}

const handleLoginPatternConfirmed = () => {
  console.log('Login pattern confirmed') // Add this to debug
  showImageSelection.value = false
  showLogin.value = false
  showDashboard.value = true
}
</script>

<template>
  <div class="register-container">
    <!-- Registration Form -->
    <div class="register-form" v-if="!showLogin && !showDashboard">
      <h2>Register</h2>
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" placeholder="Enter username">
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" placeholder="Enter email">
      </div>
      <button class="submit-btn" @click="handleSubmit">Submit</button>
      <div class="form-footer">
        <p>Already have an account? <a href="#" @click.prevent="showLogin = true">Login here</a></p>
      </div>
    </div>

    <!-- Login Form -->
    <div class="register-form" v-if="showLogin && !showDashboard">
      <h2>Login</h2>
      <div class="form-group">
        <label for="login-email">Email:</label>
        <input 
          type="email" 
          id="login-email" 
          v-model="loginEmail" 
          placeholder="Enter email"
        >
      </div>
      <button class="submit-btn" @click="handleLoginSubmit">Submit</button>
      <div class="form-footer">
        <p>Don't have an account? <a href="#" @click.prevent="showLogin = false">Register here</a></p>
      </div>
    </div>

    <!-- Dashboard -->
    <MainPage v-if="showDashboard" />
    
    <!-- Image Selection Lightbox -->
    <ImageSelection 
      v-if="showImageSelection" 
      @close="showImageSelection = false"
      @pattern-confirmed="showLogin ? handleLoginPatternConfirmed : handlePatternConfirmed"
      :username="username"
      :email="email"
      :loginEmail="loginEmail"
      :isLogin="showLogin"
      :storedImage="storedImage"
    />
  </div>
</template>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 20px;
}

.register-form {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  border: 2px solid #e0e0e0;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 1.5rem;
  color: #2c3e50;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.submit-btn {
  width: 100%;
  padding: 0.75rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  margin-top: 1rem;
}

.submit-btn:hover {
  background-color: #3aa876;
}

.form-footer {
  margin-top: 1.5rem;
  text-align: center;
  font-size: 0.9rem;
}

.form-footer a {
  color: #42b983;
  text-decoration: none;
}

.form-footer a:hover {
  text-decoration: underline;
}
</style>
