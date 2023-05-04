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
          period: "2010",
          iphone: 50,
          ipad: 80,
          itouch: 20,
        },
        {
          period: "2011",
          iphone: 130,
          ipad: 100,
          itouch: 80,
        },
        {
          period: "2012",
          iphone: 80,
          ipad: 60,
          itouch: 70,
        },
        {
          period: "2013",
          iphone: 70,
          ipad: 200,
          itouch: 140,
        },
        {
          period: "2014",
          iphone: 180,
          ipad: 150,
          itouch: 140,
        },
        {
          period: "2015",
          iphone: 105,
          ipad: 100,
          itouch: 80,
        },
        {
          period: "2016",
          iphone: 250,
          ipad: 150,
          itouch: 200,
        },
      ],
      xkey: "period",
      ykeys: ["iphone", "ipad", "itouch"],
      labels: ["iPhone", "iPad", "iPod Touch"],
      pointSize: 2,
      fillOpacity: 0,
      lineWidth: 2,
      pointStrokeColors: ["#4aa23c", "#f8b32d", "#f33923"],
      behaveLikeLine: true,
      grid: false,
      hideHover: "auto",
      lineColors: ["#4aa23c", "#f8b32d", "#f33923"],
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
          period: "2010",
          iphone: 50,
          ipad: 80,
          itouch: 20,
        },
        {
          period: "2011",
          iphone: 130,
          ipad: 100,
          itouch: 80,
        },
        {
          period: "2012",
          iphone: 80,
          ipad: 60,
          itouch: 70,
        },
        {
          period: "2013",
          iphone: 70,
          ipad: 200,
          itouch: 140,
        },
        {
          period: "2014",
          iphone: 180,
          ipad: 150,
          itouch: 140,
        },
        {
          period: "2015",
          iphone: 105,
          ipad: 100,
          itouch: 80,
        },
        {
          period: "2016",
          iphone: 250,
          ipad: 150,
          itouch: 200,
        },
      ],
      xkey: "period",
      ykeys: ["iphone", "ipad", "itouch"],
      labels: ["iPhone", "iPad", "iPod Touch"],
      pointSize: 2,
      fillOpacity: 0,
      lineWidth: 2,
      pointStrokeColors: ["#4aa23c", "#f8b32d", "#f33923"],
      behaveLikeLine: true,
      grid: false,
      hideHover: "auto",
      lineColors: ["#4aa23c", "#f8b32d", "#f33923"],
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
          period: "2010",
          iphone: 50,
          ipad: 80,
          itouch: 20,
        },
        {
          period: "2011",
          iphone: 130,
          ipad: 100,
          itouch: 80,
        },
        {
          period: "2012",
          iphone: 80,
          ipad: 60,
          itouch: 70,
        },
        {
          period: "2013",
          iphone: 70,
          ipad: 200,
          itouch: 140,
        },
        {
          period: "2014",
          iphone: 180,
          ipad: 150,
          itouch: 140,
        },
        {
          period: "2015",
          iphone: 105,
          ipad: 100,
          itouch: 80,
        },
        {
          period: "2016",
          iphone: 250,
          ipad: 150,
          itouch: 200,
        },
      ],
      xkey: "period",
      ykeys: ["iphone", "ipad", "itouch"],
      labels: ["iPhone", "iPad", "iPod Touch"],
      pointSize: 2,
      fillOpacity: 0,
      lineWidth: 2,
      pointStrokeColors: ["#4aa23c", "#f8b32d", "#f33923"],
      behaveLikeLine: true,
      grid: false,
      hideHover: "auto",
      lineColors: ["#4aa23c", "#f8b32d", "#f33923"],
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
