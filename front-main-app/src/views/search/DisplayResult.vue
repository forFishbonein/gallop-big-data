<script setup lang="ts">
const props = defineProps<{
  indiId: string;
}>();
const indiId = props.indiId;
// alert(indiId);
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
                <tr>
                  <td><span class="txt-dark weight-500">Facebook</span></td>
                  <td>Beavis</td>
                  <td>
                    <span class="txt-success"
                      ><i class="zmdi zmdi-caret-up mr-10 font-20"></i
                      ><span>2.43%</span></span
                    >
                  </td>
                </tr>
                <tr>
                  <td><span class="txt-dark weight-500">Facebook</span></td>
                  <td>Beavis</td>
                  <td>
                    <span class="txt-success"
                      ><i class="zmdi zmdi-caret-up mr-10 font-20"></i
                      ><span>2.43%</span></span
                    >
                  </td>
                </tr>
                <tr>
                  <td><span class="txt-dark weight-500">Facebook</span></td>
                  <td>Beavis</td>
                  <td>
                    <span class="txt-success"
                      ><i class="zmdi zmdi-caret-up mr-10 font-20"></i
                      ><span>2.43%</span></span
                    >
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped></style>
