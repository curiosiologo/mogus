<template>
  <div class="fixed inset-0 z-0">
    <canvas ref="canvas" class="w-full h-full"></canvas>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';

const canvas = ref(null);
let ctx, width, height;
let stars = [];
let shootingStars = [];

const numStars = 150;

function createStar() {
  return {
    x: Math.random() * width,
    y: Math.random() * height,
    radius: Math.random() * 1.2,
    speed: Math.random() * 0.5 + 0.1,
  };
}

function createShootingStar() {
  return {
    x: Math.random() * width,
    y: Math.random() * height * 0.5,
    length: Math.random() * 80 + 20,
    speed: Math.random() * 10 + 6,
    size: Math.random() * 2 + 1,
    life: 0,
    maxLife: 60,
  };
}

function draw() {
  ctx.clearRect(0, 0, width, height);
  ctx.fillStyle = '#000';
  ctx.fillRect(0, 0, width, height);

  // Stars
  ctx.fillStyle = '#ffffff';
  stars.forEach((star) => {
    star.y += star.speed;
    if (star.y > height) star.y = 0;
    ctx.beginPath();
    ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
    ctx.fill();
  });

  // Shooting Stars
  for (let i = 0; i < shootingStars.length; i++) {
    let s = shootingStars[i];
    ctx.strokeStyle = 'white';
    ctx.lineWidth = s.size;
    ctx.beginPath();
    ctx.moveTo(s.x, s.y);
    ctx.lineTo(s.x + s.length, s.y + s.length * 0.3);
    ctx.stroke();

    s.x += s.speed;
    s.y += s.speed * 0.3;
    s.life++;

    if (s.life > s.maxLife) {
      shootingStars.splice(i, 1);
      i--;
    }
  }

  if (Math.random() < 0.01) {
    shootingStars.push(createShootingStar());
  }

  requestAnimationFrame(draw);
}

onMounted(() => {
  const c = canvas.value;
  ctx = c.getContext('2d');
  width = c.width = window.innerWidth;
  height = c.height = window.innerHeight;

  stars = Array.from({ length: numStars }, createStar);

  window.addEventListener('resize', () => {
    width = c.width = window.innerWidth;
    height = c.height = window.innerHeight;
  });

  draw();
});
</script>

<style scoped>
canvas {
  background-color: #000;
  display: block;
}
</style>