<script setup lang="ts">
import { ref } from "vue";
import SearchInput from "@/components/SearchInput.vue";
let searchKey2 = ref("");
let searchData2 = ref("");
//获取子组件传过来的值
const onSearch = (searchData, searchKey) => {
  searchKey2.value = searchKey;
  searchData2.value = searchData;
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
