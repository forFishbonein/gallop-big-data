<script setup lang="ts">
import { ref, reactive, defineExpose, onMounted } from "vue";
import { useRouter } from "vue-router";
const testEcharts = () => {
  if ($("#e_chart_1").length > 0) {
    // alert(111)
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
  if ($("#e_chart_2").length > 0) {
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
  if ($("#e_chart_3").length > 0) {
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
onMounted(() => {});
</script>
<template><h1>这是首页</h1></template>

<style lang="scss" scoped></style>
