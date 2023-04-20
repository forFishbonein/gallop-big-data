<script setup lang="ts">
import { ref } from "vue";
</script>
<script lang="ts">
$(function () {
  if ($("#world_map_marker_1").length > 0) {
    $("#world_map_marker_1").vectorMap({
      map: "world_mill_en",
      backgroundColor: "transparent",
      borderColor: "#fff",
      borderOpacity: 0.25,
      borderWidth: 0,
      color: "#e6e6e6",
      regionStyle: {
        initial: {
          fill: "#f4f4f4",
        },
      },

      markerStyle: {
        initial: {
          r: 10,
          fill: "#fff",
          "fill-opacity": 1,
          stroke: "#000",
          "stroke-width": 1,
          "stroke-opacity": 0.4,
        },
      },

      markers: [
        {
          latLng: [21.0, 78.0],
          name: "INDIA : 350",
        },
        {
          latLng: [-33.0, 151.0],
          name: "Australia : 250",
        },
        {
          latLng: [36.77, -119.41],
          name: "USA : 250",
        },
        {
          latLng: [55.37, -3.41],
          name: "UK   : 250",
        },
        {
          latLng: [25.2, 55.27],
          name: "UAE : 250",
        },
      ],

      series: {
        regions: [
          {
            values: {
              US: "#667add",
              SA: "#667add",
              AU: "#667add",
              IN: "#667add",
              GB: "#667add",
            },
            attribute: "fill",
          },
        ],
      },
      hoverOpacity: null,
      normalizeFunction: "linear",
      zoomOnScroll: false,
      scaleColors: ["#000000", "#000000"],
      selectedColor: "#000000",
      selectedRegions: [],
      enableZoom: false,
      hoverColor: "#fff",
    });
  }
});
</script>

<template>
  <div class="container-fluid pt-25">
    <div class="row">
      <div class="col-lg-6">
        <div class="panel panel-default card-view">
          <div class="panel-heading">
            <div class="pull-left">
              <h6 class="panel-title txt-dark">world map</h6>
            </div>
            <div class="clearfix"></div>
          </div>
          <div class="panel-wrapper collapse in">
            <div class="panel-body">
              <div id="world_map_marker_1" style="height: 400px"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped></style>
