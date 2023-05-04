<script setup lang="ts">
import { onMounted } from "vue";
import { useRouter } from "vue-router";
const router = useRouter();
onMounted(() => {
  // @ts-ignore
  $(function () {
    var defaultData = [
      {
        text: "第一产业",
        nodes: [
          {
            text: "农业",
            nodes: [
              {
                text: "地区生产总值",
                href: "#search/result/地区生产总值",
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
            text: "林业",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "畜牧业",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "渔业",
            href: "#child2",
            tags: ["0"],
          },
        ],
      },
      {
        text: "第二产业",
        nodes: [
          {
            text: "工业",
            nodes: [
              {
                text: "地区生产总值",
                href: "#arch/result/地区生产总值",
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
            text: "采矿业",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "制造业",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "建筑业",
            href: "#child2",
            tags: ["0"],
          },
        ],
      },
      {
        text: "第三产业",
        nodes: [
          {
            text: "批发和零售业",
            nodes: [
              {
                text: "Grandchild 1",
                href: "#arch/result/111",
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
            text: "交通运输、仓储和邮政业",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "住宿和餐饮业",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "金融服务业",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "租赁和商贸服务业",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "社会公共服务",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "文化、体育、娱乐业",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "信息传输、软件和信息技术服务业",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "卫生公共服务",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "科研研究与技术服务业",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "教育服务业",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "旅游业",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "房地产",
            href: "#child2",
            tags: ["0"],
          },
        ],
      },
      {
        text: "国民经济核算指标",
        nodes: [
          {
            text: "人口就业与产业结构",
            nodes: [
              {
                text: "人口就业与产业结构",
                href: "#arch/result/111",
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
            text: "专利类",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "创新类",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "金融服务业",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "产业类",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "居民消费类",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "人口统计指标类",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "投资与财证类",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "城市",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "农村",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "自然资源",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "环境",
            href: "#child2",
            tags: ["0"],
          },
        ],
      },
      {
        text: "政府和社会公共服务",
        nodes: [
          {
            text: "社会管理领域",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "社会福利领域",
            href: "#child2",
            tags: ["0"],
          },
          {
            text: "社会保障领域",
            href: "#child2",
            tags: ["0"],
          },
        ],
      },
    ];

    // $(function () {
    //   var defaultData = [
    //     {
    //       text: "Parent 1",
    //       nodes: [
    //         {
    //           text: "Child 1",
    //           nodes: [
    //             {
    //               text: "地区生产总值",
    //               href: "#/search/result/地区生产总值",
    //               tags: ["0"],
    //             },
    //             {
    //               text: "Grandchild 2",
    //               href: "#grandchild2",
    //               tags: ["0"],
    //             },
    //           ],
    //         },
    //         {
    //           text: "Child 2",
    //           href: "#child2",
    //           tags: ["0"],
    //         },
    //       ],
    //     },
    //     {
    //       text: "Parent 2",
    //       href: "#parent2",
    //       tags: ["0"],
    //     },
    //     {
    //       text: "Parent 3",
    //       href: "#parent3",
    //       tags: ["0"],
    //     },
    //     {
    //       text: "Parent 4",
    //       href: "#parent4",
    //       tags: ["0"],
    //     },
    //     {
    //       text: "Parent 5",
    //       href: "#parent5",
    //       tags: ["0"],
    //     },
    //   ];
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
      <div class="col-lg-4">
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
      <div class="col-lg-8 col-md-7 col-sm-12 col-xs-12">
        <router-view></router-view>
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
