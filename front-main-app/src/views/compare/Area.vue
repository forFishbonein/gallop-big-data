<script setup lang="ts">
import { onMounted, inject, ref } from "vue";
import chinaJson from "@/assets/json/map/china.json";
let echarts = inject("ec"); //引入
let mapOption = {};
let barOption = {};
let currentOption = {};
let myChart;
const modelName = ref("");
const initEcharts = () => {
  // @ts-ignore
  myChart = echarts.init(document.getElementById("map-container"));
  // @ts-ignore
  echarts.registerMap("china", chinaJson);
  let dataList = [
    {
      name: "北京",
      value: 54,
    },
    {
      name: "南海诸岛",
      value: 0,
    },
    {
      name: "天津",
      value: 13,
    },
    {
      name: "上海",
      value: 40,
    },
    {
      name: "重庆",
      value: 75,
    },
    {
      name: "河北",
      value: 13,
    },
    {
      name: "河南",
      value: 83,
    },
    {
      name: "云南",
      value: 11,
    },
    {
      name: "辽宁",
      value: 19,
    },
    {
      name: "黑龙江",
      value: 15,
    },
    {
      name: "湖南",
      value: 69,
    },
    {
      name: "安徽",
      value: 60,
    },
    {
      name: "山东",
      value: 39,
    },
    {
      name: "新疆",
      value: 4,
    },
    {
      name: "江苏",
      value: 31,
    },
    {
      name: "浙江",
      value: 104,
    },
    {
      name: "江西",
      value: 36,
    },
    {
      name: "湖北",
      value: 1052,
    },
    {
      name: "广西",
      value: 33,
    },
    {
      name: "甘肃",
      value: 7,
    },
    {
      name: "山西",
      value: 9,
    },
    {
      name: "内蒙古",
      value: 7,
    },
    {
      name: "陕西",
      value: 22,
    },
    {
      name: "吉林",
      value: 4,
    },
    {
      name: "福建",
      value: 18,
    },
    {
      name: "贵州",
      value: 5,
    },
    {
      name: "广东",
      value: 98,
    },
    {
      name: "青海",
      value: 1,
    },
    {
      name: "西藏",
      value: 0,
    },
    {
      name: "四川",
      value: 44,
    },
    {
      name: "宁夏",
      value: 4,
    },
    {
      name: "海南",
      value: 22,
    },
    {
      name: "台湾",
      value: 3,
    },
    {
      name: "香港",
      value: 5,
    },
    {
      name: "澳门",
      value: 5,
    },
  ];
  dataList.sort(function (a, b) {
    return a.value - b.value;
  });
  mapOption = {
    visualMap: {
      left: "right",
      min: 0,
      max: 100,
      inRange: {
        // prettier-ignore
        color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026'],
      },
      text: ["High", "Low"],
      calculable: true,
    },
    series: [
      {
        id: "population",
        type: "map",
        roam: true,
        map: "china",
        animationDurationUpdate: 1000,
        universalTransition: true,
        data: dataList,
      },
    ],
  };
  barOption = {
    xAxis: {
      type: "value",
    },
    yAxis: {
      type: "category",
      axisLabel: {
        rotate: 30,
      },
      data: dataList.map(function (item) {
        return item.name;
      }),
    },
    animationDurationUpdate: 1000,
    series: {
      type: "bar",
      id: "population",
      data: dataList.map(function (item) {
        return item.value;
      }),
      universalTransition: true,
    },
  };
  currentOption = mapOption;
  myChart.setOption(mapOption);
  modelName.value = "地图模式";
  //   setInterval(, 2000);
  window.onresize = function () {
    //自适应大小
    myChart.resize();
  };
};
const changeModel = () => {
  // @ts-ignore
  currentOption = currentOption === mapOption ? barOption : mapOption;
  modelName.value = modelName.value === "地图模式" ? "条形图模式" : "地图模式";
  // @ts-ignore
  myChart.setOption(currentOption, true);
};
onMounted(() => {
  initEcharts();
  // @ts-ignore
  $(document).ready(function () {
    /* Switchery Init*/
    var elems = Array.prototype.slice.call(
      document.querySelectorAll(".js-switch")
    );
    // @ts-ignore
    $(".js-switch-1").each(function () {
      // @ts-ignore
      new Switchery($(this)[0], $(this).data());
    });
  });
});
</script>

<template>
  <div class="row row-center">
    <div class="col-lg-8 col-md-6 col-sm-12 col-xs-12">
      <div class="panel panel-default card-view panel-refresh">
        <div class="refresh-container">
          <div class="la-anim-1"></div>
        </div>
        <div class="panel-heading">
          <div class="pull-left pull-left2">
            <h6 class="panel-title txt-dark">Line Chart</h6>
            <div @click="changeModel" class="change-button">
              <input
                type="checkbox"
                checked
                class="js-switch js-switch-1"
                data-color="#667add"
                data-size="small"
              />
              <span v-text="modelName" style="margin-left: 10px"></span>
            </div>
          </div>
          <div class="clearfix"></div>
        </div>
        <div class="panel-wrapper panel-wrapper2 collapse in">
          <div id="map-container"></div>
        </div>
      </div>
    </div>
    <div class="col-lg-3 col-md-6 col-sm-6 col-xs-12">
      <div class="panel panel-default card-view">
        <div class="panel-heading">
          <div class="pull-left pull-left2">
            <h6 class="panel-title txt-dark">browser stats</h6>
          </div>
          <div class="pull-right">
            <a href="#" class="pull-left inline-block mr-15">
              <i class="zmdi zmdi-download"></i>
            </a>
            <a
              href="#"
              class="pull-left pull-left2 inline-block close-panel"
              data-effect="fadeOut"
            >
              <i class="zmdi zmdi-close"></i>
            </a>
          </div>
          <div class="clearfix"></div>
        </div>
        <div class="panel-wrapper collapse in">
          <div class="panel-body row">
            <div class="table-wrap sm-data-box-2">
              <div class="table-responsive">
                <table class="table top-countries mb-0">
                  <tbody>
                    <tr>
                      <td>
                        <img src="/picture/01-flag.png" alt="country" />
                        <span class="country-name txt-dark pl-15">Aland</span>
                      </td>
                      <td class="text-right">
                        <span
                          class="badge badge-warning transparent-badge weight-500"
                          >57%</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <img src="/picture/02-flag.png" alt="country" />
                        <span class="country-name txt-dark pl-15">Angola</span>
                      </td>
                      <td class="text-right">
                        <span
                          class="badge badge-danger transparent-badge weight-500"
                          >17%</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <img src="/picture/03-flag.png" alt="country" />
                        <span class="country-name txt-dark pl-15"
                          >Anguilla</span
                        >
                      </td>

                      <td class="text-right">
                        <span
                          class="badge badge-info transparent-badge weight-500"
                          >27%</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <img src="/picture/04-flag.png" alt="country" />
                        <span class="country-name txt-dark pl-15">Bahrain</span>
                      </td>
                      <td class="text-right">
                        <span
                          class="badge badge-danger transparent-badge weight-500"
                          >17%</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <img src="/picture/05-flag.png" alt="country" />
                        <span class="country-name txt-dark pl-15"
                          >Australia</span
                        >
                      </td>
                      <td class="text-right">
                        <span
                          class="badge badge-primary transparent-badge weight-500"
                          >51%</span
                        >
                      </td>
                    </tr>

                    <tr>
                      <td>
                        <img src="/picture/06-flag.png" alt="country" />
                        <span class="country-name txt-dark pl-15">Austria</span>
                      </td>

                      <td class="text-right">
                        <span
                          class="badge badge-warning transparent-badge weight-500"
                          >10%</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td>
                        <img src="/picture/07-flag.png" alt="country" />
                        <span class="country-name txt-dark pl-15">Belgium</span>
                      </td>
                      <td class="text-right">
                        <span
                          class="badge badge-success transparent-badge weight-500"
                          >27%</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td class="txt-dark">Other</td>

                      <td class="text-right">
                        <span
                          class="badge badge-warning transparent-badge weight-500"
                          >10%</span
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
    </div>
  </div>
</template>

<style lang="scss" scoped>
.pull-left2 {
  display: flex;
  justify-content: left;
  align-items: center;
}
.change-button {
  margin-left: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
  ::v-deep .switchery {
    margin: 0 !important;
  }
}
#map-container {
  width: 100%;
  height: 370px;
  //   margin: 0px auto;
  //   margin-top: 10px;
  //   background: linear-gradient(
  //     -90deg,
  //     rgba(238, 83, 22, 0.3) 0%,
  //     rgba(213, 62, 20, 0.6) 100%
  //   );
}
.panel-wrapper2 {
  background: linear-gradient(
    -90deg,
    rgba(238, 83, 22, 0.3) 0%,
    rgba(213, 62, 20, 0.6) 100%
  );
}

.row-center {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
}
</style>
