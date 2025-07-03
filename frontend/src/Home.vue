<script setup lang="js">
  import Ninja from './components/Ninja.vue';
  import { ref,onMounted, hydrateOnMediaQuery } from "vue";
  import usePolling from './composables/usePolling';
  const ninjas=ref([]);
  const emeeting=ref([]);
  const apiCall = async () => {
    const response = await fetch("http://localhost:8000/info")
    const data=await response.json ();
    ninjas.value=data.ninjas;
    emeeting.value=data.emeeting;
  };
  const { start, clear } = usePolling(apiCall, 1000);
  onMounted(start);
</script>

<template>
<main class="bg--200 flex flex-row p-4 gap-8 box-shadow">
  <div class="w-full">
    <router-link to="/ninja">Ninja view</router-link>
    <h1 class="text-6xl font-semi-bold orbitron text-white">Among Us - Coderdojo 2025</h1>
    
    <div class="p-4 grid gap-4 grid-cols-3">
      
      <div v-for="(ninja, index) in ninjas" ><Ninja :name="ninja[2]" :isImpostor="ninja[1]" :isDead="ninja[3] != null" :onCooldown="ninja[4]==1" :idx="index" progress="75%"/></div>
    </div>
    <div v-if="emeeting[0]==1" class=" flex flex-col absolute top-1/2 -translate-x-1/2 -translate-y-1/2 z-10 left-1/2 w-4/5 h-4/5 bg-gradient-to-br from-red-500/10 to-red-700/10  drop-shadow-4xl backdrop-blur-md border border-white/20 transform -skew-x-12 ring-1 ring-inset ring-red-400/40 shadow-3xl item-center justify-center ">
      <img v-if="emeeting[2]==0" :src="`public/Call_emergency_meeting.png`" class=" w-100 mx-auto align-canter p-1"/>
      <img v-if="emeeting[2]==1" :src="`public/dead_amongus.png`" class=" w-100 mx-auto align-canter p-1"/>
      <h1 class="orbitron text-center text-8xl text-white">Reunião de Emergência!!</h1>
      <p class="space-mono-regular text-white text-center text-3xl m-4">{{ ninjas[emeeting[1]][2] }} convocou uma reunião</p>
    </div>
  </div>

</main>

</template>

<style>
body{
  background-color: rgb(17, 0, 33); 
}
</style>
