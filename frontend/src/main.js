import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import './style.css'
import router from "./router"

const completarTarefa = async (ninja, task) => {
    response = await fetch("http://localhost:8000/completar_task?ninja="+ninja+"?task="+task);
    return response;
  }

createApp(App).use(router).mount('#app')
