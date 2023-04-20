<script setup lang="ts">
import SearchInput from "@/components/SearchInput.vue";
//获取子组件传过来的值
const onSearch = (searchData, searchKey) => {
  this.searchKey = searchKey;
  this.searchData = searchData;
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
