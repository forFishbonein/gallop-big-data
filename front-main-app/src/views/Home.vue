<script setup lang="ts">
import { ref, reactive, onMounted, inject } from "vue";
import { useRouter } from "vue-router";
import { getPeopleSexApi } from "@/apis/home";
import "echarts-liquidfill";
let echarts = inject("ec"); //引入
const testEcharts = () => {
  // @ts-ignore
  if ($("#e_chart_2").length > 0) {
    // @ts-ignore
    var eChart_2 = echarts.init(document.getElementById("e_chart_2"));
    var option1 = {
      series: [
        {
          type: "liquidFill",
          data: [0.7, 0.5, 0.4],
          color: ["#119dd2", "#d36ee8", "#667add"],
          backgroundStyle: {
            borderWidth: 0,
            color: "rgba(255,255,255,0)",
            shadowBlur: 0,
          },
          itemStyle: {
            normal: {
              shadowBlur: 5,
              shadowColor: "rgba(0, 0, 0, .5)",
            },
          },
          shape: "container",
          outline: {
            show: false,
          },
          label: {
            normal: {
              fontSize: 20,
            },
          },
        },
      ],
    };
    eChart_2.setOption(option1);
    eChart_2.resize();
  }
  // @ts-ignore
  if ($("#e_chart_3").length > 0) {
    // @ts-ignore
    var eChart_3 = echarts.init(document.getElementById("e_chart_3"));
    var option3 = {
      tooltip: {
        trigger: "item",
        formatter: "{a} <br/>{b} : {c} ({d}%)",
        backgroundColor: "rgba(33,33,33,1)",
        borderRadius: 0,
        padding: 10,
        textStyle: {
          color: "#fff",
          fontStyle: "normal",
          fontWeight: "normal",
          fontFamily: "'Roboto', sans-serif",
          fontSize: 12,
        },
      },
      legend: {
        show: false,
      },
      toolbox: {
        show: false,
      },
      calculable: true,
      itemStyle: {
        normal: {
          shadowBlur: 5,
          shadowColor: "rgba(0, 0, 0, 0.5)",
        },
      },
      series: [
        {
          name: "Advertising",
          type: "pie",
          radius: "80%",
          center: ["50%", "50%"],
          roseType: "radius",
          color: ["#119dd2", "#d36ee8", "#667add"],
          label: {
            normal: {
              fontFamily: "'Roboto', sans-serif",
              fontSize: 12,
            },
          },
          data: [
            { value: 8265207754, name: "第一产业生产总值" },
            //46003416813
            { value: 44030132010, name: "第二产业生产总值" },
            //2961858143
            { value: 44060986406, name: "第三产业生产总值" },
            //19386245233
          ].sort(function (a, b) {
            return a.value - b.value;
          }),
        },
      ],
      animationType: "scale",
      animationEasing: "elasticOut",
      animationDelay: function (idx) {
        return Math.random() * 1000;
      },
    };
    eChart_3.setOption(option3);
    eChart_3.resize();
  }
};
let peopleSexInfo = {};
let xData = [];
let yData1 = [];
let yData2 = [];
const getPeopleSex = async () => {
  await getPeopleSexApi()
    .then((res) => {
      console.log(res);
      peopleSexInfo = res;
      for (var key in peopleSexInfo) {
        // @ts-ignore
        xData.push(decodeURI(encodeURIComponent(peopleSexInfo[key][0][0])));
        // @ts-ignore
        yData1.push(peopleSexInfo[key][0][3]);
        // @ts-ignore
        yData2.push(peopleSexInfo[key][0][2]);
      }
    })
    .catch((error) => {
      // @ts-ignore
      ElMessage({ type: "error", message: error.message });
    });
  initEcharts();
};
/* 男女性别数量 */
const initEcharts = () => {
  // @ts-ignore
  if ($("#e_chart_5").length > 0) {
    // @ts-ignore
    var eChart_5 = echarts.init(document.getElementById("e_chart_5"));
    // var xData = (function () {
    //   var data = [];
    //   for (var i = 1; i < 6; i++) {
    //     // @ts-ignore
    //     data.push(i);
    //   }
    //   return data;
    // })();

    var option5 = {
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
        show: false,
        top: 30,
        bottom: 10,
        containLabel: true,
      },
      legend: {
        x: "right",
        data: [],
      },
      calculable: true,
      xAxis: [
        {
          type: "category",
          splitLine: {
            show: false,
          },
          axisLine: {
            show: false,
          },
          axisLabel: {
            textStyle: {
              color: "#878787",
              fontStyle: "normal",
              fontWeight: "normal",
              fontFamily: "'Roboto', sans-serif",
              fontSize: 12,
            },
          },
          axisTick: {
            show: false,
          },
          splitArea: {
            show: false,
          },
          data: xData,
        },
      ],
      yAxis: [
        {
          type: "value",
          splitLine: {
            show: false,
          },
          axisLine: {
            show: false,
          },
          axisLabel: {
            textStyle: {
              color: "#878787",
              fontStyle: "normal",
              fontWeight: "normal",
              fontFamily: "'Roboto', sans-serif",
              fontSize: 12,
            },
          },
          axisTick: {
            show: false,
          },
          splitArea: {
            show: false,
          },
        },
      ],
      series: [
        {
          name: "女性",
          type: "bar",
          stack: "split",
          barMaxWidth: 50,
          barGap: "10%",
          itemStyle: {
            normal: {
              barBorderRadius: 0,
              color: "#667add",
              label: {
                show: true,
                textStyle: {
                  color: "#fff",
                },
                position: "insideTop",
                formatter: function (p) {
                  return p.value > 0 ? p.value : "";
                },
              },
            },
          },
          data: yData1,
        },
        {
          name: "男性",
          type: "bar",
          stack: "split",
          itemStyle: {
            normal: {
              color: "#119dd2",
              barBorderRadius: 0,
              label: {
                show: true,
                position: "top",
                formatter: function (p) {
                  return p.value > 0 ? "▼" + p.value + "" : "";
                },
              },
            },
          },
          data: yData2,
        },
      ],
    };
    eChart_5.setOption(option5);
    eChart_5.resize();
  }
};
let fourCityInfo = {};
// let data1 = [];
// const getFourCityInfo = async () => {
//   await getPeopleSexApi()
//     .then((res) => {
//       console.log(res);
//       fourCityInfo = res;
//       for (var key in fourCityInfo) {
//         let temList = [];
//         // @ts-ignore
//         temList.push(decodeURI(encodeURIComponent(peopleSexInfo[key][0][0])));
//         // @ts-ignore
//         yData1.push(peopleSexInfo[key][0][3]);
//         // @ts-ignore
//         yData2.push(peopleSexInfo[key][0][2]);
//       }
//     })
//     .catch((error) => {
//       // @ts-ignore
//       ElMessage({ type: "error", message: error.message });
//     });
//   initEcharts2();
// };
/* 四个直辖市维度对比 */
const initEcharts2 = () => {
  // @ts-ignore
  if ($("#e_chart_1").length > 0) {
    // alert(111)
    // @ts-ignore
    var eChart_1 = echarts.init(document.getElementById("e_chart_1"));
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
      grid: {
        show: false,
      },

      legend: {
        show: false,
      },

      singleAxis: {
        top: 0,
        bottom: 20,
        axisTick: {
          show: false,
        },
        type: "time",
        axisPointer: {
          animation: true,
          label: {
            show: true,
          },
        },
        axisLabel: {
          textStyle: {
            color: "#878787",
            fontStyle: "normal",
            fontWeight: "normal",
            fontFamily: "'Roboto', sans-serif",
            fontSize: 12,
          },
        },
        axisLine: {
          show: false,
        },
        splitLine: {
          show: false,
        },
      },

      series: [
        {
          type: "themeRiver",
          color: ["#d36ee8", "#119dd2", "#667add"],
          label: {
            normal: {
              show: false,
            },
          },
          itemStyle: {
            emphasis: {
              shadowBlur: 5,
              shadowColor: "rgba(0, 0, 0, 0.5)",
            },
          },
          data: [
            // ["北京", 15, "政府消费"],
            // ["北京", 15, "政府消费"],
            // ["北京", 15, "政府消费"],
            // ["北京", 15, "政府消费"],
            // ["北京", 15, "政府消费"],
            // ["北京", 15, "政府消费"],
            // ["北京", 15, "政府消费"],
            // ["上海", 35, "政府消费"],
            // ["上海", 7, "政府消费"],
            // ["上海", 2, "政府消费"],
            // ["上海", 17, "农村居民消费"],
            // ["上海", 33, "农村居民消费"],
            // ["上海", 40, "农村居民消费"],
            // ["上海", 32, "农村居民消费"],
            // ["上海", 26, "农村居民消费"],
            ["2020/11/21", 35, "农村居民消费"],
            ["2020/11/22", 40, "农村居民消费"],
            ["2020/11/23", 32, "农村居民消费"],
            ["2020/11/24", 26, "农村居民消费"],
            ["2020/11/25", 22, "农村居民消费"],
            ["2020/11/08", 35, "城镇居民消费"],
            ["2020/11/09", 36, "城镇居民消费"],
            ["2020/11/10", 37, "城镇居民消费"],
            ["2020/11/11", 22, "城镇居民消费"],
            ["2020/11/12", 24, "城镇居民消费"],
            ["2020/11/13", 26, "城镇居民消费"],
            ["2020/11/14", 34, "城镇居民消费"],
            ["2020/11/15", 21, "城镇居民消费"],
            ["2020/11/16", 18, "城镇居民消费"],
            ["2020/11/17", 45, "城镇居民消费"],
            ["2020/11/18", 32, "城镇居民消费"],
            ["2020/11/19", 35, "城镇居民消费"],
            ["2020/11/20", 30, "城镇居民消费"],
            ["2020/11/21", 28, "城镇居民消费"],
            ["2020/11/22", 27, "城镇居民消费"],
            ["2020/11/23", 26, "城镇居民消费"],
            ["2020/11/24", 15, "城镇居民消费"],
            ["2020/11/25", 30, "城镇居民消费"],
            ["2020/11/26", 35, "城镇居民消费"],
            ["2020/11/27", 42, "城镇居民消费"],
            ["2020/11/28", 42, "城镇居民消费"],
            ["2020/11/08", 21, "政府消费"],
            ["2020/11/09", 25, "政府消费"],
            ["2020/11/10", 27, "政府消费"],
            ["2020/11/11", 23, "政府消费"],
            ["2020/11/12", 24, "政府消费"],
            ["2020/11/13", 21, "政府消费"],
            ["2020/11/14", 35, "政府消费"],
            ["2020/11/15", 39, "政府消费"],
            ["2020/11/16", 40, "政府消费"],
            ["2020/11/17", 36, "政府消费"],
            ["2020/11/18", 33, "政府消费"],
            ["2020/11/19", 43, "政府消费"],
            ["2020/11/20", 40, "政府消费"],
            ["2020/11/21", 34, "政府消费"],
            ["2020/11/22", 28, "政府消费"],
          ],
        },
      ],
    };
    eChart_1.setOption(option);
    eChart_1.resize();
  }
};
onMounted(() => {
  testEcharts();
  // initEcharts();
  getPeopleSex();
  initEcharts2();
  /*****Resize function start*****/
  var sparkResize, echartResize;
  // @ts-ignore
  $(window)
    .on("resize", function () {
      /*Sparkline Resize*/
      clearTimeout(sparkResize);
      // @ts-ignore
      sparkResize = setTimeout(sparklineLogin, 200);

      /*E-Chart Resize*/
      clearTimeout(echartResize);
      // @ts-ignore
      echartResize = setTimeout(testEcharts, 200);
    })
    .resize();
  /*****Resize function end*****/
});
</script>
<template>
  <div class="container-fluid pt-25">
    <!-- Row -->
    <div class="row">
      <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12">
        <div class="panel panel-default card-view panel-refresh">
          <div class="refresh-container">
            <div class="la-anim-1"></div>
          </div>
          <div class="panel-heading">
            <div class="pull-left">
              <h6 class="panel-title txt-dark">国内生产总值</h6>
            </div>
            <div class="pull-right">
              <a href="#" class="pull-left inline-block refresh mr-15">
                <i class="zmdi zmdi-replay"></i>
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
                <ul
                  class="dropdown-menu bullet dropdown-menu-right"
                  role="menu"
                >
                  <li role="presentation">
                    <a href="javascript:void(0)" role="menuitem"
                      ><i class="icon wb-reply" aria-hidden="true"></i
                      >Devices</a
                    >
                  </li>
                  <li role="presentation">
                    <a href="javascript:void(0)" role="menuitem"
                      ><i class="icon wb-share" aria-hidden="true"></i
                      >General</a
                    >
                  </li>
                  <li role="presentation">
                    <a href="javascript:void(0)" role="menuitem"
                      ><i class="icon wb-trash" aria-hidden="true"></i
                      >Referral</a
                    >
                  </li>
                </ul>
              </div>
            </div>
            <div class="clearfix"></div>
          </div>
          <div class="panel-wrapper collapse in">
            <div class="panel-body">
              <div id="e_chart_3" class="" style="height: 215px"></div>
              <hr class="light-grey-hr row mt-10 mb-15" />
              <div class="label-chatrs">
                <div class="">
                  <span
                    class="clabels clabels-lg inline-block bg-primary mr-10 pull-left"
                  ></span>
                  <span
                    class="clabels-text font-12 inline-block txt-dark capitalize-font pull-left"
                    ><span class="block font-15 weight-500 mb-5">45.73%</span
                    ><span class="block txt-grey">第三产业生产总值</span></span
                  >
                  <div
                    id="sparkline_1"
                    class="pull-right"
                    style="width: 100px; overflow: hidden; margin: 0px auto"
                  ></div>
                  <div class="clearfix"></div>
                </div>
              </div>
              <hr class="light-grey-hr row mt-10 mb-15" />
              <div class="label-chatrs">
                <div class="">
                  <span
                    class="clabels clabels-lg inline-block bg-purple mr-10 pull-left"
                  ></span>
                  <span
                    class="clabels-text font-12 inline-block txt-dark capitalize-font pull-left"
                    ><span class="block font-15 weight-500 mb-5">45.69%</span
                    ><span class="block txt-grey">第二产业生产总值</span></span
                  >
                  <div
                    id="sparkline_2"
                    class="pull-right"
                    style="width: 100px; overflow: hidden; margin: 0px auto"
                  ></div>
                  <div class="clearfix"></div>
                </div>
              </div>
              <hr class="light-grey-hr row mt-10 mb-15" />
              <div class="label-chatrs">
                <div class="">
                  <span
                    class="clabels clabels-lg inline-block bg-skyblue mr-10 pull-left"
                  ></span>
                  <span
                    class="clabels-text font-12 inline-block txt-dark capitalize-font pull-left"
                    ><span class="block font-15 weight-500 mb-5">8.58%</span
                    ><span class="block txt-grey">第一产业生产总值</span></span
                  >
                  <div
                    id="sparkline_3"
                    class="pull-right"
                    style="width: 100px; overflow: hidden; margin: 0px auto"
                  ></div>
                  <div class="clearfix"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-lg-5 col-md-6 col-sm-6 col-xs-12">
        <div class="panel panel-default card-view panel-refresh">
          <div class="refresh-container">
            <div class="la-anim-1"></div>
          </div>
          <div class="panel-heading">
            <div class="pull-left">
              <h6 class="panel-title txt-dark">国内消费水平</h6>
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
                <ul
                  class="dropdown-menu bullet dropdown-menu-right"
                  role="menu"
                >
                  <li role="presentation">
                    <a href="javascript:void(0)" role="menuitem"
                      ><i class="icon wb-reply" aria-hidden="true"></i
                      >Devices</a
                    >
                  </li>
                  <li role="presentation">
                    <a href="javascript:void(0)" role="menuitem"
                      ><i class="icon wb-share" aria-hidden="true"></i
                      >General</a
                    >
                  </li>
                  <li role="presentation">
                    <a href="javascript:void(0)" role="menuitem"
                      ><i class="icon wb-trash" aria-hidden="true"></i
                      >Referral</a
                    >
                  </li>
                </ul>
              </div>
            </div>
            <div class="clearfix"></div>
          </div>
          <div class="panel-wrapper collapse in">
            <div class="panel-body">
              <div id="e_chart_1" class="" style="height: 313px"></div>
              <ul class="flex-stat mt-40">
                <li>
                  <span class="block">政府消费水平</span>
                  <span class="block txt-dark weight-500 font-18"
                    ><span>111667.6（亿元）</span></span
                  >
                </li>
                <li>
                  <span class="block">居民消费水平</span>
                  <span class="block txt-dark weight-500 font-18"
                    ><span>325216（亿元)</span></span
                  >
                </li>
                <li>
                  <span class="block">增长</span>
                  <span class="block">
                    <i class="zmdi zmdi-trending-up txt-success font-24"></i>
                  </span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="col-lg-3 col-md-12 col-sm-12 col-xs-12">
        <div class="panel panel-default card-view panel-refresh">
          <div class="refresh-container">
            <div class="la-anim-1"></div>
          </div>
          <div class="panel-heading">
            <div class="pull-left">
              <h6 class="panel-title txt-dark">国内男女人口对比分析</h6>
            </div>
            <div class="pull-right">
              <a href="#" class="pull-left inline-block refresh mr-15">
                <i class="zmdi zmdi-replay"></i>
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
                <ul
                  class="dropdown-menu bullet dropdown-menu-right"
                  role="menu"
                >
                  <li role="presentation">
                    <a href="javascript:void(0)" role="menuitem"
                      ><i class="icon wb-reply" aria-hidden="true"></i>option
                      1</a
                    >
                  </li>
                  <li role="presentation">
                    <a href="javascript:void(0)" role="menuitem"
                      ><i class="icon wb-share" aria-hidden="true"></i>option
                      2</a
                    >
                  </li>
                  <li role="presentation">
                    <a href="javascript:void(0)" role="menuitem"
                      ><i class="icon wb-trash" aria-hidden="true"></i>option
                      3</a
                    >
                  </li>
                </ul>
              </div>
            </div>
            <div class="clearfix"></div>
          </div>
          <div class="panel-wrapper collapse in">
            <div class="panel-body">
              <div id="e_chart_5" class="" style="height: 260px"></div>
              <hr class="light-grey-hr row mt-10 mb-15" />
              <div class="label-chatrs">
                <div class="">
                  <span
                    class="clabels clabels-lg inline-block bg-blue mr-10 pull-left"
                  ></span>
                  <span
                    class="clabels-text font-12 inline-block txt-dark capitalize-font pull-left"
                    ><span class="block font-16 weight-500 mb-5"
                      ><span>51</span>%</span
                    ><span class="block txt-grey">Male</span></span
                  >
                  <i
                    class="big-rpsn-icon zmdi zmdi-male-alt pull-right txt-primary"
                  ></i>
                  <div class="clearfix"></div>
                </div>
              </div>
              <hr class="light-grey-hr row mt-10 mb-15" />
              <div class="label-chatrs">
                <div class="">
                  <span
                    class="clabels clabels-lg inline-block bg-skyblue mr-10 pull-left"
                  ></span>
                  <span
                    class="clabels-text font-12 inline-block txt-dark capitalize-font pull-left"
                    ><span class="block font-16 weight-500 mb-5"
                      ><span>49</span>%</span
                    ><span class="block txt-grey">Female</span></span
                  >
                  <i
                    class="big-rpsn-icon zmdi zmdi-female pull-right txt-skyblue"
                  ></i>
                  <div class="clearfix"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- <div class="panel panel-default card-view">
          <div class="panel-heading">
            <div class="pull-left">
              <h6 class="panel-title txt-dark">browser stats</h6>
            </div>
            <div class="pull-right">
              <a href="#" class="pull-left inline-block mr-15">
                <i class="zmdi zmdi-download"></i>
              </a>
              <a
                href="#"
                class="pull-left inline-block close-panel"
                data-effect="fadeOut"
              >
                <i class="zmdi zmdi-close"></i>
              </a>
            </div>
            <div class="clearfix"></div>
          </div>
          <div class="panel-wrapper collapse in">
            <div class="panel-body">
              <div>
                <span class="pull-left inline-block capitalize-font txt-dark">
                  google chrome
                </span>
                <span class="label label-primary pull-right">50%</span>
                <div class="clearfix"></div>
                <hr class="light-grey-hr row mt-10 mb-10" />
                <span class="pull-left inline-block capitalize-font txt-dark">
                  mozila firefox
                </span>
                <span class="label label-primary pull-right">10%</span>
                <div class="clearfix"></div>
                <hr class="light-grey-hr row mt-10 mb-10" />
                <span class="pull-left inline-block capitalize-font txt-dark">
                  Internet explorer
                </span>
                <span class="label label-primary pull-right">30%</span>
                <div class="clearfix"></div>
                <hr class="light-grey-hr row mt-10 mb-10" />
                <span class="pull-left inline-block capitalize-font txt-dark">
                  safari
                </span>
                <span class="label label-primary pull-right">10%</span>
                <div class="clearfix"></div>
              </div>
            </div>
          </div>
        </div> -->
        <!-- <div class="panel panel-default card-view">
          <div class="panel-wrapper collapse in">
            <div class="panel-body sm-data-box-1">
              <span
                class="uppercase-font weight-500 font-14 block text-center txt-dark"
                >customer satisfaction</span
              >
              <div class="cus-sat-stat weight-500 txt-primary text-center mt-5">
                <span class="counter-anim">70</span><span>%</span>
              </div>
              <div class="progress-anim mt-20">
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-primary wow animated progress-animated"
                    role="progressbar"
                    aria-valuenow="70"
                    aria-valuemin="0"
                    aria-valuemax="100"
                  ></div>
                </div>
              </div>
              <ul class="flex-stat mt-5">
                <li>
                  <span class="block">Previous</span>
                  <span class="block txt-dark weight-500 font-15">79.82</span>
                </li>
                <li>
                  <span class="block">% Change</span>
                  <span class="block txt-dark weight-500 font-15">+14.29</span>
                </li>
                <li>
                  <span class="block">Trend</span>
                  <span class="block">
                    <i class="zmdi zmdi-trending-up txt-success font-20"></i>
                  </span>
                </li>
              </ul>
            </div>
          </div>
        </div> -->
      </div>
    </div>
    <!-- /Row -->

    <!-- Row -->
    <div class="row">
      <div class="col-lg-3 col-md-6 col-sm-6 col-xs-12">
        <div class="panel panel-default card-view pa-0">
          <div class="panel-wrapper collapse in">
            <div class="panel-body pa-0">
              <div class="sm-data-box">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-xs-6 text-center pl-0 pr-0 data-wrap-left">
                      <span class="txt-dark block counter"
                        ><span>5.53063%</span></span
                      >
                      <span class="weight-500 uppercase-font block font-13"
                        >人口自然增长率</span
                      >
                    </div>
                    <div class="col-xs-6 text-center pl-0 pr-0 data-wrap-right">
                      <i
                        class="icon-user-following data-right-rep-icon txt-light-grey"
                      ></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-lg-3 col-md-6 col-sm-6 col-xs-12">
        <div class="panel panel-default card-view pa-0">
          <div class="panel-wrapper collapse in">
            <div class="panel-body pa-0">
              <div class="sm-data-box">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-xs-6 text-center pl-0 pr-0 data-wrap-left">
                      <span class="txt-dark block counter"
                        ><span>203950.8</span></span
                      >
                      <span class="weight-500 uppercase-font block"
                        >就业人口</span
                      >
                    </div>
                    <div class="col-xs-6 text-center pl-0 pr-0 data-wrap-right">
                      <i
                        class="icon-control-rewind data-right-rep-icon txt-light-grey"
                      ></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-lg-3 col-md-6 col-sm-6 col-xs-12">
        <div class="panel panel-default card-view pa-0">
          <div class="panel-wrapper collapse in">
            <div class="panel-body pa-0">
              <div class="sm-data-box">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-xs-6 text-center pl-0 pr-0 data-wrap-left">
                      <span class="txt-dark block counter"
                        ><span>711059.34</span></span
                      >
                      <span class="weight-500 uppercase-font block"
                        >国家财政收入</span
                      >
                    </div>
                    <div class="col-xs-6 text-center pl-0 pr-0 data-wrap-right">
                      <i
                        class="icon-layers data-right-rep-icon txt-light-grey"
                      ></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-lg-3 col-md-6 col-sm-6 col-xs-12">
        <div class="panel panel-default card-view pa-0">
          <div class="panel-wrapper collapse in">
            <div class="panel-body pa-0">
              <div class="sm-data-box">
                <div class="container-fluid">
                  <div class="row">
                    <div class="col-xs-6 text-center pl-0 pr-0 data-wrap-left">
                      <span class="txt-dark block counter"
                        ><span>245588.47</span></span
                      >
                      <span class="weight-500 uppercase-font block"
                        >国家财政支出</span
                      >
                    </div>
                    <div
                      class="col-xs-6 text-center pl-0 pr-0 pt-25 data-wrap-right"
                    >
                      <div
                        id="sparkline_4"
                        style="width: 100px; overflow: hidden; margin: 0px auto"
                      ></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- /Row -->

    <!-- Row -->
    <div class="row">
      <div class="col-lg-4 col-md-5 col-sm-12 col-xs-12">
        <div class="panel panel-default card-view panel-refresh">
          <div class="refresh-container">
            <div class="la-anim-1"></div>
          </div>
          <div class="panel-heading">
            <div class="pull-left">
              <h6 class="panel-title txt-dark">国内对外贸易发展水平</h6>
            </div>
            <div class="pull-right">
              <a href="#" class="pull-left inline-block refresh mr-15">
                <i class="zmdi zmdi-replay"></i>
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
                <ul
                  class="dropdown-menu bullet dropdown-menu-right"
                  role="menu"
                >
                  <li role="presentation">
                    <a href="javascript:void(0)" role="menuitem"
                      ><i class="icon wb-reply" aria-hidden="true"></i>option
                      1</a
                    >
                  </li>
                  <li role="presentation">
                    <a href="javascript:void(0)" role="menuitem"
                      ><i class="icon wb-share" aria-hidden="true"></i>option
                      2</a
                    >
                  </li>
                  <li role="presentation">
                    <a href="javascript:void(0)" role="menuitem"
                      ><i class="icon wb-trash" aria-hidden="true"></i>option
                      3</a
                    >
                  </li>
                </ul>
              </div>
            </div>
            <div class="clearfix"></div>
          </div>
          <div class="panel-wrapper collapse in">
            <div class="panel-body">
              <div id="e_chart_2" class="" style="height: 236px"></div>
              <div class="label-chatrs text-center mt-30">
                <div class="inline-block mr-15">
                  <span class="clabels inline-block bg-primary mr-5"></span>
                  <span
                    class="clabels-text font-12 inline-block txt-dark capitalize-font"
                    >经营单位</span
                  >
                </div>
                <div class="inline-block mr-15">
                  <span class="clabels inline-block bg-purple mr-5"></span>
                  <span
                    class="clabels-text font-12 inline-block txt-dark capitalize-font"
                    >外商投资企业</span
                  >
                </div>
                <div class="inline-block">
                  <span class="clabels inline-block bg-skyblue mr-5"></span>
                  <span
                    class="clabels-text font-12 inline-block txt-dark capitalize-font"
                    >境内目的地货源地</span
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-lg-8 col-md-7 col-sm-12 col-xs-12">
        <div class="panel panel-default card-view panel-refresh">
          <div class="refresh-container">
            <div class="la-anim-1"></div>
          </div>
          <div class="panel-heading">
            <div class="pull-left">
              <h6 class="panel-title txt-dark">重点城市受高等教育发展情况</h6>
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
                <ul
                  class="dropdown-menu bullet dropdown-menu-right"
                  role="menu"
                >
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
                        <th>area</th>
                        <th>count（w）</th>
                        <th>Changes</th>
                        <th>different(w)</th>
                        <!--                        <th>Status</th>-->
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>
                          <span class="txt-dark weight-500">北京</span>
                        </td>
                        <td>13.08</td>
                        <td>
                          <span class="txt-success"
                            ><i class="zmdi zmdi-caret-up mr-10 font-20"></i
                            ><span>0.076%</span></span
                          >
                        </td>
                        <td>
                          <span class="txt-dark weight-500">0.01</span>
                        </td>
                        <!--                        <td>-->
                        <!--                          <span class="label label-primary">Active</span>-->
                        <!--                        </td>-->
                      </tr>
                      <tr>
                        <td>
                          <span class="txt-dark weight-500">天津</span>
                        </td>
                        <td>8.92</td>
                        <td>
                          <span class="txt-success"
                            ><i class="zmdi zmdi-caret-up mr-10 font-20"></i
                            ><span>1.133%</span></span
                          >
                        </td>
                        <td>
                          <span class="txt-dark weight-500">0.1</span>
                        </td>
                        <!--                        <td>-->
                        <!--                          <span class="label label-danger">Closed</span>-->
                        <!--                        </td>-->
                      </tr>
                      <tr>
                        <td>
                          <span class="txt-dark weight-500">上海</span>
                        </td>
                        <td>10.23</td>
                        <td>
                          <span class="txt-success"
                            ><i class="zmdi zmdi-caret-down mr-10 font-20"></i
                            ><span>1.994%</span></span
                          >
                        </td>
                        <td>
                          <span class="txt-dark weight-500">0.2</span>
                        </td>
                        <!--                        <td>-->
                        <!--                          <span class="label label-default">Hold</span>-->
                        <!--                        </td>-->
                      </tr>
                      <tr>
                        <td>
                          <span class="txt-dark weight-500">重庆</span>
                        </td>
                        <td>11.74</td>
                        <td>
                          <span class="txt-success"
                            ><i class="zmdi zmdi-caret-up mr-10 font-20"></i
                            ><span>1.748%</span></span
                          >
                        </td>
                        <td>
                          <span class="txt-dark weight-500">0.09</span>
                        </td>
                        <!--                        <td>-->
                        <!--                          <span class="label label-default">Hold</span>-->
                        <!--                        </td>-->
                      </tr>
                      <tr>
                        <td>
                          <span class="txt-dark weight-500">武汉</span>
                        </td>
                        <td>22.7</td>
                        <td>
                          <span class="txt-success"
                            ><i class="zmdi zmdi-caret-up mr-10 font-20"></i
                            ><span>0.773%</span></span
                          >
                        </td>
                        <td>
                          <span class="txt-dark weight-500">0.39</span>
                        </td>
                        <!--                        <td>-->
                        <!--                          <span class="label label-primary">Active</span>-->
                        <!--                        </td>-->
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
    <!-- Row -->
  </div>
</template>

<style lang="scss" scoped></style>
