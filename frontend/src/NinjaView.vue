<script setup lang="js">
  import Ninja from './components/Ninja.vue';
  import { ref,onMounted } from "vue";
  import usePolling from './composables/usePolling';
  import StarBackground from './components/StarBackground.vue';
  const ninjas=ref([]);
  const emeeting=ref([]);
  const global_progress=ref(0);
  const apiCall = async () => {
    const response = await fetch("http://localhost:8000/info")
    const data=await response.json ();
    ninjas.value=data.ninjas;
    emeeting.value=data.emeeting;
    global_progress.value=data.task_progress;
  };
  const { start, clear } = usePolling(apiCall, 1000);
  onMounted(start);
</script>

<template>
<StarBackground />
<main class="relative z-10 bg--200 flex flex-row p-4 gap-8 box-shadow">
  <div class="w-full">
    <h1 class="text-6xl font-semi-bold orbitron text-white">Among Us - Coderdojo 2025</h1>
    <div class=" bg-blue-700/30 h-10 w-30 border -skew-x-12 border-white/20 ">
          <div class="h-full bg-gradient-to-br from-green-500 to-cyan-500 border border-white/20 ring-1 ring-inset ring-indigo-400/40 backdrop-blur-md inset-0" :style="{width: Math.round(global_progress)+'%'}"></div>
      </div>
    <div class="p-4 grid gap-4 grid-cols-3">
      
      <div class="animate-[pulse_1s_ease-in-out_3]" v-for="(ninja, index) in ninjas" ><Ninja :name="ninja[2]" :isImpostor="false" :isDead="ninja[3] != null" :onCooldown="false" :idx="index" progress={{  }}"/></div>
    </div>
    <div class=" flex flex-col absolute z-10 left-1/2 item-center justify-center">
      <div v-if="emeeting[0]==1" class=" -translate-x-1/2 -translate-y-1/2 w-4/5 h-4/5 bg-gradient-to-br from-red-500/10 to-red-700/10  drop-shadow-4xl backdrop-blur-md border border-white/20 transform -skew-x-12 ring-1 ring-inset ring-red-400/40 shadow-3xl ">
      <img v-if="emeeting[2]==0" :src="`public/Call_emergency_meeting.png`" class=" w-1/3 mx-auto align-canter p-1"/>
      <img v-if="emeeting[2]==1" :src="`public/dead_amongus.png`" class=" w-1/3 mx-auto align-canter p-1"/>
      <h1 class="orbitron text-center text-8xl text-white h-2/3">Reunião de Emergência!!</h1>
      <p class="space-mono-regular text-white text-center text-3xl m-4">{{ ninjas[emeeting[1]][2] }} convocou uma reunião</p>
    </div>
    </div>
  </div>

</main>

</template>

<style>
body{
  background-color: rgb(17, 0, 33); 
}
</style>
