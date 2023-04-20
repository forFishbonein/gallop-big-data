import { RouteRecordRaw } from "vue-router";
import Index from "@/Index.vue";
import Home from "@/views/Home.vue";
import Search from "@/views/search/Search.vue";

export const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Index", //App中包裹Index
    meta: {
      title: "首页",
      keepAlive: true,
      // requireLogin: true, //先加在这里，表示需要登录！
    },
    // component: () => import("@/Index.vue"), //这个不行，会加载不出来
    component: Index,
    redirect: "/home", //Index中包裹Home等组件
    children: [
      {
        path: "/home",
        name: "Home",
        // component: () => import("@/views/Home.vue"), //这个不行，会加载不出来
        component: Home,
        meta: { title: "首页", keepAlive: true, showTab: true },
      },
      {
        path: "/search",
        name: "Search",
        component: Search,
        meta: { title: "搜索指标页", keepAlive: true, showTab: true },
        redirect: "/goTravel/city/list",
        children: [
          {
            path: "list",
            name: "CityList",
            component: () => import("@/views/goTravel/city/CityList.vue"),
            meta: {
              title: "城市列表",
              keepAlive: false,
              showTab: true,
            },
            // beforeEnter: (to, from, next) => {
            //   alert("要进入了");
            //   next();
            // },
            //把route对象直接拆出属性
            /* params刷新一下就没了，更好 */
            props({ params: { keyword } }) {
              return {
                keyword,
              };
            },
          },
          {
            path: "detail/:cityId",
            name: "CityDetail",
            component: () => import("@/views/goTravel/city/CityDetail.vue"),
            meta: {
              title: "城市详情",
              keepAlive: false,
              showTab: true,
            },
            props(route) {
              return {
                cityId: route.params.cityId,
              };
            },
            // children: [
            //   {
            //     path: "canvas",
            //     name: "Canvas",
            //     component: () =>
            //       import("@/views/goTravel/city/CityCanvas.vue"),
            //     meta: {
            //       title: "知识图谱",
            //       keepAlive: false,
            //       showTab: true,
            //     },
            //   },
            // ],
          },
        ],
      },
    ],
  },
];
