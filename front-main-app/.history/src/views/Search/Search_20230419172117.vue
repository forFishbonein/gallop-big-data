<script setup lang="ts"></script>
<script lang="ts">
$("#treeview1").treeview({
  data: defaultData,
});
</script>

<template>
  <div class="container-fluid pt-25">
    <!-- Row -->
    <div class="row">
      <!-- <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12"> -->
      <div class="col-sm-4">
        <div class="panel panel-default card-view">
          <div class="panel-heading">
            <div class="pull-left">
              <h6 class="panel-title txt-dark">Default</h6>
            </div>
            <div class="clearfix"></div>
          </div>
          <div class="panel-wrapper collapse in">
            <div class="panel-body">
              <div class="treeview" id="treeview1"></div>
            </div>
          </div>
        </div>
        <!-- </div> -->
      </div>
    </div>
    <!-- /Row -->
  </div>
</template>
<style lang="scss" scoped>
.font-color {
  color: $theme-color;
}
</style>
