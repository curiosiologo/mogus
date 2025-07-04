import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import './style.css'
import router from "./router"

const apiurl = "http://localhost:8000/"

createApp(App).use(router).mount('#app')
