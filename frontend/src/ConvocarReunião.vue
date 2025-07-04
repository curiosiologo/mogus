<script setup lang="js">
  import { ref,onMounted } from "vue";
  import usePolling from './composables/usePolling';
  import { RouterLink } from "vue-router";
  const ninjas=ref([]);
  const selected_ninja=ref(null);
  const is_death=ref(false);
  const fetchNinjas= async () => {
    const response = await fetch(import.meta.env.VITE_API_URL + "/info");
    const data=await response.json ();
    ninjas.value=data.ninjas;
  };
  const emeeting=ref([]);
  const Convocar= async (selected_ninja, is_death) => {
    const response = await fetch(import.meta.env.VITE_API_URL + `/emergency_meeting_start?ninja=${selected_ninja}&report=${is_death}`);
    
  };
  const { start, clear } = usePolling(fetchNinjas, 1000);
  onMounted(start);
</script>

<template>
<main class="bg--200 flex flex-row p-4 gap-8 box-shadow">
  <div class="w-full">
    <h1 class=" text-6xl font-semi-bold orbitron text-large text-white">Convocar Reunião</h1>  
    <div class="flex justify-end">
        <router-link to="/mentor" class="bitcount-grid-double w-16 text-center align-middle bg-slate-600 -skew-x-12 backdrop-blur-md drop-shadow-3xl ring-1 ring-inset ring-red-400/40 text-white">Home</router-link>       
    </div>

    <div class="gap-4 flex flex-col mt-8">
        
            <div class="bg-slate-600 flex flex-row items-center gap-2 w-full justify-center">
                <input type="checkbox" v-model="is_death">
                <p class="text-white space-mono-regular">Está a reportar uma morte?</p>
            </div>
            <div class="flex flex-row gap-4 px-16 py-4 text-white orbitron"> Quem convocou?
                <select v-model="selected_ninja" name="ninjas" id="ninjas-select" class="text-black w-full -skew-x-12 backdrop-blur-md drop-shadow-3xl ring-1 ring-inset ring-red-400/40">
                    <option v-for="(ninja, index) in ninjas" :value="ninja[0]">{{ ninja[2] }}</option>
                </select>

        <button v-on:click="Convocar(selected_ninja, is_death)" class="p-2 bg-gradient-to-br from-red-500/10 to-red-700/10 backdrop-blur-md border border-white/20 transform -skew-x-12 ring-1 ring-inset ring-red-400/40 drop-shadow-4xl text-xl bitcount-grid-double text-white">Convocar</button>
       
    
    </div>
        <router-link to="/marcar_morte" class="p-2 bg-gradient-to-br from-red-500/10 to-red-700/10 backdrop-blur-md border border-white/20 transform -skew-x-12 ring-1 ring-inset ring-red-400/40 drop-shadow-4xl text-xl text-white bitcount-grid-double text-center">Reportar morte</router-link>
    </div>
  </div>

</main>

</template>

<style>
body{
  background-color: rgb(17, 0, 33); 
}
</style>
