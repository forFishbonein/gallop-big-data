<script setup lang="ts"></script>

<template>
  <div>
    <!--Preloader-->
    <!-- <div class="preloader-it">
      <div class="la-anim-1"></div>
    </div> -->
    <!--/Preloader-->

    <div class="wrapper pa-0">
      <header class="sp-header">
        <div class="sp-logo-wrap pull-left">
          <router-link to="/home">
            <img class="brand-img mr-10" src="/picture/logo.png" alt="brand" />
            <span class="brand-text">飞驰大数据</span>
          </router-link>
        </div>
        <div class="form-group mb-0 pull-right">
          <span class="inline-block pr-10">已经有账号了?</span>
          <router-link
            to="/login"
            class="inline-block btn btn-primary btn-rounded btn-outline"
            >登录</router-link
          >
        </div>
        <div class="clearfix"></div>
      </header>

      <!-- Main Content -->
      <div class="page-wrapper pa-0 ma-0 auth-page">
        <div class="container-fluid">
          <!-- Row -->
          <div class="table-struct full-width full-height">
            <div class="table-cell vertical-align-middle auth-form-wrap">
              <div class="auth-form ml-auto mr-auto no-float">
                <div class="row">
                  <div class="col-sm-12 col-xs-12">
                    <div class="mb-30">
                      <h3 class="text-center txt-dark mb-10">注册飞驰账号</h3>
                      <h6 class="text-center nonecase-font txt-grey">
                        请在下面填写你的信息
                      </h6>
                    </div>
                    <div class="form-wrap">
                      <form action="#">
                        <div class="form-group">
                          <label
                            class="control-label mb-10"
                            for="exampleInputName_1"
                            >用户名</label
                          >
                          <input
                            type="email"
                            class="form-control"
                            required
                            id="exampleInputName_1"
                            placeholder="输入用户名"
                          />
                        </div>
                        <div class="form-group">
                          <label
                            class="control-label mb-10"
                            for="exampleInputEmail_2"
                            >邮箱地址</label
                          >
                          <input
                            type="email"
                            class="form-control"
                            required
                            id="exampleInputEmail_2"
                            placeholder="输入邮箱地址"
                          />
                        </div>
                        <div class="form-group">
                          <label
                            class="pull-left control-label mb-10"
                            for="exampleInputpwd_2"
                            >密码</label
                          >
                          <input
                            type="password"
                            class="form-control"
                            required
                            id="exampleInputpwd_2"
                            placeholder="Enter pwd"
                          />
                        </div>
                        <div class="form-group">
                          <label
                            class="pull-left control-label mb-10"
                            for="exampleInputpwd_3"
                            >确认密码</label
                          >
                          <input
                            type="password"
                            class="form-control"
                            required
                            id="exampleInputpwd_3"
                            placeholder="Enter pwd"
                          />
                        </div>
                        <div class="form-group">
                          <div
                            class="checkbox checkbox-primary pr-10 pull-left"
                          >
                            <input id="checkbox_2" required type="checkbox" />
                            <label for="checkbox_2">
                              我接受全部
                              <span class="txt-primary">协议</span></label
                            >
                          </div>
                          <div class="clearfix"></div>
                        </div>
                        <div class="form-group text-center">
                          <button
                            type="submit"
                            class="btn btn-primary btn-rounded"
                          >
                            注册
                          </button>
                        </div>
                      </form>
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
