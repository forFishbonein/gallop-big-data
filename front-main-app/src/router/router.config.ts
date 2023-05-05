import { RouteRecordRaw } from "vue-router";
import Index from "@/Index.vue";
import Home from "@/views/Home.vue";
import Search from "@/views/search/Search.vue";
import Detail from "@/views/detail/Detail.vue";
import DisplayDefault from "@/views/search/DisplayDefault.vue";
import DisplayResult from "@/views/search/DisplayResult.vue";
import Compare from "@/views/compare/CompareContainer.vue";
import Industry from "@/views/compare/Industry.vue";
import Area from "@/views/compare/Area.vue";
import Time from "@/views/compare/Time.vue";
import Predict from "@/views/predict/PredictContainer.vue";
import City from "@/views/predict/City.vue";
import Province from "@/views/predict/Province.vue";
import Indicator from "@/views/predict/Indicator.vue";
import Evaluate from "@/views/evaluate/EvaluateContainer.vue";
import Position from "@/views/evaluate/Position.vue";
import Year from "@/views/evaluate/Year.vue";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";
import NotFound from "@/views/error/NotFound.vue";
import Chat from "@/views/chat/Chat.vue";

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
        path: "home",
        name: "Home",
        // component: () => import("@/views/Home.vue"), //这个不行，会加载不出来
        component: Home,
        meta: { title: "首页", keepAlive: true, showTab: true },
      },
      {
        path: "search",
        name: "Search",
        component: Search,
        meta: { title: "搜索指标页", keepAlive: true, showTab: true },
        redirect: "/search/default",
        children: [
          {
            path: "default",
            name: "DisplayDefault",
            component: DisplayDefault,
            meta: {
              title: "默认页面",
              keepAlive: false,
              showTab: true,
            },
          },
          {
            path: "result/:indiId",
            name: "DisplayResult",
            component: DisplayResult,
            meta: {
              title: "结果页面",
              keepAlive: false,
              showTab: true,
            },
            props(route) {
              return {
                indiId: route.params.indiId,
              };
            },
          },
        ],
      },
      {
        path: "detail",
        name: "Detail",
        component: Detail,
        meta: { title: "指标详情页", keepAlive: true, showTab: true },
        props(route) {
          return {
            keyword: route.params.keyword,
          };
        },
      },
      {
        path: "compare",
        name: "Compare",
        meta: { title: "对比分析页", keepAlive: true, showTab: true },
        component: Compare,
        // component: () => import("@/views/compare/CompareContainer.vue"),
        redirect: "/compare/industry",
        children: [
          {
            path: "industry",
            name: "Industry",
            component: Industry,
            meta: {
              title: "行业对比",
              keepAlive: false,
              showTab: true,
            },
          },
          {
            path: "area",
            name: "Area",
            component: Area,
            meta: {
              title: "地区对比",
              keepAlive: false,
              showTab: true,
            },
          },
          {
            path: "time",
            name: "Time",
            component: Time,
            meta: {
              title: "时间对比",
              keepAlive: false,
              showTab: true,
            },
          },
        ],
      },
      {
        path: "predict",
        name: "Predict",
        component: Predict,
        meta: { title: "预测页面", keepAlive: true, showTab: true },
        redirect: "/predict/indicator",
        children: [
          {
            path: "indicator",
            name: "Indicator",
            component: Indicator,
            meta: {
              title: "根据指标预测",
              keepAlive: false,
              showTab: true,
            },
          },
          {
            path: "city",
            name: "City",
            component: City,
            meta: {
              title: "根据城市预测",
              keepAlive: false,
              showTab: true,
            },
          },
          {
            path: "province",
            name: "Province",
            component: Province,
            meta: {
              title: "根据省份预测",
              keepAlive: false,
              showTab: true,
            },
          },
        ],
      },
      {
        path: "evaluate",
        name: "Evaluate",
        component: Evaluate,
        meta: { title: "评价页面", keepAlive: true, showTab: true },
        redirect: "/evaluate/position",
        children: [
          {
            path: "position",
            name: "Position",
            component: Position,
            meta: {
              title: "按照地区评价",
              keepAlive: false,
              showTab: true,
            },
          },
          {
            path: "year",
            name: "Year",
            component: Year,
            meta: {
              title: "按照年份评价",
              keepAlive: false,
              showTab: true,
            },
          },
        ],
      },
    ],
  },
  {
    path: "/chat",
    name: "Chat",
    component: Chat, //这个不行，会加载不出来
    // component: Home,
    meta: { title: "HaoGPT", keepAlive: true, showTab: true },
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: {
      title: "登录页",
      keepAlive: false,
      showTab: true,
    },
  },
  {
    path: "/signup",
    name: "Register",
    component: Register,
    // component: () => import("@/views/Register.vue"),
    meta: {
      title: "注册页",
      keepAlive: false,
      showTab: true,
    },
  },
  {
    path: "/404",
    name: "notFound",
    component: NotFound,
  },
  {
    path: "/:pathMatch(.*)*", // 此处需特别注意置于最底部
    redirect: "/404",
  },
];
