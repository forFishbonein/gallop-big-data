<script setup lang="ts">
import { ref, onMounted, inject } from "vue";
let echarts = inject("ec"); //引入
const initEcharts = () => {
  // @ts-ignore
  if ($("#e_chart_3").length > 0) {
    // @ts-ignore
    var eChart_3 = echarts.init(document.getElementById("e_chart_3"));
    var base = +new Date(1968, 9, 3);
    var oneDay = 24 * 3600 * 1000;
    var date = [];

    var data = [Math.random() * 300];

    for (var i = 1; i < 5000; i++) {
      var now = new Date((base += oneDay));
      date.push(
        // @ts-ignore
        [now.getFullYear(), now.getMonth() + 1, now.getDate()].join("/")
      );
      data.push(Math.round((Math.random() - 0.5) * 40 + data[i - 1]));
    }
    var option3 = {
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
      toolbox: {
        show: false,
      },
      xAxis: {
        type: "category",
        boundaryGap: false,
        data: date,
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
      },
      yAxis: {
        type: "value",
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
        splitLine: {
          show: false,
        },
        boundaryGap: [0, "100%"],
      },
      series: [
        {
          name: "Educattion",
          type: "line",
          smooth: true,
          symbol: "none",
          sampling: "average",
          itemStyle: {
            normal: {
              color: "#667add",
            },
          },
          areaStyle: {
            show: false,
          },
          data: data,
        },
      ],
    };
    eChart_3.setOption(option3);
    eChart_3.resize();
  }
};
onMounted(() => {
  initEcharts();
});
</script>

<template>
  <div class="row row-center">
    <div class="col-lg-5 col-md-12 col-sm-12 col-xs-12">
      <div class="panel panel-default card-view panel-refresh relative">
        <div class="refresh-container">
          <div class="la-anim-1"></div>
        </div>
        <div class="panel-heading">
          <div class="pull-left">
            <h6 class="panel-title txt-dark">Education Growth</h6>
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
              <ul class="dropdown-menu bullet dropdown-menu-right" role="menu">
                <li role="presentation">
                  <a href="javascript:void(0)" role="menuitem"
                    ><i class="icon wb-reply" aria-hidden="true"></i>option 1</a
                  >
                </li>
                <li role="presentation">
                  <a href="javascript:void(0)" role="menuitem"
                    ><i class="icon wb-share" aria-hidden="true"></i>option 2</a
                  >
                </li>
                <li role="presentation">
                  <a href="javascript:void(0)" role="menuitem"
                    ><i class="icon wb-trash" aria-hidden="true"></i>option 3</a
                  >
                </li>
              </ul>
            </div>
          </div>
          <div class="clearfix"></div>
        </div>
        <div class="panel-wrapper collapse in">
          <div class="panel-body">
            <div id="e_chart_3" class="" style="height: 348px"></div>
            <div class="label-chatrs">
              <div class="inline-block mr-15">
                <span class="clabels inline-block bg-primary mr-5"></span>
                <span
                  class="clabels-text font-12 inline-block txt-dark capitalize-font"
                  >Higher education</span
                >
              </div>
            </div>
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
</style>
