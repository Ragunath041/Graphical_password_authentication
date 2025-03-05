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
      <img src="/images/lock.jpeg" alt="Featured Image" class="featured-image" />
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
  height: 100vh;
  overflow: hidden;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.5s ease;
}

.loaded {
  opacity: 1;
  transform: translateY(0);
}

.left-section {
  flex: 1;
  background: #f8f9fa;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.profile-header {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.profile-info {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.avatar {
  width: 80px;
  height: 80px;
  background: #42b983;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  color: white;
  font-weight: bold;
}

.user-details {
  flex: 1;
}

.email {
  color: #666;
  margin-top: 0.5rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.stat-card {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-5px);
}

.stat-icon {
  font-size: 2rem;
  margin-bottom: 1rem;
  display: block;
}

.right-section {
  flex: 2;
  position: relative;
}

.featured-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 2rem;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.8));
  color: white;
}

.app-name {
  font-size: 2.5rem;
  font-weight: bold;
  margin-top: 0.5rem;
}

.logout-btn {
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 12px 24px;
  background-color: #ff4757;
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
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.logout-btn:hover {
  background-color: #ff6b81;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
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