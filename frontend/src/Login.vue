<template>
    <form @submit.prevent="login" class="flex gap-4">
        <input type="password" v-model="password">
        <button class="text-white" type="submit">
            Login
        </button>
    </form>
</template>

<script setup lang="js">
    import { ref } from "vue";
    import { useRouter } from "vue-router";
    const password = ref("");
    const router = useRouter();
    const login = () => {
        if (password.value == "stringqualquer") {
            router.push("/mentor")
            localStorage["logged_in"] = true;
        } else {
            alert("password incorecta");
            password.value = "";
        }
    }
</script>