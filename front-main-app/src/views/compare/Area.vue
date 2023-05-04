<script setup lang="ts">
import { onMounted, inject, ref } from "vue";
import chinaJson from "@/assets/json/map/china.json";
import { getAreaInfoApi } from "@/apis/compare";
let echarts = inject("ec"); //引入
let mapOption = {};
let barOption = {};
let currentOption = {};
let myChart;
const modelName = ref("");
let areaInfo = [];
let dataA = [];
let max = 0;
let min = 0;
const top7Items = ref([]);
const remainPercent = ref("");
const getAreaInfo = async () => {
  await getAreaInfoApi()
    .then((res) => {
      console.log(res);
      areaInfo = res.data;
      areaInfo.forEach((e) => {
        let str = "";
        if (
          decodeURI(encodeURIComponent(e.province)).substring(0, 3) ==
            "内蒙古" ||
          decodeURI(encodeURIComponent(e.province)).substring(0, 3) == "黑龙江"
        ) {
          str = decodeURI(encodeURIComponent(e.province)).substring(0, 3);
        } else {
          str = decodeURI(encodeURIComponent(e.province)).substring(0, 2);
        }
        // if (str.endsWith("市") || str.endsWith("省")) {
        //   str = str.slice(0, -1);
        // }
        if (max == 0 || min == 0) {
          max = parseInt(e.GDP);
          min = parseInt(e.GDP);
        } else if (parseInt(e.GDP) > max) {
          max = parseInt(e.GDP);
        } else if (parseInt(e.GDP) < min) {
          min = parseInt(e.GDP);
        }
        dataA.push({
          name: str,
          value: parseInt(e.GDP),
        });
      });
    })
    .catch((error) => {
      // @ts-ignore
      ElMessage({ type: "error", message: error.message });
    });
  initEcharts1();
  // 计算总和
  const total = dataA.reduce((acc, curr) => acc + curr.value, 0);

  // 按数值大小对数组进行排序，并加入所占百分比字段
  dataA
    .sort((a, b) => b.value - a.value)
    .forEach((item) => {
      item.percent = ((item.value / total) * 100).toFixed(2) + "%";
    });

  // 取前7项
  top7Items.value = dataA.slice(0, 7);

  // 计算剩下项的百分比
  const top7Sum = top7Items.value.reduce((acc, curr) => acc + curr.value, 0);
  remainPercent.value = (((total - top7Sum) / total) * 100).toFixed(2) + "%";
};
const initEcharts1 = () => {
  console.log(max);
  console.log(min);
  // @ts-ignore
  myChart = echarts.init(document.getElementById("map-container"));
  // @ts-ignore
  echarts.registerMap("china", chinaJson);
  let dataList = [
    {
      name: "北京",
      value: 16926,
    },
    {
      name: "南海诸岛",
      value: 0,
    },
    {
      name: "天津",
      value: 7275,
    },
    {
      name: "上海",
      value: 19229,
    },
    {
      name: "重庆",
      value: 10393,
    },
    {
      name: "河北",
      value: 18606,
    },
    {
      name: "河南",
      value: 25280,
    },
    {
      name: "云南",
      value: 10058,
    },
    {
      name: "辽宁",
      value: 14359,
    },
    {
      name: "黑龙江",
      value: 8415,
    },
    {
      name: "湖南",
      value: 18345,
    },
    {
      name: "安徽",
      value: 16225,
    },
    {
      name: "山东",
      value: 36541,
    },
    {
      name: "新疆",
      value: 6340,
    },
    {
      name: "江苏",
      value: 46848,
    },
    {
      name: "浙江",
      value: 30128,
    },
    {
      name: "江西",
      value: 11143,
    },
    {
      name: "湖北",
      value: 19728,
    },
    {
      name: "广西",
      value: 9909,
    },
    {
      name: "甘肃",
      value: 4422,
    },
    {
      name: "山西",
      value: 8859,
    },
    {
      name: "内蒙古",
      value: 8607,
    },
    {
      name: "陕西",
      value: 11660,
    },
    {
      name: "吉林",
      value: 6643,
    },
    {
      name: "福建",
      value: 18348,
    },
    {
      name: "贵州",
      value: 6705,
    },
    {
      name: "广东",
      value: 51473,
    },
    {
      name: "青海",
      value: 1352,
    },
    {
      name: "西藏",
      value: 707,
    },
    {
      name: "四川",
      value: 20697,
    },
    {
      name: "宁夏",
      value: 1747,
    },
    {
      name: "海南",
      value: 2449,
    },
    {
      name: "台湾",
      value: 0,
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
  dataA.sort(function (a, b) {
    return a.value - b.value;
  });
  mapOption = {
    visualMap: {
      left: "right",
      min: min,
      max: max,
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
        data: dataA,
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
      data: dataA.map(function (item) {
        return item.name;
      }),
    },
    animationDurationUpdate: 1000,
    series: {
      type: "bar",
      id: "population",
      data: dataA.map(function (item) {
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
  getAreaInfo();
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
            <h6 class="panel-title txt-dark">全国各省市GDP</h6>
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
            <h6 class="panel-title txt-dark">排行榜</h6>
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
                    <tr v-for="(item, index) in top7Items" :key="index">
                      <td>
                        <span class="country-name txt-dark pl-15">{{
                          item.name
                        }}</span>
                      </td>
                      <td class="text-right">
                        <span
                          class="badge badge-warning transparent-badge weight-500"
                          >{{ item.percent }}</span
                        >
                      </td>
                    </tr>
                    <tr>
                      <td class="txt-dark">其他</td>

                      <td class="text-right">
                        <span
                          class="badge badge-warning transparent-badge weight-500"
                          >{{ remainPercent }}</span
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
  height: 400px;
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
