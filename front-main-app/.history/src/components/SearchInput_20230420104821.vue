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
      //   this.clickSearch();
    },
    clickSearch() {
      alert(1);
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
      <img src="@/assets/images/icon_search.png" />
      <span>搜索</span>
    </div>
    <div class="search_input" v-if="isShow">
      <img @click="clickSearch" src="@/assets/images/icon_search.png" />
      <!-- @blur="onShow" -->
      <input
        v-if="isShow"
        v-model="searchKey"
        placeholder="搜索"
        @blur="onShow"
        @keydown.enter="clickSearch"
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
    color: $font-color;
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
    animation: shineLight 1.8s infinite;

    img {
      width: 18px;
      height: 18px;
      margin: 0 12px;
      cursor: pointer;
    }
    img:hover {
    }
    input {
      flex: 1;
      height: 100%;
      font-size: 14px;
      outline: none !important;
      //   background: transparent;
      color: #666;
      border: 1px $theme-color solid;
      border-radius: 0 18px 18px 0;
    }
    input:focus {
      outline: none !important;
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
      width: 18px;
      height: 18px;
      margin: 0 12px;
      cursor: pointer;
    }
    span {
      font-size: 16px;
      color: #999999;
    }
  }
}
</style>
