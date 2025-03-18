<template>
  <div class="container" :class="{ 'loaded': isLoaded }">
    <button @click="handleLogout" class="logout-btn">
      <span class="logout-icon">🚪</span> Logout
    </button>
    
    <!-- <div > -->
      <div class="profile-header">
        <div class="profile-info">
          <div class="avatar">{{ username ? username[0].toUpperCase() : 'U' }}</div>
          <div class="user-details">
            <h1 class="headline">Welcome, {{username}}</h1>
            <p class="email">{{email}}</p>
          </div>
        </div>
      </div>
      <div class="stats-grid">
        <div class="stat-card">
          <span class="stat-icon">🔐</span>
          <h3>Last Login</h3>
          <p>{{lastLogin}}</p>
        </div>
        <div class="stat-card">
          <span class="stat-icon">✅</span>
          <h3>Authentication</h3>
          <p>Pattern Verified</p>
        </div>
        <div class="stat-card">
          <span class="stat-icon">🔒</span>
          <h3>Security</h3>
          <p>Account Protected</p>
        </div>
      </div>
    </div>
    
    <!-- <div class="right-section"> -->
      <!-- <img src="/images/lock.jpeg" alt="Featured Image" class="featured-image" /> -->
      <div class="overlay">
        <p class="tagline">Secured by</p>
        <h2 class="app-name">Graphical Authentication</h2>
      </div>
    <!-- </div> -->
  <!-- </div> -->
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const username = ref(localStorage.getItem('username'))
const email = ref(localStorage.getItem('currentUser'))
const lastLogin = ref(new Date().toLocaleString())
const isLoaded = ref(false)

const handleLogout = () => {
  localStorage.removeItem('currentUser')
  localStorage.removeItem('username')
  router.push('/')
}

onMounted(() => {
  setTimeout(() => {
    isLoaded.value = true
  }, 100)
})
</script>

<style scoped>
.container {
  display: flex;
  flex-wrap: wrap;
  min-height: 100vh;
  gap: 2rem;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.5s ease;
  padding: 1rem;
  background-color: #1a1f2c;
  color: #ffffff;
  font-family: 'Roboto', sans-serif;
}

.loaded {
  opacity: 1;
  transform: translateY(0);
}

.profile-header {
  flex: 1 1 300px;
  background: #242b3d;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  border: 1px solid #2d3548;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.profile-header:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
}

.profile-info {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.avatar {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #4a90e2, #2b68c9);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  color: white;
  font-weight: bold;
  box-shadow: 0 4px 10px rgba(43, 104, 201, 0.3);
}

.user-details {
  flex: 1;
}

.headline {
  color: #ffffff;
  font-size: 2.2rem;
  font-weight: 600;
  font-family: 'Segoe UI', system-ui, sans-serif;
  margin-bottom: 0.5rem;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.email {
  color: #a8b3cf;
  margin-top: 0.5rem;
  font-size: 1.1rem;
  letter-spacing: 0.5px;
}

.stats-grid {
  flex: 2 1 600px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  align-content: start;
}

.stat-card {
  background: #242b3d;
  padding: 1.8rem;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid #2d3548;
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
  background: #2a324a;
}

.stat-card h3 {
  color: #4a90e2;
  font-size: 1.4rem;
  font-weight: 600;
  margin: 1rem 0;
  font-family: 'Segoe UI', system-ui, sans-serif;
}

.stat-card p {
  color: #ffffff;
  font-size: 1.1rem;
  margin-top: 0.5rem;
}

.stat-icon {
  font-size: 2.2rem;
  margin-bottom: 1rem;
  display: block;
  background: linear-gradient(135deg, #4a90e2, #2b68c9);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.featured-image {
  width: 100%;
  max-width: 100%;
  border-radius: 15px;
  margin-top: 2rem;
  opacity: 0.8;
  transition: opacity 0.3s ease;
}

.featured-image:hover {
  opacity: 1;
}

.overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 2rem;
  background: linear-gradient(transparent, rgba(26, 31, 44, 0.95));
  color: white;
  border-radius: 0 0 15px 15px;
}

.tagline {
  font-size: 1.2rem;
  color: #4a90e2;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.app-name {
  font-size: 2.5rem;
  font-weight: bold;
  margin-top: 0.5rem;
  background: linear-gradient(135deg, #4a90e2, #2b68c9);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.logout-btn {
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 12px 24px;
  background: linear-gradient(135deg, #4a90e2, #2b68c9);
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  z-index: 1000;
  box-shadow: 0 4px 15px rgba(43, 104, 201, 0.3);
}

.logout-btn:hover {
  background: linear-gradient(135deg, #2b68c9, #1e4b94);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(43, 104, 201, 0.4);
}

@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }
  
  .right-section {
    display: none;
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
  }
}
</style>
