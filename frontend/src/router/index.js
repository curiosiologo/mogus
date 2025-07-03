import { createRouter, createWebHistory } from "vue-router"
import NinjaView from "../NinjaView.vue"
import Home from "../Home.vue"
import Mentor from "../Mentor.vue"
const routes=[
    {path:"/", component:Home},
    {path:"/ninja", component:NinjaView},
    {path:"/mentor", component:Mentor},
]
const router=createRouter({
    history: createWebHistory(),
    routes
})
export default router