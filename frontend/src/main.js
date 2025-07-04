import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import './style.css'
import router from "./router"

// Use old fetch but with custom ngrok bypass warning header

createApp(App).use(router).mount('#app')
