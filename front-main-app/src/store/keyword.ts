import { defineStore } from "pinia";
export const keywordStore = defineStore("keyword", {
  state: () => ({
    // refreshNum: 0,
    keyword: "",
  }),
  getters: {},
  actions: {
    // updateRefreshNum() {
    //   this.refreshNum += 1;
    // },
    // resetRefreshNum() {
    //   this.refreshNum = 0;
    // },
  },
  persist: {
    key: "keyword",
    storage: window.localStorage,
  },
});
