<script lang="ts">
import { navPage } from "../api/api";
export default {
  data() {
    return {
      searchKey: "",
      isShow: false,
    };
  },
  methods: {
    onShow() {
      this.isShow = !this.isShow;
      if (this.isShow) {
        //input 自动获取焦点
        this.$nextTick(() => {
          this.$refs.input.focus();
        });
      }
      this.searchKey = "";
      this.clickSearch();
    },
    clickSearch() {
      let param = {
        moduleCode: "xmzl_zxjd",
        keyword: this.searchKey.trim(),
      };
      navPage(param).then((res) => {
        if (res.data && res.data.success) {
          let searchData = res.data.responData.part3[0].items;
          // 将多个参数传给父组件
          this.$emit("onSearch", searchData, this.searchKey);
        }
      });
    },
  },
};
</script>

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
