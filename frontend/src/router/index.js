import { createRouter, createWebHistory } from "vue-router"
import NinjaView from "../NinjaView.vue"
import Home from "../Home.vue"
import Mentor from "../Mentor.vue"
import MarcarMorte from "../MarcarMorte.vue"
import ConvocarReuniao from "../ConvocarReunião.vue"
const routes=[
    {path:"/", component:Home},
    {path:"/ninja", component:NinjaView},
    {path:"/mentor", component:Mentor},
    {path:"/marcar_morte", component:MarcarMorte},
    {path:"/convocar_reuniao", component:ConvocarReuniao},
]
const router=createRouter({
    history: createWebHistory(),
    routes
})
export default router