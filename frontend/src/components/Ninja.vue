<script setup lang="ts">
defineProps<{
  name: string,
  isImpostor: boolean
  isDead: boolean
  idx: number
  onCooldown: boolean
  progress: string
}>()
</script>

<template>
  <div class="flex p-1 h-36 text-white flex-row gap-4 items-center " :class="(isImpostor ? 'bg-gradient-to-br from-red-500/10 to-red-700/10  drop-shadow-4xl backdrop-blur-md border border-white/20 transform -skew-x-12 ring-1 ring-inset ring-red-400/40 ' : 'bg-gradient-to-br from-indigo-400/10 to-purple-600/10 drop-shadow-3xl border border-white/20 transform -skew-x-12 ring-1 ring-inset ring-indigo-400/40 backdrop-blur-md ') + (isDead ? 'opacity-55 ' : 'opacity-100 ')">

    <img :src="`public/amongus_images/${idx}.gif`" class="w-24 p-1"/>
    <h1 class="space-mono-regular p-1 ">{{ name }} <p v-if="onCooldown"> ⏱️ Cooldown</p></h1>
    <div class="w-full h-full">
      <div class="orbitron">{{progress}} Tarefas</div>
      <div class="h-20">
        <div class=" bg-blue-700/30 h-full w-30 border border-white/20 ">
          <div class="h-full bg-gradient-to-br from-green-500 to-cyan-500 border border-white/20 ring-1 ring-inset ring-indigo-400/40 backdrop-blur-md inset-0" :style="{width: progress}"></div>
        </div>
      </div>
    </div>
  </div>
</template>


