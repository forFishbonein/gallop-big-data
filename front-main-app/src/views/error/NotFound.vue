<script setup lang="ts"></script>

<template>
  <div>
    <!--Preloader-->
    <!-- <div class="preloader-it">
      <div class="la-anim-1"></div>
    </div> -->
    <!--/Preloader-->

    <div class="wrapper error-page pa-0">
      <header class="sp-header">
        <div class="sp-logo-wrap pull-left">
          <a href="index.html">
            <img class="brand-img mr-10" src="/picture/logo.png" alt="brand" />
            <span class="brand-text">Elmer</span>
          </a>
        </div>
        <div class="form-group mb-0 pull-right">
          <a
            class="inline-block btn btn-primary btn-rounded btn-outline nonecase-font"
            href="index.html"
            >Back to Home</a
          >
        </div>
        <div class="clearfix"></div>
      </header>

      <!-- Main Content -->
      <div class="page-wrapper pa-0 ma-0 error-bg-img">
        <div class="container-fluid">
          <!-- Row -->
          <div class="table-struct full-width full-height">
            <div class="table-cell vertical-align-middle auth-form-wrap">
              <div class="auth-form ml-auto mr-auto no-float">
                <div class="row">
                  <div class="col-sm-12 col-xs-12">
                    <div class="mb-30">
                      <span
                        class="block error-head text-center txt-primary mb-10"
                        >404</span
                      >
                      <span
                        class="text-center nonecase-font mb-20 block error-comment"
                        >Page Not Found</span
                      >
                      <p class="text-center">
                        The URL may be misplaced or the pahe you are looking is
                        no longer available.
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Row -->
        </div>
      </div>
      <!-- /Main Content -->
    </div>
    <!-- /#wrapper -->
  </div>
</template>

<style lang="scss" scoped></style>
