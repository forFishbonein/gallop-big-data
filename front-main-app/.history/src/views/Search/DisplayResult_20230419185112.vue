<script setup lang="ts">
const props = defineProps<{
  cityId: string;
}>();
const cityId = props.cityId;
alert(cityId);
</script>

<template>
  <div>你好</div>
</template>

<style lang="scss" scoped></style>
