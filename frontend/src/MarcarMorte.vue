<script setup lang="js">
  import { ref,onMounted } from "vue";
  import usePolling from './composables/usePolling';
  const ninjas=ref([]);
  const impostors=ref([]);
  const selected_impostor=ref(null);
  const selected_ninja=ref(null);
  
  const fetchNinjas= async () => {
    const response = await fetch("http://localhost:8000/info")
    const data=await response.json ();
    ninjas.value=data.ninjas.filter((n)=>n[1]==0).filter((n)=>n[3]==null);
    impostors.value=data.ninjas.filter((n)=>n[1]==1).filter((n)=>n[3]==null);
  }
  const reportarmorte= async (ninja, impostor) => {
    const response = await fetch(`http://localhost:8000/matar_ninja?ninja=${ninja}&impostor=${impostor}`);

  }
  
  const { start, clear } = usePolling(fetchNinjas, 1000);
  onMounted(start);
</script>

<template>
<main class="bg--200 flex flex-row p-4 gap-8 box-shadow">
  <div class="w-full">
    <h1 class="text-6xl font-semi-bold orbitron text-white">Marcar Morte</h1>
    <div class="flex justify-end">
        <router-link to="/mentor" class="w-16 space-mono-regular text-center align-middle bg-slate-600 -skew-x-12 backdrop-blur-md drop-shadow-3xl ring-1 ring-inset ring-red-400/40 text-white">Home</router-link>       
    </div> 
    <div class="gap-4 flex flex-col mt-8">
    
            <div class="flex flex-row gap-4 px-16 py-4 text-white orbitron"> Quem morreu?
                <select v-model="selected_ninja" name="ninjas" id="ninjas-select" class="text-black w-full -skew-x-12 backdrop-blur-md drop-shadow-3xl ring-1 ring-inset ring-red-400/40">
                    <option v-for="(ninja, index) in ninjas" :value="ninja[0]">{{ ninja[2] }}</option>
                </select>

                Quem matou?
                <select v-model="selected_impostor" name="ninjas" id="ninjas-select" class="text-black w-full -skew-x-12 backdrop-blur-md drop-shadow-3xl ring-1 ring-inset ring-red-400/40">
                    <option v-for="(ninja, index) in impostors" :value="ninja[0]">{{ ninja[2] }}</option>
                </select>
            </div>
        <button v-on:click="reportarmorte(selected_ninja, selected_impostor)" class=" p-2 orbitron bg-gradient-to-br from-red-500/10 to-red-700/10 backdrop-blur-md border border-white/20 transform -skew-x-12 ring-1 ring-inset ring-red-400/40 drop-shadow-4xl text-xl text-white"><p class="bitcount-grid-double">Reportar Morte</p></button>
       
    </div>
  </div>

</main>

</template>

<style>
body{
  background-color: rgb(17, 0, 33); 
}
</style>
