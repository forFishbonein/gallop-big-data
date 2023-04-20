import { RouteRecordRaw } from "vue-router";
import Index from "../Index.vue";
import Login from "@components/login/Login.vue";
import Register from "@components/login/Register.vue";
import Home from "@views/Home.vue";
import TravelPlan from "@/views/makePlan/TravelPlan.vue";
import AllCountry from "@/views/country/AllCountry.vue";
import ThemeTravel from "@/views/themeTravel/ThemeTravel.vue";
import LocalPlay from "@/views/localPlay/LocalPlay.vue";
import LocalTeam from "@/views/localTeam/LocalTeam.vue";
import News from "@/views/xpNews/News.vue";
import ContactUs from "@/views/contact/ContactUs.vue";
import VisaInsurance from "@/views/visaInsurance/VisaInsurance.vue";
import PersonalIndex from "@/views/personal/Index.vue";
// import Visa from "@/views/visaInsurance/Visa.vue";
// import Insurance from "@/views/visaInsurance/Insurance.vue";

export const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Index", //App中包裹Index
    meta: {
      title: "首页",
      keepAlive: true,
      // requireLogin: true, //先加在这里，表示需要登录！
    },
    component: () => import("@/Index.vue"),
    // component: Index,
    redirect: "/home", //Index中包裹Home等组件
    children: [
      {
        path: "/home",
        name: "Home",
        component: () => import("@/views/Home.vue"), //这个不行，会加载不出来
        // component: Home,
        meta: { title: "首页", keepAlive: true, showTab: true },
      },
    ],
  },

  {
    path: "/plan",
    name: "TrvalPlan",
    component: TravelPlan,
    meta: {
      title: "行程制定",
      keepAlive: false,
      showTab: true,
      requireLogin: true,
    },
    //把route对象直接拆出属性
    props({ params: { routeTitle, peopleNum, arriveCity, planId } }) {
      return {
        routeTitle,
        peopleNum,
        arriveCity,
        planId,
      };
    },
  },
];
