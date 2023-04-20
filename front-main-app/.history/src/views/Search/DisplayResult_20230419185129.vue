<script setup lang="ts">
const props = defineProps<{
  indiId: string;
}>();
const indiId = props.indiId;
alert(indiId);
</script>

<template>
  <div>你好</div>
</template>

<style lang="scss" scoped></style>
