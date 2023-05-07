<script setup lang="ts">
import { ref, onMounted, inject, onBeforeMount } from "vue";
import { onBeforeRouteLeave } from "vue-router";
import { utilStore } from "@/store/util";
import {
  getBubbleInfoApi,
  getLineInfoApi,
  getAllProvinces,
  getMapInfoApi,
  getLineInfoByAreaApi,
} from "@/apis/detail";
import { keywordStore } from "@/store/keyword";
// import { useRoute } from "vue-router";
// const route = useRoute();
// console.log(route.params);
// const fromFlag = route.query.param;
// alert(fromFlag);
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
// @ts-ignore
// let provincesName = [];
// const getAllProvincesName = () => {
//   getAllProvinces()
//     .then((res) => {
//       // @ts-ignore
//       provincesName = res.values;
//       console.log(provincesName);
//     })
//     .catch((error) => {
//       // @ts-ignore
//       ElMessage({ type: "error", message: error.message });
//     });
// };
// onBeforeMount(() => {
//   getAllProvincesName();
// });
let mapList = [];
let dictList = [
  ["江苏省", "CN-32"],
  ["贵州省", "CN-52"],
  ["云南省", "CN-53"],
  ["重庆市", "CN-50"],
  ["四川省", "CN-51"],
  ["上海市", "CN-31"],
  ["西藏自治区", "CN-54"],
  ["浙江省", "CN-33"],
  ["内蒙古自治区", "CN-15"],
  ["山西省", "CN-14"],
  ["福建省", "CN-"],
  ["天津市", "CN-12"],
  ["河北省", "CN-13"],
  ["北京市", "CN-11"],
  ["安徽省", "CN-34"],
  ["江西省", "CN-36"],
  ["山东省", "CN-37"],
  ["河南省", "CN-41"],
  ["湖南省", "CN-43"],
  ["湖北省", "CN-42"],
  ["广西壮族自治区", "CN-45"],
  ["广东省", "CN-44"],
  ["海南省", "CN-46"],
  ["新疆维吾尔自治区", "CN-65"],
  ["宁夏回族自治区", "CN-64"],
  ["青海省", "CN-63"],
  ["甘肃省", "CN-62"],
  ["陕西省", "CN-61"],
  ["黑龙江省", "CN-23"],
  ["吉林省", "CN-22"],
  ["辽宁省", "CN-21"],
];
let data3 = {};
const getMapInfo = async () => {
  await getMapInfoApi(kstore.keyword, year.value)
    .then((res) => {
      // @ts-ignore
      mapList = res.values;
      // @ts-ignore
      mapList = mapList.map(function (subArr) {
        return [decodeURI(encodeURIComponent(subArr[0])), subArr[1]];
      });
      mapList.forEach((e) => {
        for (let i = 0; i < dictList.length; i++) {
          if (e[0] == dictList[i][0]) {
            data3[dictList[i][1]] = e[1];
          }
        }
      });
    })
    .catch((error) => {
      // @ts-ignore
      ElMessage({ type: "error", message: error.message });
    });
  initMap();
};
let data4 = [];
let xAxis = [];
const getLineInfo2 = async () => {
  await getLineInfoByAreaApi(kstore.keyword, province.value)
    .then((res) => {
      // @ts-ignore
      res.values.forEach((e) => {
        // @ts-ignore
        xAxis.push(Math.floor(e[0]) + "");
        // @ts-ignore
        data4.push(e[1]);
      });
    })
    .catch((error) => {
      // @ts-ignore
      ElMessage({ type: "error", message: error.message });
    });
  initLine2();
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
const initLine2 = () => {
  // @ts-ignore
  if ($("#e_chart_1").length > 0) {
    // @ts-ignore
    var eChart_1 = echarts.init(document.getElementById("e_chart_1"));
    //data
    var data = data4;
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
        data: xAxis,
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
        text: `各地区各年份 ${kstore.keyword} 情况`,
        left: "5%",
        top: "3%",
      },
      legend: {
        right: "10%",
        top: "3%",
        data: [kstore.keyword],
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
          name: kstore.keyword,
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
  // let dictList = [
  //   ["江苏省", "CN-32"],
  //   ["北京市", "CN-32"],
  // ];
  // @ts-ignore
  $(function () {
    // @ts-ignore
    if ($("#china_map").length > 0) {
      // var mapData = {
      //   "CN-32": 500, // 北京市
      //   "CN-52": 200, // 天津市
      //   "CN-53": 800, // 河北省
      // };
      // @ts-ignore
      $("#china_map").vectorMap({
        map: "cn_mill",
        // backgroundColor: "#f7f2ea",
        backgroundColor: "#e5e5e5",
        series: {
          regions: [
            {
              values: data3,
              scale: ["#C8EEFF", "#FFA500"],
              normalizeFunction: "polynomial",
            },
          ],
        },
        onRegionTipShow: function (e, el, code) {
          // console.log(mapData[code + ""]);
          // console.log(code);
          el.html(el.html() + " (Value: " + data3[code] + ")");
        },
      });
      // .vectorMap("set", "focus", { region: "CN-44" });
    }
  });
};
const displayFlag = ref(0);
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
  if (kstore.keyword.length > 0) {
    if (province.value !== "" && year.value === "") {
      displayFlag.value = 3;
      data4 = [];
      xAxis = [];
      getLineInfo2();
    }
    // else if (province.value === "" && year.value !== "") {
    //   // @ts-ignore
    //   ElMessage({ type: "error", message: "请先选择省份" });
    // }
    else if (province.value === "" && year.value !== "") {
      displayFlag.value = 2;
      /* 地图 */
      data3 = {};
      getMapInfo();
    } else if (province.value === "" && year.value === "") {
      displayFlag.value = 1;
      data1 = [];
      // data2 = [];
      // @ts-ignore
      ElMessage({ type: "error", message: "请先选择内容！" });
      // alert("开始查询");
      getBubbleInfo();
      // getLineInfo();
    } else if (province.value !== "" && year.value !== "") {
      // @ts-ignore
      ElMessage({ type: "error", message: "只能选择二者之一！" });
    }
    // alert(province.value);
    // alert(year.value);
  } else {
    // @ts-ignore
    ElMessage({ type: "warning", message: "请先搜索指标！" });
  }
};
onMounted(() => {
  // alert(111);
  if (kstore.keyword.length > 0) {
    displayFlag.value = 1;
    // alert("开始查询");
    getBubbleInfo();
    getLineInfo();
  } else {
    // @ts-ignore
    ElMessage({ type: "warning", message: "请先搜索指标！" });
  }
  // initEcharts2();
  // initMap();
});
onBeforeRouteLeave((to, from, next) => {
  // 在此处执行你的逻辑
  // 可以进行清理操作或者弹出确认提示框
  kstore.keyword = "";
  store.refreshFlag = false;
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
        <option data-tokens="ketchup mustard" value="北京市">北京市</option>
        <option data-tokens="ketchup mustard" value="天津市">天津市</option>
        <option data-tokens="ketchup mustard" value="河北省">河北省</option>
        <option data-tokens="ketchup mustard" value="山西省">山西省</option>
        <option data-tokens="ketchup mustard" value="内蒙古自治区">
          内蒙古自治区
        </option>
        <option data-tokens="ketchup mustard" value="辽宁省">辽宁省</option>
        <option data-tokens="ketchup mustard" value="吉林省">吉林省</option>
        <option data-tokens="ketchup mustard" value="黑龙江省">黑龙江省</option>
        <option data-tokens="ketchup mustard" value="上海市">上海市</option>
        <option data-tokens="ketchup mustard" value="江苏省">江苏省</option>
        <option data-tokens="ketchup mustard" value="浙江省">浙江省</option>
        <option data-tokens="ketchup mustard" value="安徽省">安徽省</option>
        <option data-tokens="ketchup mustard" value="福建省">福建省</option>
        <option data-tokens="ketchup mustard" value="江西省">江西省</option>
        <option data-tokens="ketchup mustard" value="山东省">山东省</option>
        <option data-tokens="ketchup mustard" value="河南省">河南省</option>
        <option data-tokens="ketchup mustard" value="湖北省">湖北省</option>
        <option data-tokens="ketchup mustard" value="湖南省">湖南省</option>
        <option data-tokens="ketchup mustard" value="广东省">广东省</option>
        <option data-tokens="ketchup mustard" value="广西壮族自治区">
          广西壮族自治区
        </option>
        <option data-tokens="ketchup mustard" value="海南省">海南省</option>
        <option data-tokens="ketchup mustard" value="重庆市">重庆市</option>
        <option data-tokens="ketchup mustard" value="四川省">四川省</option>
        <option data-tokens="ketchup mustard" value="贵州省">贵州省</option>
        <option data-tokens="ketchup mustard" value="云南省">云南省</option>
        <option data-tokens="ketchup mustard" value="西藏自治区">
          西藏自治区
        </option>
        <option data-tokens="ketchup mustard" value="四川省">四川省</option>
        <option data-tokens="ketchup mustard" value="陕西省">陕西省</option>
        <option data-tokens="ketchup mustard" value="甘肃省">甘肃省</option>
        <option data-tokens="ketchup mustard" value="青海省">青海省</option>
        <option data-tokens="ketchup mustard" value="宁夏回族自治区">
          宁夏回族自治区
        </option>
        <option data-tokens="ketchup mustard" value="新疆维吾尔自治区">
          新疆维吾尔自治区
        </option>
        <!-- <option
          data-tokens="ketchup mustard"
          :value="i"
          v-for="(i, k) in provincesName"
          :key="k"
        >
          {{ i }}
        </option> -->
      </select>
      <select
        class="selectpicker"
        data-style="btn-primary btn-outline"
        v-model="year"
      >
        <option data-tokens="ketchup mustard" value="">选择年份</option>
        <option data-tokens="ketchup mustard" value="2000">2000</option>
        <option data-tokens="ketchup mustard" value="2001">2001</option>
        <option data-tokens="ketchup mustard" value="2002">2002</option>
        <option data-tokens="ketchup mustard" value="2003">2003</option>
        <option data-tokens="ketchup mustard" value="2004">2004</option>
        <option data-tokens="ketchup mustard" value="2005">2005</option>
        <option data-tokens="ketchup mustard" value="2006">2006</option>
        <option data-tokens="ketchup mustard" value="2007">2007</option>
        <option data-tokens="ketchup mustard" value="2008">2008</option>
        <option data-tokens="ketchup mustard" value="2009">2009</option>
        <option data-tokens="ketchup mustard" value="2010">2010</option>
        <option data-tokens="ketchup mustard" value="2011">2011</option>
        <option data-tokens="ketchup mustard" value="2012">2012</option>
        <option data-tokens="ketchup mustard" value="2013">2013</option>
        <option data-tokens="ketchup mustard" value="2014">2014</option>
        <option data-tokens="ketchup mustard" value="2015">2015</option>
        <option data-tokens="ketchup mustard" value="2016">2016</option>
        <option data-tokens="ketchup mustard" value="2017">2017</option>
        <option data-tokens="ketchup mustard" value="2018">2018</option>
        <option data-tokens="ketchup mustard" value="2019">2019</option>
        <option data-tokens="ketchup mustard" value="2020">2020</option>
      </select>
      <button
        class="btn btn-primary btn-outline fancy-button btn-0"
        @click="selectOptions"
      >
        确认
      </button>
    </div>
    <div class="row row-center" v-if="displayFlag === 0">
      <div class="col-lg-10">
        <el-empty :image-size="200" description="无结果" />
      </div>
    </div>
    <div class="row row-center" v-if="displayFlag === 1">
      <div class="col-lg-10">
        <div class="panel panel-default card-view">
          <div class="panel-heading">
            <div class="pull-left">
              <h6 class="panel-title txt-dark">指标数据分布</h6>
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
              <h6 class="panel-title txt-dark">指标平均值年份趋势</h6>
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
              <h6 class="panel-title txt-dark">省份指标数值</h6>
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
              <h6 class="panel-title txt-dark">年份趋势</h6>
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
