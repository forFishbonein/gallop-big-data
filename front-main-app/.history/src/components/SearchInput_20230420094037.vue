<script setup lang="ts"></script>

<template>
  <div class="search_box">
    <div class="search_btn" @click="onShow" v-if="!isShow">
      <img @click="clickSearch" src="@/assets/images/icon_search.png" />
      <span>搜索</span>
    </div>
    <div class="search_input" v-if="isShow">
      <img @click="clickSearch" src="@/assets/images/icon_search.png" />
      <input
        v-if="isShow"
        v-model="searchKey"
        placeholder="搜索"
        @blur="clickSearch"
        @keyup.13="clickSearch"
        ref="input"
      />
    </div>
    <a v-if="isShow" @click="onShow">取消</a>
  </div>
</template>

<style lang="scss" scoped></style>
