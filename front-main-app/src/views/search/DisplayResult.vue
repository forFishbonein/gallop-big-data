<script setup lang="ts">
// 引入中文包
import zhCn from "element-plus/lib/locale/lang/zh-cn";
import { ref, reactive, toRefs } from "vue";
import { getPageListInfo, getAllListInfo } from "@/apis/search";
const props = defineProps<{
  indiId: string;
}>();
const indiId = props.indiId;

// alert(indiId);
/* 分页查询的实现 */
let result = ref([]);
const pageParams = reactive({
  total: 0,
  page: 1,
  limit: 6,
});
const { total, page, limit } = toRefs(pageParams);
const getTotalInfo = () => {
  getAllListInfo(indiId)
    .then((res: any) => {
      // @ts-ignore
      total.value = res.values.length;
    })
    .catch((error) => {
      //@ts-ignore
      ElMessage({
        type: "error",
        message: error.message,
      });
    });
};
//得到分页数据
const requestPageListInfo = async () => {
  await getPageListInfo(indiId, limit.value, page.value)
    .then((res: any) => {
      result.value = res.values;
      console.log(result.value);
    })
    .catch((error) => {
      //@ts-ignore
      ElMessage({
        type: "error",
        message: error.message,
      });
    });
};
// requestPageListInfo();
// 回调函数1：每页记录数改变时调用，size：回调参数，表示当前选中的“每页条数”
const changePageSize = (size: number) => {
  limit.value = size; //将页面大小改变
  requestPageListInfo(); //请求新的数据
};

// 回调函数2：改变页码时调用，page：回调参数，表示当前选中的“页码”
const changeCurrentPage = (p: number) => {
  page.value = p; //将当前页数改变
  requestPageListInfo(); //请求新的数据
};
if (indiId) {
  getTotalInfo();
  requestPageListInfo();
}
</script>
<script lang="ts">
//@ts-ignore
(function ($) {
  $(document).ready(function () {
    $(document).on("click", ".full-screen", function (e) {
      // @ts-ignore
      $(this).parents(".panel").toggleClass("fullscreen");
      $(window).trigger("resize");
      return false;
    });
  });
  //@ts-ignore
})(jQuery);
</script>

<template>
  <div class="panel panel-default card-view panel-refresh">
    <div class="refresh-container">
      <div class="la-anim-1"></div>
    </div>
    <div class="panel-heading">
      <div class="pull-left">
        <h6 class="panel-title txt-dark">查询结果</h6>
      </div>
      <div class="pull-right">
        <a href="#" class="pull-left inline-block refresh mr-15">
          <i class="zmdi zmdi-replay"></i>
        </a>
        <a href="#" class="pull-left inline-block full-screen mr-15">
          <i class="zmdi zmdi-fullscreen"></i>
        </a>
        <div class="pull-left inline-block dropdown">
          <a
            class="dropdown-toggle"
            data-toggle="dropdown"
            href="#"
            aria-expanded="false"
            role="button"
            ><i class="zmdi zmdi-more-vert"></i
          ></a>
          <ul class="dropdown-menu bullet dropdown-menu-right" role="menu">
            <li role="presentation">
              <a href="javascript:void(0)" role="menuitem"
                ><i class="icon wb-reply" aria-hidden="true"></i>Edit</a
              >
            </li>
            <li role="presentation">
              <a href="javascript:void(0)" role="menuitem"
                ><i class="icon wb-share" aria-hidden="true"></i>Delete</a
              >
            </li>
            <li role="presentation">
              <a href="javascript:void(0)" role="menuitem"
                ><i class="icon wb-trash" aria-hidden="true"></i>New</a
              >
            </li>
          </ul>
        </div>
      </div>
      <div class="clearfix"></div>
    </div>
    <div class="panel-wrapper collapse in">
      <div class="panel-body row pa-0">
        <div class="table-wrap">
          <div class="table-responsive">
            <table class="table table-hover mb-0">
              <thead>
                <tr>
                  <th>省份</th>
                  <th>年份</th>
                  <th>数值</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, key) in result" :key="key">
                  <td>
                    <span class="txt-dark weight-500">{{
                      decodeURI(encodeURIComponent(item[0]))
                    }}</span>
                  </td>
                  <td>{{ item[1] }}</td>
                  <td>
                    <span class="txt-success">
                      <!-- <i class="zmdi zmdi-caret-up mr-10 font-20"></i
                      > -->
                      <span>{{ item[2] }}</span></span
                    >
                  </td>
                </tr>
              </tbody>
            </table>

            <el-config-provider :locale="zhCn">
              <el-pagination
                :current-page="page"
                :total="total"
                :page-size="limit"
                :page-sizes="[6, 12, 20, 30, 40, 50, 100]"
                style="padding: 30px 40px; text-align: center"
                layout="total, sizes, prev, pager, next, jumper"
                background
                @size-change="changePageSize"
                @current-change="changeCurrentPage"
                hide-on-single-page
                pager-count="5"
                prev-icon="Back"
                next-icon="Right"
                default-page-size="12"
              />
            </el-config-provider>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped></style>
