<script setup lang="ts">
import { ref } from "vue";
import SearchInput from "@/components/SearchInput.vue";
let searchKey = ref("");
let searchData = ref("");
//获取子组件传过来的值
const onSearch = (searchData, searchKey) => {
  searchKey.value = searchKey;
  searchData.value = searchData;
  alert(111);
};
</script>

<template>
  <div class="container-fluid pt-25">
    <!-- Row -->
    <div class="row">
      <SearchInput @onSearch="onSearch"></SearchInput>
    </div>
    <!-- /Row -->
  </div>
</template>

<style lang="scss" scoped></style>
