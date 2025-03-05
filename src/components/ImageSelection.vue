<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'  // Add this import

const router = useRouter()  // Add this
const props = defineProps({
  username: String,
  email: String,
  loginEmail: String, 
  isLogin: Boolean,  
  storedImage: String 
})

const emit = defineEmits(['close', 'pattern-confirmed'])
const selectedCells = ref([])
const randomImage = ref('')

const images = [
  '/images/img1.jpg',
  '/images/img2.jpg',
  '/images/img3.jpg',
  '/images/img4.jpg',
  '/images/img5.jpg'
]

onMounted(() => {
  if (props.isLogin && props.storedImage) {
    randomImage.value = props.storedImage
  } else {
    const randomIndex = Math.floor(Math.random() * images.length)
    randomImage.value = images[randomIndex]
  }
})

const MAX_SELECTIONS = 5

const handleCellClick = (index) => {
  const cellIndex = selectedCells.value.indexOf(index)
  if (cellIndex === -1) {
    if (selectedCells.value.length < MAX_SELECTIONS) {
      selectedCells.value.push(index)
    }
  } else {
    selectedCells.value.splice(cellIndex, 1)
  }
}

const handleSubmit = async () => {
  if (selectedCells.value.length < 3) {
    alert('Please select at least 3 cells')
    return
  }
  
  try {
    if (!props.isLogin) {
      // Registration Process
      const response = await fetch('http://localhost:5000/api/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: props.email,
          username: props.username,
          selected_image: randomImage.value,
          pattern: selectedCells.value
        })
      })

      if (response.ok) {
        emit('pattern-confirmed')  // Change this from router.push
      } else {
        const data = await response.json()
        alert(data.error || 'Registration failed')
      }
    } else {
      // Login Process (Pattern Verification)
      const response = await fetch('http://localhost:5000/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: props.loginEmail,
          pattern: selectedCells.value
        })
      })

      if (response.ok) {
        const data = await response.json()
        localStorage.setItem('currentUser', props.loginEmail)
        localStorage.setItem('username', data.username)
        emit('pattern-confirmed')  // This will trigger the parent's handler
        router.push('/main')  // Change this line to redirect to MainPage
      } else {
        const data = await response.json()
        alert(data.error || 'Login failed')
      }
    }
  } catch (error) {
    console.error('Error:', error)
    alert('An error occurred')
  }
}
</script>

<template>
  <div class="lightbox-overlay">
    <div class="lightbox-content">
      <h3>Select Grid Pattern</h3>
      <div class="image-container">
        <div class="grid-image" :style="{ backgroundImage: `url(${randomImage})` }"></div>
        <div class="image-grid">
          <div 
            v-for="i in 25" 
            :key="i"
            class="grid-cell"
            @click="handleCellClick(i-1)"
            :class="{ selected: selectedCells.includes(i-1) }"
          ></div>
        </div>
      </div>
      <div class="buttons">
        <button @click="handleSubmit" class="submit-btn">Confirm Pattern</button>
        <button @click="$emit('close')" class="cancel-btn">Cancel</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.lightbox-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.lightbox-content {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  max-width: 500px;
  width: 90%;
}

.image-container {
  position: relative;
  width: 100%;
  aspect-ratio: 1;
  margin: 20px 0;
}

.grid-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
}

.image-grid {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 2px;
  z-index: 2;
}

.grid-cell {
  aspect-ratio: 1;
  border: 1px solid rgba(255, 255, 255, 0.5);
  cursor: pointer;
  transition: background-color 0.2s;
}

.grid-cell.selected {
  background-color: rgba(66, 185, 131, 0.5);
  border: 2px solid #42b983;
}

.buttons {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
}

.submit-btn, .cancel-btn {
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
}

.submit-btn {
  background-color: #42b983;
  color: white;
  border: none;
}

.cancel-btn {
  background-color: #666;
  color: white;
  border: none;
}
</style>
