<script setup lang="ts">
import { ref, reactive, onMounted, inject } from "vue";
import { useRouter } from "vue-router";
import "echarts-liquidfill";
/* echarts地图 */
let echarts = inject("ec"); //引入
const testEcharts = () => {
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
            ["2015/11/08", 10, "DQ"],
            ["2015/11/09", 15, "DQ"],
            ["2015/11/10", 35, "DQ"],
            ["2015/11/14", 7, "DQ"],
            ["2015/11/15", 2, "DQ"],
            ["2015/11/16", 17, "DQ"],
            ["2015/11/17", 33, "DQ"],
            ["2015/11/18", 40, "DQ"],
            ["2015/11/19", 32, "DQ"],
            ["2015/11/20", 26, "DQ"],
            ["2015/11/21", 35, "DQ"],
            ["2015/11/22", 40, "DQ"],
            ["2015/11/23", 32, "DQ"],
            ["2015/11/24", 26, "DQ"],
            ["2015/11/25", 22, "DQ"],
            ["2015/11/08", 35, "TY"],
            ["2015/11/09", 36, "TY"],
            ["2015/11/10", 37, "TY"],
            ["2015/11/11", 22, "TY"],
            ["2015/11/12", 24, "TY"],
            ["2015/11/13", 26, "TY"],
            ["2015/11/14", 34, "TY"],
            ["2015/11/15", 21, "TY"],
            ["2015/11/16", 18, "TY"],
            ["2015/11/17", 45, "TY"],
            ["2015/11/18", 32, "TY"],
            ["2015/11/19", 35, "TY"],
            ["2015/11/20", 30, "TY"],
            ["2015/11/21", 28, "TY"],
            ["2015/11/22", 27, "TY"],
            ["2015/11/23", 26, "TY"],
            ["2015/11/24", 15, "TY"],
            ["2015/11/25", 30, "TY"],
            ["2015/11/26", 35, "TY"],
            ["2015/11/27", 42, "TY"],
            ["2015/11/28", 42, "TY"],
            ["2015/11/08", 21, "SS"],
            ["2015/11/09", 25, "SS"],
            ["2015/11/10", 27, "SS"],
            ["2015/11/11", 23, "SS"],
            ["2015/11/12", 24, "SS"],
            ["2015/11/13", 21, "SS"],
            ["2015/11/14", 35, "SS"],
            ["2015/11/15", 39, "SS"],
            ["2015/11/16", 40, "SS"],
            ["2015/11/17", 36, "SS"],
            ["2015/11/18", 33, "SS"],
            ["2015/11/19", 43, "SS"],
            ["2015/11/20", 40, "SS"],
            ["2015/11/21", 34, "SS"],
            ["2015/11/22", 28, "SS"],
          ],
        },
      ],
    };
    eChart_1.setOption(option);
    eChart_1.resize();
  }
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
            { value: 335, name: "Active" },
            { value: 310, name: "Closed" },
            { value: 274, name: "Hold" },
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
onMounted(() => {
  testEcharts();
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
<script lang="ts">
(function ($) {
  $(document).ready(function () {});
  //@ts-ignore
})(jQuery);
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
              <h6 class="panel-title txt-dark">Visit by Traffic Types</h6>
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
                    ><span class="block font-15 weight-500 mb-5"
                      >44.46% organic</span
                    ><span class="block txt-grey">356 visits</span></span
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
                    ><span class="block font-15 weight-500 mb-5"
                      >5.54% Refrral</span
                    ><span class="block txt-grey">36 visits</span></span
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
                    ><span class="block font-15 weight-500 mb-5">50% Other</span
                    ><span class="block txt-grey">245 visits</span></span
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
              <h6 class="panel-title txt-dark">user statistics</h6>
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
                  <span class="block">Weekly Users</span>
                  <span class="block txt-dark weight-500 font-18"
                    ><span class="counter-anim">3,24,222</span></span
                  >
                </li>
                <li>
                  <span class="block">Monthly Users</span>
                  <span class="block txt-dark weight-500 font-18"
                    ><span class="counter-anim">1,23,432</span></span
                  >
                </li>
                <li>
                  <span class="block">Trend</span>
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
        <div class="panel panel-default card-view">
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
        </div>
        <div class="panel panel-default card-view">
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
        </div>
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
                        ><span class="counter-anim">914,001</span></span
                      >
                      <span class="weight-500 uppercase-font block font-13"
                        >visits</span
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
                        ><span class="counter-anim">46.41</span>%</span
                      >
                      <span class="weight-500 uppercase-font block"
                        >bounce rate</span
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
                        ><span class="counter-anim">4,054,876</span></span
                      >
                      <span class="weight-500 uppercase-font block"
                        >pageviews</span
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
                        ><span class="counter-anim">46.43</span>%</span
                      >
                      <span class="weight-500 uppercase-font block"
                        >growth rate</span
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
              <h6 class="panel-title txt-dark">Advertising & Promotions</h6>
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
                    >Active</span
                  >
                </div>
                <div class="inline-block mr-15">
                  <span class="clabels inline-block bg-purple mr-5"></span>
                  <span
                    class="clabels-text font-12 inline-block txt-dark capitalize-font"
                    >Closed</span
                  >
                </div>
                <div class="inline-block">
                  <span class="clabels inline-block bg-skyblue mr-5"></span>
                  <span
                    class="clabels-text font-12 inline-block txt-dark capitalize-font"
                    >Hold</span
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
              <h6 class="panel-title txt-dark">social campaigns</h6>
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
                        <th>Campaign</th>
                        <th>Client</th>
                        <th>Changes</th>
                        <th>Budget</th>
                        <th>Status</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>
                          <span class="txt-dark weight-500">Facebook</span>
                        </td>
                        <td>Beavis</td>
                        <td>
                          <span class="txt-success"
                            ><i class="zmdi zmdi-caret-up mr-10 font-20"></i
                            ><span>2.43%</span></span
                          >
                        </td>
                        <td>
                          <span class="txt-dark weight-500">$1478</span>
                        </td>
                        <td>
                          <span class="label label-primary">Active</span>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <span class="txt-dark weight-500">Youtube</span>
                        </td>
                        <td>Felix</td>
                        <td>
                          <span class="txt-success"
                            ><i class="zmdi zmdi-caret-up mr-10 font-20"></i
                            ><span>1.43%</span></span
                          >
                        </td>
                        <td>
                          <span class="txt-dark weight-500">$951</span>
                        </td>
                        <td>
                          <span class="label label-danger">Closed</span>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <span class="txt-dark weight-500">Twitter</span>
                        </td>
                        <td>Cannibus</td>
                        <td>
                          <span class="txt-danger"
                            ><i class="zmdi zmdi-caret-down mr-10 font-20"></i
                            ><span>-8.43%</span></span
                          >
                        </td>
                        <td>
                          <span class="txt-dark weight-500">$632</span>
                        </td>
                        <td>
                          <span class="label label-default">Hold</span>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <span class="txt-dark weight-500">Spotify</span>
                        </td>
                        <td>Neosoft</td>
                        <td>
                          <span class="txt-success"
                            ><i class="zmdi zmdi-caret-up mr-10 font-20"></i
                            ><span>7.43%</span></span
                          >
                        </td>
                        <td>
                          <span class="txt-dark weight-500">$325</span>
                        </td>
                        <td>
                          <span class="label label-default">Hold</span>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <span class="txt-dark weight-500">Instagram</span>
                        </td>
                        <td>Hencework</td>
                        <td>
                          <span class="txt-success"
                            ><i class="zmdi zmdi-caret-up mr-10 font-20"></i
                            ><span>9.43%</span></span
                          >
                        </td>
                        <td>
                          <span class="txt-dark weight-500">$258</span>
                        </td>
                        <td>
                          <span class="label label-primary">Active</span>
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
    <!-- Row -->
  </div>
</template>

<style lang="scss" scoped></style>
