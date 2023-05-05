<script setup lang="ts">
import { ref, onMounted, inject } from "vue";
import { getLinePredictInfoApiProvince } from "@/apis/predict";
let echarts = inject("ec"); //引入
const provinceName = ref("");
let resultReal = [];
let resultPredict = [];
let dataX = [];
let realY = [];
let predictY = [];
const getLinePredictInfo = async () => {
  // @ts-ignore
  ElMessage({ type: "success", message: "开始计算，请耐心等待！" });
  await getLinePredictInfoApiProvince(provinceName.value)
    .then((res) => {
      // @ts-ignore
      ElMessage({ type: "success", message: "计算成功！" });

      resultReal = res.realGdp;
      resultReal.forEach((e) => {
        // @ts-ignore
        realY.push(e[1]);
      });
      resultPredict = res.predictGdp;
      resultPredict.forEach((e) => {
        dataX.push(e[0]);
        // @ts-ignore
        predictY.push(e[1].toFixed(2));
      });
      console.log(dataX);
      console.log(realY);
      console.log(predictY);
    })
    .catch((error) => {
      // @ts-ignore
      ElMessage({ type: "error", message: error.message });
    });
  initLine();
};
const initLine = () => {
  // @ts-ignore
  if ($("#e_chart_3").length > 0) {
    // @ts-ignore
    var eChart_3 = echarts.init(document.getElementById("e_chart_3"));
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
        data: dataX,
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
          interval: 0, // 显示所有标签
          rotate: 60, // 将标签旋转30度
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
        // boundaryGap: [0, "100%"],
      },
      series: [
        {
          name: "真实值",
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
          data: realY,
        },
        {
          name: "预测值",
          type: "line",
          smooth: true,
          symbol: "none",
          sampling: "average",
          itemStyle: {
            normal: {
              color: "#e8604c",
            },
          },
          areaStyle: {
            show: false,
          },
          data: predictY,
          // markLine: {
          //   label: {
          //     show: false, // 将标签设置为不显示
          //   },
          //   data: [
          //     {
          //       yAxis: 0, // 设置标线的位置
          //     },
          //   ],
          // },
        },
      ],
    };
    eChart_3.setOption(option3);
    eChart_3.resize();
  }
};
onMounted(() => {
  // getLinePredictInfo();
});
</script>

<template>
  <div class="row row-center">
    <div class="col-sm-10">
      <div class="panel panel-default card-view">
        <div class="panel-heading">
          <div class="pull-left">
            <h6 class="panel-title txt-dark">预测之后5年的gdp值</h6>
          </div>
          <div class="clearfix"></div>
        </div>
        <div class="panel-wrapper collapse in">
          <div class="panel-body">
            <div class="form-wrap">
              <form
                class="form-inline"
                autocomplete="off"
                @submit.prevent="getLinePredictInfo"
              >
                <div class="form-group mr-15">
                  <label class="control-label mr-10" for="email_inline"
                    >省份名称:（北京市）</label
                  >
                  <input
                    type="input"
                    class="form-control"
                    id="email_inline"
                    v-model="provinceName"
                  />
                </div>
                <!-- <div class="form-group mr-15">
                  <label class="control-label mr-10" for="pwd_inline"
                    >Password:</label
                  >
                  <input type="password" class="form-control" id="pwd_inline" />
                </div> -->
                <!-- <div class="checkbox mr-15">
                  <input id="checkbox_inline" type="checkbox" />
                  <label for="checkbox_inline"> remember me </label>
                </div> -->
                <button type="submit" class="btn btn-success btn-anim">
                  <i class="icon-rocket"></i><span class="btn-text">确定</span>
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="row row-center">
    <div class="col-lg-5 col-md-12 col-sm-12 col-xs-12">
      <div class="panel panel-default card-view panel-refresh relative">
        <div class="refresh-container">
          <div class="la-anim-1"></div>
        </div>
        <div class="panel-heading">
          <div class="pull-left">
            <h6 class="panel-title txt-dark">预测结果</h6>
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
                  >{{ provinceName }}GDP</span
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
