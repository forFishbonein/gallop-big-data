<script setup lang="ts">
import { onMounted } from "vue";
onMounted(() => {
  // @ts-ignore
  $(function () {
    var defaultData = [
      {
        text: "<a href='index.html'>Parent 1</a>",
        nodes: [
          {
            text: "Child 1",
            nodes: [
              {
                text: "<span class='link1'>Grandchild 1</span>",
                href: "#grandchild2",
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
      levels: 1,
      data: defaultData,
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
    </div>
    <!-- /Row -->
  </div>
</template>
<style lang="scss" scoped>
.font-color {
  color: $theme-color;
}
</style>
