<script setup lang="ts">
import { ref } from "vue";
</script>
<script lang="ts"></script>

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
