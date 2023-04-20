<script setup lang="ts">
import { onMounted } from "vue";
import { useRouter } from "vue-router";
import DisplayResult from "./DisplayResult.vue";
const router = useRouter();
const link1 = () => {
  alert(111);
  router.push("/home");
};
onMounted(() => {
  // @ts-ignore
  $(function () {
    var defaultData = [
      {
        text: "Parent 1",
        nodes: [
          {
            text: "Child 1",
            nodes: [
              {
                text: "Grandchild 1",
                href: "#/home",
                tags: ["0"],
              },
              {
                text: "Grandchild 2",
                href: "#grandchild2",
                tags: ["0"],
              },
            ],
          },
          {
            text: "Child 2",
            href: "#child2",
            tags: ["0"],
          },
        ],
      },
      {
        text: "Parent 2",
        href: "#parent2",
        tags: ["0"],
      },
      {
        text: "Parent 3",
        href: "#parent3",
        tags: ["0"],
      },
      {
        text: "Parent 4",
        href: "#parent4",
        tags: ["0"],
      },
      {
        text: "Parent 5",
        href: "#parent5",
        tags: ["0"],
      },
    ];
    // @ts-ignore
    $("#treeview1").treeview({
      levels: 1, //显示一层
      data: defaultData,
      enableLinks: true, //允许使用链接
    });
  });
});
</script>

<template>
  <div class="container-fluid pt-25">
    <!-- Row -->
    <div class="row">
      <!-- <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12"> -->
      <div class="col-sm-4">
        <div class="panel panel-default card-view">
          <div class="panel-heading">
            <div class="pull-left">
              <h6 class="panel-title txt-dark">Default</h6>
            </div>
            <div class="clearfix"></div>
          </div>
          <div class="panel-wrapper collapse in">
            <div class="panel-body">
              <div class="treeview" id="treeview1"></div>
            </div>
          </div>
        </div>
        <!-- </div> -->
      </div>
      <div class="col-sm-4"><router-view></router-view></div>
    </div>
    <!-- /Row -->
  </div>
</template>
<style lang="scss" scoped>
.font-color {
  color: $theme-color;
}
</style>
