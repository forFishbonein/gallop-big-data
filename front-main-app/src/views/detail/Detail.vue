<script setup lang="ts">
import { ref, onMounted, inject } from "vue";
import { onBeforeRouteLeave } from "vue-router";
import { utilStore } from "@/store/util";
import { getBubbleInfoApi, getLineInfoApi } from "@/apis/detail";
import { keywordStore } from "@/store/keyword";
// const props = defineProps<{
//   keyword: string;
// }>();
// const keyword = props.keyword;
// console.log(keyword);
const store = utilStore();
const kstore = keywordStore();
const timeFlag = ref(false);
let echarts = inject("ec"); //引入
let data1 = [];
let allProvinces = [];
let allYears = [];
const getBubbleInfo = async () => {
  await getBubbleInfoApi(kstore.keyword)
    .then((res) => {
      // @ts-ignore
      data1 = res.values;
      console.log(data1);
      // @ts-ignore
      data1 = data1.map(function (subArr) {
        return [
          decodeURI(encodeURIComponent(subArr[0])),
          // @ts-ignore
          subArr[1].toString(),
          subArr[2],
        ];
      });
      console.log(data1);
      allProvinces = data1
        .map(function (subArr) {
          return subArr[0]; // 返回子数组的第一项
        })
        .reduce(function (acc, value) {
          if (!acc.includes(value)) {
            acc.push(value); // 将不重复的子数组第一项放入结果数组中
          }
          return acc;
        }, []);
      allYears = data1
        .map(function (subArr) {
          return subArr[1]; // 返回子数组的第一项
        })
        .reduce(function (acc, value) {
          if (!acc.includes(value)) {
            acc.push(value); // 将不重复的子数组第一项放入结果数组中
          }
          return acc;
        }, []);
      console.log(allProvinces);
      console.log(allYears);
    })
    .catch((error) => {
      // @ts-ignore
      ElMessage({ type: "error", message: error.message });
    });
  initEcharts2();
};
let data2 = [];
const getLineInfo = async () => {
  await getLineInfoApi(kstore.keyword)
    .then((res) => {
      // @ts-ignore
      let temple = res.values;
      temple.forEach((e) => {
        // @ts-ignore
        data2.push({
          name: Math.floor(e[0]) + "年",
          value: e[1].toFixed(2),
        });
      });
    })
    .catch((error) => {
      // @ts-ignore
      ElMessage({ type: "error", message: error.message });
    });
  initLine();
};
/*
提取标签：
const data = [
  { label: '标签1', value: 10 },
  { label: '标签2', value: 20 },
  { label: '标签3', value: 30 }
]

const labels = data.map(item => item.label)
 */
/* 折线图2 */
const initEcharts = () => {
  // @ts-ignore
  if ($("#e_chart_1").length > 0) {
    // @ts-ignore
    var eChart_1 = echarts.init(document.getElementById("e_chart_1"));
    //data
    var data = [220, 182, 191, 234, 190, 330, 310];
    var markLineData = [];
    for (var i = 1; i < data.length; i++) {
      // @ts-ignore
      markLineData.push([
        {
          xAxis: i - 1,
          yAxis: data[i - 1],
          value: (data[i] + data[i - 1]).toFixed(2),
        },
        {
          xAxis: i,
          yAxis: data[i],
        },
      ]);
    }

    //option
    var option = {
      tooltip: {
        trigger: "axis",
        backgroundColor: "rgba(33,33,33,1)",
        borderRadius: 0,
        padding: 10,
        axisPointer: {
          type: "cross",
          label: {
            backgroundColor: "rgba(33,33,33,1)",
          },
        },
        textStyle: {
          color: "#fff",
          fontStyle: "normal",
          fontWeight: "normal",
          fontFamily: "'Roboto', sans-serif",
          fontSize: 12,
        },
      },
      color: ["#667add"],
      grid: {
        show: false,
        top: 100,
        bottom: 10,
        containLabel: true,
      },
      xAxis: {
        data: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
        axisLine: {
          show: false,
        },
        axisLabel: {
          textStyle: {
            color: "#878787",
          },
        },
      },
      yAxis: {
        axisLine: {
          show: false,
        },
        axisLabel: {
          textStyle: {
            color: "#878787",
          },
        },
        splitLine: {
          show: false,
        },
      },
      series: [
        {
          type: "line",
          data: data,
          markPoint: {
            data: [
              { type: "max", name: "最大值" },
              { type: "min", name: "最小值" },
            ],
          },
          markLine: {
            smooth: true,
            effect: {
              show: true,
            },
            distance: 10,
            label: {
              normal: {
                position: "middle",
              },
            },
            symbol: ["none", "none"],
            data: markLineData,
          },
        },
      ],
    };
    eChart_1.setOption(option);
    eChart_1.resize();
  }
};
/* 气泡图 */
const initEcharts2 = () => {
  // @ts-ignore
  if ($("#e_chart_2").length > 0) {
    // @ts-ignore
    var eChart_2 = echarts.init(document.getElementById("e_chart_2"));
    // const data = [
    //   // [
    //   //   [28604, 77, 17096869, "Australia"],
    //   //   [31163, 77.4, 27662440, "Canada"],
    //   //   [1516, 68, 1154605773, "China"],
    //   //   [13670, 74.7, 10582082, "Cuba"],
    //   //   [28599, 75, 4986705, "Finland"],
    //   //   [29476, 77.1, 56943299, "France"],
    //   //   [31476, 75.4, 78958237, "Germany"],
    //   //   [28666, 78.1, 254830, "Iceland"],
    //   //   [1777, 57.7, 870601776, "India"],
    //   //   [29550, 79.1, 122249285, "Japan"],
    //   //   [2076, 67.9, 20194354, "North Korea"],
    //   //   [12087, 72, 42972254, "South Korea"],
    //   //   [24021, 75.4, 3397534, "New Zealand"],
    //   //   [43296, 76.8, 4240375, "Norway"],
    //   //   [10088, 70.8, 38195258, "Poland"],
    //   //   [19349, 69.6, 147568552, "Russia"],
    //   //   [10670, 67.3, 53994605, "Turkey"],
    //   //   [26424, 75.7, 57110117, "United Kingdom"],
    //   //   [37062, 75.4, 252847810, "United States"],
    //   // ],
    //   [
    //     ["A", "Jan", 17096869],
    //     ["B", "Feb", 27662440],
    //     ["C", "Mar", 1154605773],
    //     ["D", "Apr", 10582082],
    //     ["E", "May", 4986705],
    //   ],
    // ];
    // @ts-ignore
    var option2 = {
      // @ts-ignore
      // backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [
      //   {
      //     offset: 0,
      //     color: "#f7f8fa",
      //   },
      //   {
      //     offset: 1,
      //     color: "#cdd0d5",
      //   },
      // ]),
      title: {
        text: `各地区各年份${kstore.keyword}情况`,
        left: "5%",
        top: "3%",
      },
      legend: {
        right: "10%",
        top: "3%",
        data: ["1990"],
      },
      tooltip: {
        trigger: "axis",
        backgroundColor: "rgba(33,33,33,1)",
        borderRadius: 0,
        padding: 10,
        axisPointer: {
          type: "cross",
          label: {
            backgroundColor: "rgba(33,33,33,1)",
          },
        },
        textStyle: {
          color: "#fff",
          fontStyle: "normal",
          fontWeight: "normal",
          fontFamily: "'Roboto', sans-serif",
          fontSize: 12,
        },
      },
      grid: {
        left: "8%",
        top: "10%",
      },
      xAxis: {
        type: "category",
        data: allProvinces,
        // data: ["A", "B", "C", "D", "E"],
        splitLine: {
          lineStyle: {
            type: "dashed",
          },
        },
      },
      yAxis: {
        type: "category",
        data: allYears,
        // data: ["Jan", "Feb", "Mar", "Apr", "May"],
        splitLine: {
          lineStyle: {
            type: "dashed",
          },
        },
        scale: true,
      },
      series: [
        {
          name: "1990",
          data: data1,
          type: "scatter",
          symbolSize: function (data) {
            // return Math.sqrt(data[2]) / 5e2;
            return Math.sqrt(data[2]) / 10;
          },
          emphasis: {
            focus: "series",
            label: {
              show: true,
              formatter: function (param) {
                return param.data[2];
              },
              position: "top",
            },
          },
          itemStyle: {
            shadowBlur: 10,
            shadowColor: "rgba(120, 36, 50, 0.5)",
            shadowOffsetY: 5,
            // @ts-ignore
            color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [
              {
                offset: 0,
                color: "rgb(251, 118, 123)",
              },
              {
                offset: 1,
                color: "rgb(204, 46, 72)",
              },
            ]),
          },
        },
      ],
    };
    eChart_2.setOption(option2);
    eChart_2.resize();
  }
};
const initLine = () => {
  // @ts-ignore
  if ($("#morris_line_chart").length > 0)
    // Line Chart
    // @ts-ignore
    Morris.Line({
      // ID of the element in which to draw the chart.
      element: "morris_line_chart",
      // Chart data records -- each entry in this array corresponds to a point on
      // the chart.
      data: data2,
      // The name of the data record attribute that contains x-visitss.
      xkey: "name",
      // A list of names of data record attributes that contain y-visitss.
      ykeys: ["value"],
      // Labels for the ykeys -- will be displayed when you hover over the
      // chart.
      labels: ["均值"],
      // Disables line smoothing
      pointSize: 1,
      pointStrokeColors: ["#4aa23c"],
      behaveLikeLine: true,
      grid: false,
      gridTextColor: "#878787",
      lineWidth: 2,
      smooth: true,
      hideHover: "auto",
      lineColors: ["#4aa23c"],
      resize: true,
      gridTextFamily: "Roboto",
    });
};
const initMap = () => {
  // @ts-ignore
  $(function () {
    // @ts-ignore
    if ($("#china_map").length > 0) {
      var mapData = {
        "CN-32": 500, // 北京市
        "CN-52": 200, // 天津市
        "CN-53": 800, // 河北省
      };
      // @ts-ignore
      $("#china_map").vectorMap({
        map: "cn_mill",
        // backgroundColor: "#f7f2ea",
        backgroundColor: "#e5e5e5",
        series: {
          regions: [
            {
              values: mapData,
              scale: ["#C8EEFF", "#FFA500"],
              normalizeFunction: "polynomial",
            },
          ],
        },
        onRegionTipShow: function (e, el, code) {
          // console.log(mapData[code + ""]);
          // console.log(code);
          el.html(el.html() + " (Value: " + mapData[code] + ")");
        },
      });
      // .vectorMap("set", "focus", { region: "CN-44" });
    }
  });
};
const displayFlag = ref(1);
// 保证每次进入该页面都会刷新一次的工具方法：
const refresh = () => {
  //refreshFlag为true代表刷新过
  if (!store.refreshFlag) {
    // alert("刷新");
    //还没刷新过
    store.refreshFlag = true; //表示已经刷新了
    // console.log(store.refreshFlag);
    location.reload(); //那就刷新一下
    // setTimeout(function () {
    //   location.reload();
    // }, 1000);
    return;
  } else {
    //已经刷新过了
    store.refreshFlag = false; //表示还没有刷新
    // console.log(store.refreshFlag);

    return; //那就不刷新了
  }
};
refresh(); //调用刷新方法
const province = ref("");
const year = ref("");
const selectOptions = () => {
  alert(province.value);
  alert(year.value);
};
onMounted(() => {
  initEcharts();
  if (kstore.keyword.length > 0) {
    // alert("开始查询");
    getBubbleInfo();
    getLineInfo();
  }
  // initEcharts2();
  initMap();
});
onBeforeRouteLeave((to, from, next) => {
  // 在此处执行你的逻辑
  // 可以进行清理操作或者弹出确认提示框
  kstore.keyword = "";
  // 继续路由导航
  next();
});
</script>

<template>
  <div class="container-fluid pt-25">
    <div class="row row-around">
      <select
        class="selectpicker"
        data-style="btn-primary btn-outline"
        v-model="province"
      >
        <option data-tokens="ketchup mustard" value="">选择省份</option>
        <option data-tokens="ketchup mustard" value="Hot Dog, Fries and a Soda">
          Hot Dog, Fries and a Soda
        </option>
        <option data-tokens="mustard" value="Burger, Shake and a Smile">
          Burger, Shake and a Smile
        </option>
        <option data-tokens="frosting" value="Sugar, Spice and all things nice">
          Sugar, Spice and all things nice
        </option>
      </select>
      <select
        class="selectpicker"
        data-style="btn-primary btn-outline"
        v-model="year"
      >
        <option data-tokens="ketchup mustard" value="">选择年份</option>
        <option data-tokens="ketchup mustard" value="Hot Dog, Fries and a Soda">
          Hot Dog, Fries and a Soda
        </option>
        <option data-tokens="mustard" value="Hot Dog, Fries and a Soda">
          Burger, Shake and a Smile
        </option>
        <option data-tokens="frosting" value="Hot Dog, Fries and a Soda">
          Sugar, Spice and all things nice
        </option>
      </select>
      <button
        class="btn btn-primary btn-outline fancy-button btn-0"
        @click="selectOptions"
      >
        primary
      </button>
    </div>
    <div class="row row-center" v-if="displayFlag === 1">
      <div class="col-lg-10">
        <div class="panel panel-default card-view">
          <div class="panel-heading">
            <div class="pull-left">
              <h6 class="panel-title txt-dark">气泡图</h6>
            </div>
            <div class="clearfix"></div>
          </div>
          <div class="panel-wrapper collapse in">
            <div class="panel-body">
              <div id="e_chart_2" style="height: 450px"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row row-center" v-if="displayFlag === 1">
      <div class="col-lg-10">
        <div class="panel panel-default card-view">
          <div class="panel-heading">
            <div class="pull-left">
              <h6 class="panel-title txt-dark">折线图</h6>
            </div>
            <div class="clearfix"></div>
          </div>
          <div class="panel-wrapper collapse in">
            <div class="panel-body">
              <div id="morris_line_chart" class="morris-chart"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row row-center" v-if="displayFlag === 2">
      <div class="col-lg-10">
        <div class="panel panel-default card-view">
          <div class="panel-heading">
            <div class="pull-left">
              <h6 class="panel-title txt-dark">world map</h6>
            </div>
            <div class="clearfix"></div>
          </div>
          <div class="panel-wrapper collapse in">
            <div class="panel-body">
              <div id="china_map" style="height: 450px"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row row-center" v-if="displayFlag === 3">
      <div class="col-lg-8 col-md-6 col-sm-12 col-xs-12">
        <div class="panel panel-default card-view panel-refresh">
          <div class="refresh-container">
            <div class="la-anim-1"></div>
          </div>
          <div class="panel-heading">
            <div class="pull-left">
              <h6 class="panel-title txt-dark">Line Chart</h6>
            </div>
            <div class="clearfix"></div>
          </div>

          <div class="panel-wrapper collapse in">
            <div id="e_chart_1" class="" style="height: 370px"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="row row-center" v-if="displayFlag === 4">
      <div class="col-lg-8 col-md-6 col-sm-12 col-xs-12">
        <div class="panel panel-default card-view panel-refresh">
          <div class="refresh-container">
            <div class="la-anim-1"></div>
          </div>
          <div class="panel-heading">
            <div class="pull-left">
              <h6 class="panel-title txt-dark">Line Chart</h6>
            </div>
            <div class="clearfix"></div>
          </div>

          <div class="panel-wrapper collapse in">数据展示</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.row-center {
  display: flex;
  justify-content: center;
  align-items: center;
}
.row-around {
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin: 20px 0 40px;
}
.btn-primary {
  margin-left: 0;
  margin-right: 0;
}
::v-deep .bootstrap-select .dropdown-toggle:focus {
  outline: none !important;
}
</style>
