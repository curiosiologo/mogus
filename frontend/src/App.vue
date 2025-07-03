<script setup lang="ts">
import Ninja from './components/Ninja.vue';
</script>

<template>
<main class="bg--200 flex flex-row p-4 gap-8 box-shadow">
  <div class="w-full">
    <h1 class="text-6xl font-semi-bold orbitron text-white">Among Us - Coderdojo 2025</h1>
    
    <div class="p-4 grid grid-flow-row-dense">
    <Ninja name="Manuel da Silva Pereira" :isImpostor="false" :isDead="false" :onCooldown="true" :idx="0" progress="75%"/>
    </div>
  
  </div>

</main>

</template>

<style>
body{
  background-color: rgb(17, 0, 33); 
}
</style>
