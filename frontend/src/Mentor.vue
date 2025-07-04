<script setup lang="js">
  import { ref,onMounted } from "vue";
  import usePolling from './composables/usePolling';
  import StarBackground from './components/StarBackground.vue';
  const ninjas=ref([]);
  const emeeting=ref([]);
  const tasks=ref([]);
  const selectedtask=ref(null);
  const selected_ninja=ref(null);
  const global_progress=ref(0);
  const marcartarefa = async (ninja, tarefa) => {
    const response = await fetch(`http://localhost:8000/completar_task?ninja=${ninja}&task=${tarefa[0]}`);
    console.log(ninja, tarefa)
  };
  const taskclick=(index)=>{
    if (selectedtask.value == index){
        selectedtask.value=null
    } else{
        selectedtask.value=index;
    }
  };
  const apiCall = async () => {
    const response = await fetch("http://localhost:8000/tasks")
    const data=await response.json ();
    emeeting.value=data.emeeting;
    tasks.value=data.tasks;
    global_progress.value=data.task_progress;
  };
  const fetchNinjas= async () => {
    const response = await fetch("http://localhost:8000/info")
    const data=await response.json ();
    ninjas.value=data.ninjas.filter((n)=>n[3]==null);
  }
  onMounted(apiCall);
  const { start, clear } = usePolling(fetchNinjas, 1000);
  onMounted(start);
  
</script>

<template>
<StarBackground />

<main class="relative z-10 bg--200 flex flex-row p-4 gap-8 box-shadow animate-[pulse_1s_ease-in-out_3]">
  <div class="w-full">
    <h1 class="text-6xl font-semi-bold orbitron  text-white">Among Us - Mentor</h1>
    <div class="gap-4 flex flex-col mt-8">
        <div class="text-white flex flex-col" v-for="task in tasks.entries() " >
            <button v-on:click="taskclick(task[0])" class="bitcount-grid-double p-2 bg-gradient-to-br from-indigo-500/10 to-indigo-700/10  drop-shadow-3xl backdrop-blur-md border border-white/20 transform -skew-x-12 ring-1 ring-inset ring-indigo-400/40 shadow-3xl text-xl">
                {{ task[1][0] }}
            </button>
            <div class="flex flex-row gap-4 px-16 py-4 " v-if="task[0]==selectedtask">
                <select v-model="selected_ninja" name="ninjas" id="ninjas-select" class="text-black w-full -skew-x-12 backdrop-blur-md drop-shadow-3xl ring-1 ring-inset ring-red-400/40">
                    <option v-for="(ninja, index) in ninjas" :value="ninja[0]">{{ ninja[2] }}</option>
                </select>
                <button v-on:click="marcartarefa(selected_ninja,task[1])" class="bitcount-grid-double p-2 bg-gradient-to-br from-red-500/10 to-red-700/10 backdrop-blur-md border border-white/20 transform -skew-x-12 ring-1 ring-inset ring-red-400/40 drop-shadow-4xl text-xl">Marcar tarefa</button>
            </div>
            
        </div>
        <router-link to="/marcar_morte" class="bitcount-grid-double text-center p-2 bg-gradient-to-br from-red-500/10 to-red-700/10 backdrop-blur-md border border-white/20 transform -skew-x-12 ring-1 ring-inset ring-red-400/40 drop-shadow-4xl text-xl text-white">Reportar morte</router-link>
        <router-link to="/convocar_reuniao" class="bitcount-grid-double text-center p-2 bg-gradient-to-br from-red-500/10 to-red-700/10 backdrop-blur-md border border-white/20 transform -skew-x-12 ring-1 ring-inset ring-red-400/40 drop-shadow-4xl text-xl text-white">Convocar reunião de emergência</router-link>
        <router-link to="/meltdown" class="bitcount-grid-double text-center p-2 bg-gradient-to-br from-red-500/10 to-red-700/10 backdrop-blur-md border border-white/20 transform -skew-x-12 ring-1 ring-inset ring-red-400/40 drop-shadow-4xl text-xl text-white">Ativar Meltdown</router-link>
    </div>
  </div>

</main>

</template>


