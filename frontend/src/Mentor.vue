<script setup lang="js">
  import { ref,onMounted } from "vue";
  import usePolling from './composables/usePolling';
  const ninjas=ref([]);
  const emeeting=ref([]);
  const apiCall = async () => {
    const response = await fetch("http://localhost:8000/")
    const data=await response.json ();
    ninjas.value=data.ninjas;
    emeeting.value=data.emeeting;
  };
  onMounted(apiCall);
</script>

<template>
<main class="bg--200 flex flex-row p-4 gap-8 box-shadow">
  <div class="w-full">
    <h1 class="text-6xl font-semi-bold orbitron text-white">Among Us - Mentor</h1>
    
  </div>

</main>

</template>

<style>
body{
  background-color: rgb(17, 0, 33); 
}
</style>
