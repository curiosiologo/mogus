import { createRouter, createWebHistory } from "vue-router"
import NinjaView from "../NinjaView.vue"
import Home from "../Home.vue"
import Login from "../Login.vue"
import Mentor from "../Mentor.vue"
import MarcarMorte from "../MarcarMorte.vue"
import ConvocarReuniao from "../ConvocarReunião.vue"
import Meltdown from "../Meltdown.vue"
const routes=[
    {path:"/", component:Home},
    {path:"/login", component:Login},
    {path:"/ninja", component:NinjaView},
    {path:"/mentor", component:Mentor},
    {path:"/marcar_morte", component:MarcarMorte},
    {path:"/convocar_reuniao", component:ConvocarReuniao},
    {path:"/meltdown", component:Meltdown},
]
const router=createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to) => {
    if (to.path == "/ninja") {
        return true
    }
    if (!localStorage["logged_in"] && to.path != "/login") {
        return "/login";
    }
    return true;
})

export default router