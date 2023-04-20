<script lang="ts">
// import { navPage } from "../api/api";
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
          // @ts-ignore
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
      //搜索
      //   alert(param.keyword);
      //   navPage(param).then((res) => {
      //     if (res.data && res.data.success) {
      //       let searchData = res.data.responData.part3[0].items;
      //       // 将多个参数传给父组件
      this.$emit("onSearch", "123", this.searchKey);
      //     }
      //   });
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

<style lang="scss" scoped>
.search_box {
  margin-bottom: 20px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  > a {
    color: $theme-color;
    font-size: 14px;
    margin-left: 12px;
  }
  .search_input {
    flex: 1;
    height: 36px;
    background: #f7f7f7;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;

    img {
      width: 16px;
      height: 16px;
      margin: 0 12px;
    }
    input {
      flex: 1;
      height: 100%;
      font-size: 14px;
      outline: none;
      background: transparent;
      color: #666;
    }
    input:-moz-placeholder {
      /* Mozilla Firefox 4 to 18 */
      color: #999999;
    }
    input::-moz-placeholder {
      /* Mozilla Firefox 19+ */
      color: #999999;
    }
    input:-ms-input-placeholder {
      color: #999999;
    }
    input::-webkit-input-placeholder {
      color: #999999;
    }
  }
  .search_btn {
    flex: 1;
    height: 36px;
    background: #f7f7f7;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;

    img {
      width: 16px;
      height: 16px;
      margin: 0 12px;
    }
    span {
      font-size: 16px;
      color: #999999;
    }
  }
}
</style>
