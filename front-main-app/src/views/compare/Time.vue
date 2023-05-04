<script setup lang="ts">
import { onMounted } from "vue";
const initCharts = () => {
  // @ts-ignore
  if ($("#morris_extra_line_chart").length > 0)
    // @ts-ignore
    Morris.Line({
      element: "morris_extra_line_chart",
      data: [
        {
          period: "2000",
          easterngdp: 42910,
          // ipad: 80,
          // itouch: 20,
        },
        {
          period: "2001",
          easterngdp: 47497,
          // ipad: 100,
          // itouch: 80,
        },
        {
          period: "2002",
          easterngdp: 53231,
          // ipad: 60,
          // itouch: 70,
        },
        {
          period: "2003",
          easterngdp: 61597,
          // ipad: 200,
          // itouch: 140,
        },
        {
          period: "2004",
          easterngdp: 72888,
          // ipad: 150,
          // itouch: 140,
        },
        {
          period: "2005",
          easterngdp: 85557,
          // ipad: 100,
          // itouch: 80,
        },
        {
          period: "2006",
          easterngdp: 100567,
          // ipad: 150,
          // itouch: 200,
        },
         {
          period: "2007",
          easterngdp: 122527,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2008",
          easterngdp: 142983,
          ipad: 150,
          itouch: 200,
        },
         {
          period: "2009",
          easterngdp: 156091,
          ipad: 150,
          itouch: 200,
        },
        {
          period: "2010",
          easterngdp: 183589,
          // ipad: 80,
          // itouch: 20,
        },
        {
          period: "2011",
          easterngdp: 213223,
          // ipad: 100,
          // itouch: 80,
        },
        {
          period: "2012",
          easterngdp: 232335,
          // ipad: 60,
          // itouch: 232335,
        },
        {
          period: "2013",
          easterngdp: 255355,
          // ipad: 200,
          // itouch: 140,
        },
        {
          period: "2014",
          easterngdp: 277462,
          // ipad: 150,
          // itouch: 140,
        },
        {
          period: "2015",
          easterngdp: 302225,
          // ipad: 100,
          // itouch: 80,
        },
        {
          period: "2016",
          easterngdp: 329117,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2017",
          easterngdp: 364198,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2018",
          easterngdp: 397414,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2019",
          easterngdp: 425291,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2020",
          easterngdp: 439359,
          // ipad: 150,
          // itouch: 200,
        },
      ],
      xkey: "period",
      ykeys: ["easterngdp"],
      labels: ["easterngdp"],
      pointSize: 2,
      fillOpacity: 0,
      lineWidth: 2,
      pointStrokeColors: ["#4aa23c"],
      behaveLikeLine: true,
      grid: false,
      hideHover: "auto",
      lineColors: ["#4aa23c"],
      resize: true,
      gridTextColor: "#878787",
      gridTextFamily: "Roboto",
    });
  // @ts-ignore
  if ($("#morris_extra_line_chart2").length > 0)
    // @ts-ignore
    Morris.Line({
      element: "morris_extra_line_chart2",
      data: [
        {
          period: "2000",
          centralgdp: 17278,
          // ipad: 80,
          // itouch: 20,
        },
        {
          period: "2001",
          centralgdp: 18923,
          // ipad: 100,
          // itouch: 80,
        },
        {
          period: "2002",
          centralgdp: 20678,
          // ipad: 60,
          // itouch: 70,
        },
        {
          period: "2003",
          centralgdp: 23480,
          // ipad: 200,
          // itouch: 140,
        },
        {
          period: "2004",
          centralgdp: 28027,
          // ipad: 150,
          // itouch: 140,
        },
        {
          period: "2005",
          centralgdp: 32700,
          // ipad: 100,
          // itouch: 80,
        },
        {
          period: "2006",
          centralgdp: 38138,
          // ipad: 150,
          // itouch: 200,
        },
         {
          period: "2007",
          centralgdp: 47280,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2008",
          centralgdp: 56992,
          // ipad: 150,
          // itouch: 200,
        },
         {
          period: "2009",
          centralgdp: 63640,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2010",
          centralgdp: 77089,
          // ipad: 80,
          // itouch: 20,
        },
        {
          period: "2011",
          centralgdp: 93045,
          // ipad: 100,
          // itouch: 80,
        },
        {
          period: "2012",
          centralgdp: 103909,
          // ipad: 60,
          // itouch: 232335,
        },
        {
          period: "2013",
          centralgdp: 115439,
          // ipad: 200,
          // itouch: 140,
        },
        {
          period: "2014",
          centralgdp: 126885,
          // ipad: 150,
          // itouch: 140,
        },
        {
          period: "2015",
          centralgdp: 136578,
          // ipad: 100,
          // itouch: 80,
        },
        {
          period: "2016",
          centralgdp: 149152,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2017",
          centralgdp: 165775,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2018",
          centralgdp: 185015,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2019",
          centralgdp: 200553,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2020",
          centralgdp: 204594,
          // ipad: 150,
          // itouch: 200,
        },
      ],
      xkey: "period",
      ykeys: ["centralgdp"],
      labels: ["centralgdp"],
      pointSize: 2,
      fillOpacity: 0,
      lineWidth: 2,
      pointStrokeColors: [ "#f8b32d"],
      behaveLikeLine: true,
      grid: false,
      hideHover: "auto",
      lineColors: ["#f8b32d"],
      resize: true,
      gridTextColor: "#878787",
      gridTextFamily: "Roboto",
    });
  // @ts-ignore
  if ($("#morris_extra_line_chart3").length > 0)
    // @ts-ignore
    Morris.Line({
      element: "morris_extra_line_chart3",
      data: [
        {
          period: "2000",
          westerngdp: 13707,
          // ipad: 80,
          // itouch: 20,
        },
        {
          period: "2001",
          westerngdp: 15004,
          // ipad: 100,
          // itouch: 80,
        },
        {
          period: "2002",
          westerngdp: 16584,
          // ipad: 60,
          // itouch: 70,
        },
        {
          period: "2003",
          westerngdp: 18914,
          // ipad: 200,
          // itouch: 140,
        },
        {
          period: "2004",
          westerngdp: 22296,
          // ipad: 150,
          // itouch: 140,
        },
        {
          period: "2005",
          westerngdp: 25606,
          // ipad: 100,
          // itouch: 80,
        },
        {
          period: "2006",
          westerngdp: 30060,
          // ipad: 150,
          // itouch: 200,
        },
         {
          period: "2007",
          westerngdp: 37056,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2008",
          westerngdp: 45003,
          // ipad: 150,
          // itouch: 200,
        },
         {
          period: "2009",
          westerngdp: 49428,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2010",
          westerngdp: 59922,
          // ipad: 80,
          // itouch: 20,
        },
        {
          period: "2011",
          westerngdp: 73788,
          // ipad: 100,
          // itouch: 80,
        },
        {
          period: "2012",
          westerngdp: 84674,
          // ipad: 60,
          // itouch: 232335,
        },
        {
          period: "2013",
          westerngdp: 95525,
          // ipad: 200,
          // itouch: 140,
        },
        {
          period: "2014",
          westerngdp: 105176,
          // ipad: 150,
          // itouch: 140,
        },
        {
          period: "2015",
          westerngdp: 111279,
          // ipad: 100,
          // itouch: 80,
        },
        {
          period: "2016",
          westerngdp: 121119,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2017",
          westerngdp: 137047,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2018",
          westerngdp: 153386,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2019",
          westerngdp: 166458,
          // ipad: 150,
          // itouch: 200,
        },
        {
          period: "2020",
          westerngdp: 173775,
          // ipad: 150,
          // itouch: 200,
        },
      ],
      xkey: "period",
      ykeys: ["westerngdp"],
      labels: ["westerngdp"],
      pointSize: 2,
      fillOpacity: 0,
      lineWidth: 2,
      pointStrokeColors: ["#f33923"],
      behaveLikeLine: true,
      grid: false,
      hideHover: "auto",
      lineColors: [ "#f33923"],
      resize: true,
      gridTextColor: "#878787",
      gridTextFamily: "Roboto",
    });
};
onMounted(() => {
  initCharts();
});
</script>

<template>
  <div class="row row-center">
    <div class="col-lg-6">
      <div class="panel panel-default card-view">
        <div class="panel-heading">
          <div class="pull-left">
            <h6 class="panel-title txt-dark">line Chart</h6>
          </div>
          <div class="clearfix"></div>
        </div>
        <div class="panel-wrapper collapse in">
          <div id="morris_extra_line_chart" class="morris-chart"></div>
        </div>
      </div>
    </div>
    <div class="col-lg-6">
      <div class="panel panel-default card-view">
        <div class="panel-heading">
          <div class="pull-left">
            <h6 class="panel-title txt-dark">line Chart</h6>
          </div>
          <div class="clearfix"></div>
        </div>
        <div class="panel-wrapper collapse in">
          <div id="morris_extra_line_chart2" class="morris-chart"></div>
        </div>
      </div>
    </div>
    <div class="col-lg-6">
      <div class="panel panel-default card-view">
        <div class="panel-heading">
          <div class="pull-left">
            <h6 class="panel-title txt-dark">line Chart</h6>
          </div>
          <div class="clearfix"></div>
        </div>
        <div class="panel-wrapper collapse in">
          <div id="morris_extra_line_chart3" class="morris-chart"></div>
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
