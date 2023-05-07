<script setup lang="ts">
import { ref, onMounted, inject } from "vue";
import { getEvaluateInfoApiYear } from "@/apis/evaluate";
import chinaJson from "@/assets/json/map/china.json";
// import ecStat from "echarts-stat";
let echarts = inject("ec"); //引入
const year = ref("");
let result = [];
let dataMap = [];
let max = 0;
let min = 0;
let haveData = ref(false);
const getMapEvaluateInfo = async () => {
  // @ts-ignore
  ElMessage({ type: "success", message: "开始计算，请耐心等待！" });
  await getEvaluateInfoApiYear(year.value)
    .then((res) => {
      // @ts-ignore
      ElMessage({ type: "success", message: "计算成功！" });
      result = res.values;
      console.log(result);
      result.forEach((e) => {
        let str = "";
        if (
          decodeURI(encodeURIComponent(e[0])).substring(0, 3) == "内蒙古" ||
          decodeURI(encodeURIComponent(e[0])).substring(0, 3) == "黑龙江"
        ) {
          str = decodeURI(encodeURIComponent(e[0])).substring(0, 3);
        } else {
          str = decodeURI(encodeURIComponent(e[0])).substring(0, 2);
        }
        if (max == 0 || min == 0) {
          // @ts-ignore
          max = parseFloat(e[1].toFixed(2));
          // @ts-ignore
          min = parseFloat(e[1].toFixed(2));
          // @ts-ignore
        } else if (parseFloat(e[1].toFixed(2)) > max) {
          // @ts-ignore
          max = parseFloat(e[1].toFixed(2));
          // @ts-ignore
        } else if (parseFloat(e[1].toFixed(2)) < min) {
          // @ts-ignore
          min = parseFloat(e[1].toFixed(2));
        }
        // @ts-ignore
        dataMap.push({
          name: str,
          // @ts-ignore
          value: parseFloat(e[1].toFixed(2)),
        });
        console.log(dataMap);
        haveData.value = true;
      });
    })
    .catch((error) => {
      // @ts-ignore
      ElMessage({ type: "error", message: error.message });
    });
  initEcharts();
};
// let dataMap = [
//   {
//     name: "北京",
//     value: 16926,
//   },
//   {
//     name: "南海诸岛",
//     value: 0,
//   },
//   {
//     name: "天津",
//     value: 7275,
//   },
//   {
//     name: "上海",
//     value: 19229,
//   },
//   {
//     name: "重庆",
//     value: 10393,
//   },
//   {
//     name: "河北",
//     value: 18606,
//   },
//   {
//     name: "河南",
//     value: 25280,
//   },
//   {
//     name: "云南",
//     value: 10058,
//   },
//   {
//     name: "辽宁",
//     value: 14359,
//   },
//   {
//     name: "黑龙江",
//     value: 8415,
//   },
//   {
//     name: "湖南",
//     value: 18345,
//   },
//   {
//     name: "安徽",
//     value: 16225,
//   },
//   {
//     name: "山东",
//     value: 36541,
//   },
//   {
//     name: "新疆",
//     value: 6340,
//   },
//   {
//     name: "江苏",
//     value: 46848,
//   },
//   {
//     name: "浙江",
//     value: 30128,
//   },
//   {
//     name: "江西",
//     value: 11143,
//   },
//   {
//     name: "湖北",
//     value: 19728,
//   },
//   {
//     name: "广西",
//     value: 9909,
//   },
//   {
//     name: "甘肃",
//     value: 4422,
//   },
//   {
//     name: "山西",
//     value: 8859,
//   },
//   {
//     name: "内蒙古",
//     value: 8607,
//   },
//   {
//     name: "陕西",
//     value: 11660,
//   },
//   {
//     name: "吉林",
//     value: 6643,
//   },
//   {
//     name: "福建",
//     value: 18348,
//   },
//   {
//     name: "贵州",
//     value: 6705,
//   },
//   {
//     name: "广东",
//     value: 51473,
//   },
//   {
//     name: "青海",
//     value: 1352,
//   },
//   {
//     name: "西藏",
//     value: 707,
//   },
//   {
//     name: "四川",
//     value: 20697,
//   },
//   {
//     name: "宁夏",
//     value: 1747,
//   },
//   {
//     name: "海南",
//     value: 2449,
//   },
//   {
//     name: "台湾",
//     value: 0,
//   },
//   {
//     name: "香港",
//     value: 5,
//   },
//   {
//     name: "澳门",
//     value: 5,
//   },
// ];
const initEcharts = () => {
  // @ts-ignore
  let myChart = echarts.init(document.getElementById("map-container"));
  // @ts-ignore
  echarts.registerMap("china", chinaJson);
  dataMap.sort(function (a, b) {
    // @ts-ignore
    return a.value - b.value;
  });
  // @ts-ignore
  let mapOption = {
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
        data: dataMap,
      },
    ],
  };
  myChart.setOption(mapOption);
  window.onresize = function () {
    //自适应大小
    myChart.resize();
  };
};
onMounted(() => {
  // initEcharts();
});
</script>

<template>
  <div class="row row-center">
    <div class="col-sm-10">
      <div class="panel panel-default card-view">
        <div class="panel-heading">
          <div class="pull-left">
            <h6 class="panel-title txt-dark">
              {{ year }}年对于各省份的经济发展水平的评价
            </h6>
          </div>
          <div class="clearfix"></div>
        </div>
        <div class="panel-wrapper collapse in">
          <div class="panel-body">
            <div class="form-wrap">
              <form
                class="form-inline"
                autocomplete="off"
                @submit.prevent="getMapEvaluateInfo"
              >
                <div class="form-group mr-15">
                  <label class="control-label mr-10" for="email_inline"
                    >年份:</label
                  >
                  <input
                    type="input"
                    class="form-control"
                    id="email_inline"
                    v-model="year"
                  />
                </div>
                <!-- <div class="form-group mr-15">
                  <label class="control-label mr-10" for="pwd_inline"
                    >Password:</label
                  >
                  <input type="password" class="form-control" id="pwd_inline" />
                </div> -->
                <!-- <div class="checkbox mr-15">
                  <input id="checkbox_inline" type="checkbox" />
                  <label for="checkbox_inline"> remember me </label>
                </div> -->
                <button type="submit" class="btn btn-success btn-anim">
                  <i class="icon-rocket"></i><span class="btn-text">确定</span>
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="row row-center">
    <div class="col-lg-8 col-md-12 col-sm-12 col-xs-12">
      <div
        class="panel panel-default card-view panel-refresh relative"
        v-if="haveData"
      >
        <div class="refresh-container">
          <div class="la-anim-1"></div>
        </div>
        <div class="panel-heading">
          <div class="pull-left">
            <h6 class="panel-title txt-dark">评价结果</h6>
          </div>
          <div class="clearfix"></div>
        </div>
        <div class="panel-wrapper collapse in">
          <div class="panel-body">
            <div id="map-container"></div>
          </div>
        </div>
      </div>
      <el-empty :image-size="200" description="无结果" v-else />
    </div>
  </div>
</template>

<style lang="scss" scoped>
.row-center {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 30px;
}
// .panel-wrapper2 {
//   background: linear-gradient(
//     -90deg,
//     rgba(238, 83, 22, 0.3) 0%,
//     rgba(213, 62, 20, 0.6) 100%
//   );
// }
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
</style>
