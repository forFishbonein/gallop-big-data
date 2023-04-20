<script setup lang="ts">
// import Home from "@/views/Home.vue";
import { onMounted } from "vue";
import { useRoute } from "vue-router";
// import { utilStore } from "@/store/util";
import { useRouter } from "vue-router";
// const store = utilStore();
const route = useRoute();
const router = useRouter();
const goToQuestion = () => {
  // router.push("/goTravel/question");
};

// @ts-ignore
// Message{
//   message:"1111"
// }
onMounted(() => {
  // alert(1111);
});
</script>
<script lang="ts">
var a_idx = 0;
(function ($) {
  $(document).ready(function () {
    // 监听滚动事件
    $(window).on("scroll", function () {
      //判断向下滑动的距离
      // if ($(window).scrollTop() >= 100) {
      //   //将顶部导航栏固定
      //   $(".header").addClass("fixed").fadeIn(1000);
      // } else {
      //   $(".header").removeClass("fixed");
      // }
      /*注：fadeIn和FadeOut必须同时使用，才可以无限产生效果，如果没有用fadeOut，那么下一次的fadeIn就没有用了*/
      if ($(window).scrollTop() >= 500) {
        $(".fixed-button").fadeIn(700).css("display", "flex");
      } else {
        $(".fixed-button").fadeOut(300, function () {
          $(".fixed-button").css("display", "none");
        });
      }
    });
  });
  //@ts-ignore
})(jQuery);
</script>
<template>
  <div class="page-wrapper">
    <BaseHeader></BaseHeader>
    <router-view v-slot="{ Component }">
      <!-- <keep-alive v-if="$route.meta.keepAlive"> -->
      <!-- 只有在一个容器切换时alive才生效，并且只有include可以生效，meta不行 -->
      <keep-alive
        :include="[
          'Home',
          'Country',
          'CountryDetail',
          'ThemeTravel',
          'LocalPlay',
          'LocalTeam',
          'VisaInsurance',
          'News',
          'ContactUs',
        ]"
      >
        <component :is="Component" />
      </keep-alive>
      <!-- <component :is="Component" v-else /> -->
    </router-view>
    <BaseFooter></BaseFooter>
  </div>
</template>

<style lang="scss" scoped></style>
