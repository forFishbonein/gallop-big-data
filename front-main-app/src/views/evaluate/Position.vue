<script setup lang="ts">
import { ref, onMounted, inject } from "vue";
import { getEvaluateInfoApiProvince } from "@/apis/evaluate";
import ecStat from "echarts-stat";
let echarts = inject("ec"); //引入
const name = ref("");
let result = [];
let haveData = ref(false);
const getScatterEvaluateInfo = async () => {
  // @ts-ignore
  ElMessage({ type: "success", message: "开始计算，请耐心等待！" });
  await getEvaluateInfoApiProvince(name.value)
    .then((res) => {
      // @ts-ignore
      ElMessage({ type: "success", message: "计算成功！" });
      result = res.values;
      // result.forEach((e) => {});
      // @ts-ignore
      result = result.map(function (subArr) {
        return [
          // decodeURI(encodeURIComponent(subArr[0])),
          // @ts-ignore
          subArr[0].toString(),
          // @ts-ignore
          Number(subArr[1].toFixed(2)),
        ];
      });
      console.log(result);
      haveData.value = true;
    })
    .catch((error) => {
      // @ts-ignore
      ElMessage({ type: "error", message: error.message });
    });
  initEcharts();
};
const initEcharts = () => {
  // @ts-ignore
  let myChart = echarts.init(document.getElementById("echarts"));
  // var data = [
  //   [1, 4862.4],
  //   [2, 5294.7],
  //   [3, 5934.5],
  //   [4, 7171.0],
  //   [5, 8964.4],
  //   [6, 10202.2],
  //   [7, 11962.5],
  //   [8, 14928.3],
  //   [9, 16909.2],
  //   [10, 18547.9],
  //   [11, 21617.8],
  //   [12, 26638.1],
  //   [13, 34634.4],
  //   [14, 46759.4],
  //   [15, 58478.1],
  //   [16, 67884.6],
  //   [17, 74462.6],
  //   [18, 79395.7],
  // ];
  // @ts-ignore
  var myRegression = ecStat.regression("exponential", result);

  myRegression.points.sort(function (a, b) {
    return a[0] - b[0];
  });

  let option = {
    // title: {
    //   text: "1981 - 1998 gross domestic product GDP (trillion yuan)",
    //   subtext: "By ecStat.regression",
    //   sublink: "https://github.com/ecomfe/echarts-stat",
    //   left: "center",
    // },
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "cross",
      },
    },
    xAxis: {
      type: "value",
      splitLine: {
        lineStyle: {
          type: "dashed",
        },
      },
      splitNumber: 20,
      min: 2000, // 设置横轴的最小值
      max: 2020, // 设置横轴的最大值
      axisLabel: {
        rotate: 45, // 设置标签的旋转角度为 45 度
      },
    },
    yAxis: {
      type: "value",
      splitLine: {
        lineStyle: {
          type: "dashed",
        },
      },
    },
    series: [
      {
        name: "scatter",
        type: "scatter",
        emphasis: {
          label: {
            show: true,
            position: "left",
            color: "blue",
            fontSize: 16,
          },
        },
        data: result,
      },
      {
        name: "line",
        type: "line",
        showSymbol: false,
        smooth: true,
        data: myRegression.points,
        markPoint: {
          itemStyle: {
            color: "transparent",
          },
          label: {
            show: true,
            position: "left",
            formatter: myRegression.expression,
            color: "#333",
            fontSize: 14,
          },
          data: [
            {
              coord: myRegression.points[myRegression.points.length - 1],
            },
          ],
        },
      },
    ],
  };
  myChart.setOption(option);
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
              对于2000-2020年{{ name }}的经济发展水平的评价
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
                @submit.prevent="getScatterEvaluateInfo"
              >
                <div class="form-group mr-15">
                  <label class="control-label mr-10" for="email_inline"
                    >省份名称:（北京市）</label
                  >
                  <input
                    type="input"
                    class="form-control"
                    id="email_inline"
                    v-model="name"
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
    <div class="col-lg-5 col-md-12 col-sm-12 col-xs-12">
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
            <div id="echarts" class="" style="height: 348px"></div>
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
</style>
