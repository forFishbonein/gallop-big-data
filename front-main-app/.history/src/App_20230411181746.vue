<script setup lang="ts">
console.log(
  "---环境变量----", // @ts-ignore
  import.meta.env
);
</script>
<template>
  <router-view></router-view>
</template>

<style>
#nprogress .bar {
  background-color: #c60b1e !important;
  border: 1px #c60b1e solid;
}
</style>
