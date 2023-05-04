<script setup lang="ts">
import { ref, onMounted, inject } from "vue";
let echarts = inject("ec"); //引入
const initEcharts = () => {
  // @ts-ignore
  if ($("#e_chart_1").length > 0) {
    // @ts-ignore
    var eChart_1 = echarts.init(document.getElementById("e_chart_1"));

    var data = [
      [
        ["A", "Jan", 17096869],
        ["B", "Feb", 27662440],
        ["C", "Mar", 1154605773],
        ["D", "Apr", 10582082],
        ["E", "May", 4986705],
        ["A", "Apr", 1709686669],
        ["B", "May", 276362440],
        ["C", "Mar", 1154605773],
        ["D", "Apr", 105882],
        ["E", "May", 49867205],
      ],
      //   [
      //     [48604, 77, 17096869, "Australia", 1990],
      //     [21163, 77.4, 27662440, "Canada", 1990],
      //     [1516, 68, 1154605773, "China", 1990],
      //     [13670, 74.7, 10582082, "Cuba", 1990],
      //     [28599, 75, 4986705, "Finland", 1990],
      //     [29476, 77.1, 56943299, "France", 1990],
      //     [31476, 75.4, 78958237, "Germany", 1990],
      //     [28666, 78.1, 254830, "Iceland", 1990],
      //     [1777, 57.7, 870601776, "India", 1990],
      //     [29550, 79.1, 122249285, "Japan", 1990],
      //     [2076, 67.9, 20194354, "North Korea", 1990],
      //     [12087, 72, 42972254, "South Korea", 1990],
      //     [24021, 75.4, 3397534, "New Zealand", 1990],
      //     [43296, 76.8, 4240375, "Norway", 1990],
      //     [10088, 70.8, 38195258, "Poland", 1990],
      //     [19349, 69.6, 147568552, "Russia", 1990],
      //     [10670, 67.3, 53994605, "Turkey", 1990],
      //     [26424, 75.7, 57110117, "United Kingdom", 1990],
      //     [37062, 75.4, 252847810, "United States", 1990],
      //   ],
      //   [
      //     [14056, 81.8, 23968973, "Australia", 2015],
      //     [53294, 81.7, 35939927, "Canada", 2015],
      //     [13334, 76.9, 1376048943, "China", 2015],
      //     [21291, 78.5, 11389562, "Cuba", 2015],
      //     [38923, 80.8, 5503457, "Finland", 2015],
      //     [37599, 81.9, 64395345, "France", 2015],
      //     [44053, 81.1, 80688545, "Germany", 2015],
      //     [42182, 82.8, 329425, "Iceland", 2015],
      //     [5903, 66.8, 1311050527, "India", 2015],
      //     [36162, 83.5, 126573481, "Japan", 2015],
      //     [1390, 71.4, 25155317, "North Korea", 2015],
      //     [34644, 80.7, 50293439, "South Korea", 2015],
      //     [34186, 80.6, 4528526, "New Zealand", 2015],
      //     [64304, 81.6, 5210967, "Norway", 2015],
      //     [24787, 77.3, 38611794, "Poland", 2015],
      //     [23038, 73.13, 143456918, "Russia", 2015],
      //     [19360, 76.5, 78665830, "Turkey", 2015],
      //     [38225, 81.4, 64715810, "United Kingdom", 2015],
      //     [53354, 79.1, 321773631, "United States", 2015],
      //   ],
    ];

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
        top: 30,
        bottom: 10,
        containLabel: true,
      },
      xAxis: {
        type: "category",
        data: ["A", "B", "C", "D", "E"],
        axisLine: {
          show: false,
        },
        axisLabel: {
          textStyle: {
            color: "#878787",
            fontFamily: "'Roboto', sans-serif",
            fontSize: 12,
          },
        },
        splitLine: {
          show: false,
        },
      },
      yAxis: {
        type: "category",
        data: ["Jan", "Feb", "Mar", "Apr", "May"],
        axisLine: {
          show: false,
        },
        axisLabel: {
          textStyle: {
            color: "#878787",
            fontFamily: "'Roboto', sans-serif",
            fontSize: 12,
          },
        },
        splitLine: {
          show: false,
        },
        scale: true,
      },
      series: [
        {
          name: "服务业",
          data: data[0],
          type: "scatter",
          symbolSize: function (data) {
            return Math.sqrt(data[2]) / 5e2;
          },
          label: {
            emphasis: {
              show: true,
              formatter: function (param) {
                return param.data[2];
              },
              position: "top",
            },
          },
          itemStyle: {
            normal: {
              shadowBlur: 5,
              shadowColor: "rgba(0, 0, 0, 0.5)",
              shadowOffsetY: 5,
              color: "#667add",
            },
          },
        },
        // {
        //   name: "2015",
        //   data: data[1],
        //   type: "scatter",
        //   symbolSize: function (data) {
        //     return Math.sqrt(data[2]) / 5e2;
        //   },
        //   label: {
        //     emphasis: {
        //       show: true,
        //       formatter: function (param) {
        //         return param.data[3];
        //       },
        //       position: "top",
        //     },
        //   },
        //   itemStyle: {
        //     normal: {
        //       shadowBlur: 5,
        //       shadowColor: "rgba(0, 0, 0, 0.5)",
        //       shadowOffsetY: 5,
        //       color: "#667add",
        //     },
        //   },
        // },
        {
          name: "line",
          type: "line",
          lineStyle: {
            normal: {
              color: "rgba(102,122,221, 0.1)",
              type: "dotted",
              shadowBlur: 5,
              shadowColor: "rgba(0, 0, 0, 0.1)",
              shadowOffsetY: 5,
            },
          },
          smooth: true,
          showSymbol: false,
          data: data[0],
          markPoint: {
            itemStyle: {
              normal: {
                color: "transparent",
              },
            },
          },
        },
      ],
    };
    eChart_1.setOption(option);
    eChart_1.resize();
  }
};
const industry = ref("");
const selected = () => {
  alert(industry.value);
};
onMounted(() => {
  initEcharts();
  // 下面是用于改变大小的
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
      echartResize = setTimeout(initEcharts, 200);
    })
    .resize();
  /*****Resize function end*****/
});
</script>
<!-- <script lang="ts">
// @ts-ignore
$(document).ready(function () {
  /*Fullscreen Init Js*/
  // @ts-ignore
  $(document).on("click", ".full-screen", function (e) {
    // @ts-ignore
    $(this).parents(".panel").toggleClass("fullscreen");
    // @ts-ignore
    $(window).trigger("resize");
    return false;
  });
});
</script> -->
<template>
  <div class="row row-center">
    <div class="col-lg-9 col-md-6 col-sm-12 col-xs-12">
      <div class="panel panel-default card-view">
        <div class="panel-heading">
          <div class="pull-left">
            <h6 class="panel-title txt-dark">Yearly Revenue</h6>
          </div>
          <div class="pull-right">
            <div class="pull-left form-group mb-0 sm-bootstrap-select mr-15">
              <select
                class="selectpicker"
                data-style="form-control"
                v-model="industry"
                @change="selected"
              >
                <option value="">请选择</option>
                <option value="1">Janaury</option>
                <option value="2">February</option>
                <option value="3">March</option>
                <option value="4">April</option>
                <option value="5">May</option>
                <option value="6">June</option>
                <option value="7">July</option>
                <option value="8">August</option>
                <option value="9">September</option>
                <option value="10">October</option>
                <option value="11">November</option>
                <option value="12">December</option>
              </select>
            </div>
            <a href="#" class="pull-left inline-block full-screen">
              <i class="zmdi zmdi-fullscreen"></i>
            </a>
          </div>
          <div class="clearfix"></div>
        </div>
        <div class="panel-wrapper collapse in">
          <div class="panel-body">
            <ul class="flex-stat mb-10 ml-15">
              <li class="text-left auto-width mr-60">
                <span class="block">Last Year</span>
                <span class="block txt-dark weight-500 font-18"
                  ><span class="counter-anim">3,24,222</span></span
                >
                <span class="block txt-success mt-5">
                  <i class="zmdi zmdi-caret-up pr-5 font-20"></i
                  ><span class="weight-500">+15%</span>
                </span>
                <div class="clearfix"></div>
              </li>
              <li class="text-left auto-width mr-60">
                <span class="block">This Year</span>
                <span class="block txt-dark weight-500 font-18"
                  ><span class="counter-anim">1,23,432</span></span
                >
                <span class="block txt-success mt-5">
                  <i class="zmdi zmdi-caret-up pr-5 font-20"></i
                  ><span class="weight-500">+4%</span>
                </span>
                <div class="clearfix"></div>
              </li>
              <li class="text-left auto-width">
                <span class="block">Revenue</span>
                <span class="block txt-dark weight-500 font-18"
                  >$<span class="counter-anim">324,222</span></span
                >
                <span class="block txt-danger mt-5">
                  <i class="zmdi zmdi-caret-down pr-5 font-20"></i
                  ><span class="weight-500">-5%</span>
                </span>
                <div class="clearfix"></div>
              </li>
            </ul>
            <div id="e_chart_1" class="" style="height: 324px"></div>
          </div>
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
  margin-top: 30px;
}

::v-deep .bootstrap-select .dropdown-toggle:focus {
  outline: none !important;
}
</style>
