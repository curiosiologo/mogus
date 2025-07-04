import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import './style.css'
import router from "./router"

// Use old fetch but with custom ngrok bypass warning header
const oldFetch = window.fetch;
window.fetch = async (url) => {
    const response = await oldFetch(url, {headers: {'ngrok-skip-browser-warning': 'true'}});
    return response;
}

createApp(App).use(router).mount('#app')
