/**import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import './style.css'
import router from "./router"*/

const apiurl = "http://localhost:8000/"

const completarTarefa = async (ninja, task) => {
    response = await fetch(apiurl+"completar_task?ninja="+ninja+"?task="+task);
    return response;
}

const gApiCall = async (endpoint = "", args = {}) => {
    let url = apiurl+endpoint+"?";
    for (let key in args) { url += key+"="+args[key]+"&" }
    return await fetch(url);
} 

console.log(gApiCall("completar_task", {"task":"cham-cham","ninja":2}))
console.log(gApiCall("matar_ninja", {"ninja":4,"impostor":2}))

//createApp(App).use(router).mount('#app')
