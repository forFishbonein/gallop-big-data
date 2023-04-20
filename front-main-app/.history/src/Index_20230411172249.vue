<script setup lang="ts">
// import Home from "@/views/Home.vue";
import { onMounted } from "vue";
import { useRoute } from "vue-router";
// import { utilStore } from "@/store/util";
import { useRouter } from "vue-router";
// const store = utilStore();
const route = useRoute();
const router = useRouter();
const goToQuestion = () => {
  // router.push("/goTravel/question");
};

// @ts-ignore
// Message{
//   message:"1111"
// }
onMounted(() => {
  // alert(1111);
});
</script>
<script lang="ts"></script>
<template>
  <div class="page-wrapper">
    <BaseHeader></BaseHeader>
    <router-view v-slot="{ Component }">
      <!-- <keep-alive v-if="$route.meta.keepAlive"> -->
      <!-- 只有在一个容器切换时alive才生效，并且只有include可以生效，meta不行 -->
      <keep-alive :include="['Home']">
        <component :is="Component" />
      </keep-alive>
      <!-- <component :is="Component" v-else /> -->
    </router-view>
    <BaseFooter></BaseFooter>
  </div>
</template>

<style lang="scss" scoped></style>
