<script setup lang="ts">
import { onMounted } from "vue";
import { useRouter } from "vue-router";
const router = useRouter();
onMounted(() => {
  // @ts-ignore
  $(function () {
    var defaultData = [
      {
        text: "第一产业",
        nodes: [
          {
            text: "农业",
            nodes: [
              {
                text: "农业机械总动力",
                href: "#search/result/农业机械总动力",
                tags: ["0"],
              },
              {
                text: "农作物受灾面积",
                href: "#search/result/农作物受灾面积",
                tags: ["0"],
              },
              {
                text: "粮食产量",
                href: "#search/result/粮食产量",
                tags: ["0"],
              },
              {
                text: "粮食单位面积产量",
                href: "#search/result/粮食单位面积产量",
                tags: ["0"],
              },
              {
                text: "农作物总播种面积",
                href: "#search/result/农作物总播种面积",
                tags: ["0"],
              },
              {
                text: "农用大中型拖拉机数量",
                href: "#search/result/农用大中型拖拉机数量",
                tags: ["0"],
              },
              {
                text: "香蕉园面积",
                href: "#search/result/香蕉园面积",
                tags: ["0"],
              },
              {
                text: "苹果园面积",
                href: "#search/result/苹果园面积",
                tags: ["0"],
              },
              {
                text: "柑桔园面积",
                href: "#search/result/柑桔园面积",
                tags: ["0"],
              },
              {
                text: "梨园面积",
                href: "#search/result/梨园面积",
                tags: ["0"],
              },
              {
                text: "葡萄园面积",
                href: "#search/result/葡萄园面积",
                tags: ["0"],
              },
            ],
          },
          {
            text: "林业",
            nodes: [
              {
                text: "林业用地面积",
                href: "#search/result/林业用地面积",
                tags: ["0"],
              },
              {
                text: "人工林面积",
                href: "#search/result/人工林面积",
                tags: ["0"],
              },
              {
                text: "林业投资本年资金来源",
                href: "#search/result/林业投资本年资金来源",
                tags: ["0"],
              },
              {
                text: "林业投资国家预算资金",
                href: "#search/result/林业投资国家预算资金",
                tags: ["0"],
              },
              {
                text: "林业投资自筹资金",
                href: "#search/result/林业投资自筹资金",
                tags: ["0"],
              },
              {
                text: "林业投资",
                href: "#search/result/林业投资",
                tags: ["0"],
              },
              {
                text: "生态建设与保护本年完成投资",
                href: "#search/result/生态建设与保护本年完成投资",
                tags: ["0"],
              },
              {
                text: "林业支撑与保障本年完成投资",
                href: "#search/result/林业支撑与保障本年完成投资",
                tags: ["0"],
              },
              {
                text: "林业投资债券",
                href: "#search/result/林业投资债券",
                tags: ["0"],
              },
              {
                text: "林业投资利用外资",
                href: "#search/result/林业投资利用外资",
                tags: ["0"],
              },
              {
                text: "林业投资其它资金",
                href: "#search/result/林业投资其它资金",
                tags: ["0"],
              },
              {
                text: "林业投资国内贷款",
                href: "#search/result/林业投资国内贷款",
                tags: ["0"],
              }
            ]
          },
          {
            text: "畜牧业",
            nodes: [
              {
                text: "可利用草原面积",
                href: "#search/result/可利用草原面积",
                tags: ["0"],
              },
              {
                text: "当年新增种草面积",
                href: "#search/result/当年新增种草面积",
                tags: ["0"],
              },
              {
                text: "大牲畜年底头数",
                href: "#search/result/大牲畜年底头数",
                tags: ["0"],
              },
              {
                text: "牛期末数量",
                href: "#search/result/牛期末数量",
                tags: ["0"],
              },
              {
                text: "马期末数量",
                href: "#search/result/马期末数量",
                tags: ["0"],
              },
              {
                text: "驴期末数量",
                href: "#search/result/驴期末数量",
                tags: ["0"],
              },
              {
                text: "骆驼期末数量",
                href: "#search/result/骆驼期末数量",
                tags: ["0"],
              },
              {
                text: "家禽出栏量",
                href: "#search/result/家禽出栏量",
                tags: ["0"],
              },
              {
                text: "羊年底只数",
                href: "#search/result/羊年底只数",
                tags: ["0"],
              },
              {
                text: "绵羊毛产量",
                href: "#search/result/绵羊毛产量",
                tags: ["0"],
              },
              {
                text: "禽蛋产量",
                href: "#search/result/禽蛋产量",
                tags: ["0"],
              },
              {
                text: "蜂蜜产量",
                href: "#search/result/蜂蜜产量",
                tags: ["0"],
              },
              {
                text: "绵羊毛产量",
                href: "#search/result/绵羊毛产量",
                tags: ["0"],
              },
              {
                text: "牛奶产量",
                href: "#search/result/牛奶产量",
                tags: ["0"],
              },
            ]
          },
          {
            text: "渔业",
            nodes: [
              {
                text: "水产品总产量",
                href: "#search/result/水产品总产量",
                tags: ["0"],
              },
              {
                text: "海水产品产量",
                href: "#search/result/海水产品产量",
                tags: ["0"],
              },
              {
                text: "海洋捕捞产量",
                href: "#search/result/海洋捕捞产量",
                tags: ["0"],
              },
              {
                text: "海水养殖产量",
                href: "#search/result/海水养殖产量",
                tags: ["0"],
              },
             {
                text: "虾蟹类产量",
                href: "#search/result/虾蟹类产量",
                tags: ["0"],
              },
              {
                text: "贝类产量",
                href: "#search/result/贝类产量",
                tags: ["0"],
              },
              {
                text: "藻类产量",
                href: "#search/result/藻类产量",
                tags: ["0"],
              },
              {
                text: "天然生产海水产品产量",
                href: "#search/result/天然生产海水产品产量",
                tags: ["0"],
              },
              {
                text: "人工养殖海水产品产量",
                href: "#search/result/人工养殖海水产品产量",
                tags: ["0"],
              },
              {
                text: "鱼类海水产品产量",
                href: "#search/result/鱼类海水产品产量",
                tags: ["0"],
              },
              {
                text: "淡水捕捞产量",
                href: "#search/result/淡水捕捞产量",
                tags: ["0"],
              },
              {
                text: "鱼类淡水产品产量",
                href: "#search/result/鱼类淡水产品产量",
                tags: ["0"],
              },
              {
                text: "水产品养殖面积",
                href: "#search/result/水产品养殖面积",
                tags: ["0"],
              },
              {
                text: "内陆养殖面积",
                href: "#search/result/内陆养殖面积",
                tags: ["0"],
              },
              {
                text: "海水养殖面积",
                href: "#search/result/海水养殖面积",
                tags: ["0"],
              },
              {
                text: "浅海养殖面积",
                href: "#search/result/浅海养殖面积",
                tags: ["0"],
              },
            ]
          },
        ],
      },
      {
        text: "第二产业",
        nodes: [
          {
            text: "工业",
            nodes: [
              {
                text: "规模以上工业企业单位数",
                href: "#search/result/规模以上工业企业单位数",
                tags: ["0"],
              },
              {
                text: "规模以上工业企业亏损企业单位数",
                href: "#search/result/规模以上工业企业亏损企业单位数",
                tags: ["0"],
              },
              {
                text: "规模以上工业企业实收资本",
                href: "#search/result/规模以上工业企业实收资本",
                tags: ["0"],
              },
              {
                text: "规模以上工业企业应收账款净额",
                href: "#search/result/规模以上工业企业应收账款净额",
                tags: ["0"],
              },
             {
                text: "规模以上工业企业外商资本金",
                href: "#search/result/规模以上工业企业外商资本金",
                tags: ["0"],
              },
              {
                text: "规模以上工业企业销售费用",
                href: "#search/result/规模以上工业企业销售费用",
                tags: ["0"],
              },
              {
                text: "规模以上工业企业营业利润",
                href: "#search/result/规模以上工业企业营业利润",
                tags: ["0"],
              },
              {
                text: "国有控股工业企业单位数",
                href: "#search/result/国有控股工业企业单位数",
                tags: ["0"],
              },
              {
                text: "国有控股工业企业国家资本金",
                href: "#search/result/国有控股工业企业国家资本金",
                tags: ["0"],
              },
              {
                text: "国有控股工业企业产成品",
                href: "#search/result/国有控股工业企业产成品",
                tags: ["0"],
              },
              {
                text: "国有控股工业企业销售费用",
                href: "#search/result/国有控股工业企业销售费用",
                tags: ["0"],
              },
              {
                text: "国有控股工业企业营业利润",
                href: "#search/result/国有控股工业企业营业利润",
                tags: ["0"],
              },
              {
                text: "国有控股工业企业利润总额",
                href: "#search/result/国有控股工业企业利润总额",
                tags: ["0"],
              },
              {
                text: "国有控股工业企业出口交货值",
                href: "#search/result/国有控股工业企业出口交货值",
                tags: ["0"],
              },
              {
                text: "私营工业企业单位数",
                href: "#search/result/私营工业企业单位数",
                tags: ["0"],
              },
              {
                text: "私营工业企业实收资本",
                href: "#search/result/私营工业企业实收资本",
                tags: ["0"],
              },
              {
                text: "私营工业企业管理费用",
                href: "#search/result/私营工业企业管理费用",
                tags: ["0"],
              },
              {
                text: "私营工业企业出口交货值",
                href: "#search/result/私营工业企业出口交货值",
                tags: ["0"],
              },
              {
                text: "外商及港澳台商投资工业企业单位数",
                href: "#search/result/外商及港澳台商投资工业企业单位数",
                tags: ["0"],
              },
              {
                text: "外商及港澳台商投资工业企业外商资本金",
                href: "#search/result/外商及港澳台商投资工业企业外商资本金",
                tags: ["0"],
              },
              {
                text: "外商及港澳台商投资工业企业产成品",
                href: "#search/result/外商及港澳台商投资工业企业产成品",
                tags: ["0"],
              },
              {
                text: "外商及港澳台商投资工业企业销售费用",
                href: "#search/result/外商及港澳台商投资工业企业销售费用",
                tags: ["0"],
              },
              {
                text: "外商及港澳台商投资工业企业出口交货值",
                href: "#search/result/外商及港澳台商投资工业企业出口交货值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "采矿业",
            nodes: [
              {
                text: "国有经济能源工业固定资产投资",
                href: "#search/result/国有经济能源工业固定资产投资",
                tags: ["0"],
              },
              {
                text: "国有经济煤炭采选业固定资产投资",
                href: "#search/result/国有经济煤炭采选业固定资产投资",
                tags: ["0"],
              },
              {
                text: "国有经济石油和天然气开采业固定资产投资",
                href: "#search/result/国有经济石油和天然气开采业固定资产投资",
                tags: ["0"],
              },
              {
                text: "国有经济石油加工及炼焦业固定资产投资",
                href: "#search/result/国有经济石油加工及炼焦业固定资产投资",
                tags: ["0"],
              },
             {
                text: "能源工业投资",
                href: "#search/result/能源工业投资",
                tags: ["0"],
              },
              {
                text: "煤炭采选业投资",
                href: "#search/result/煤炭采选业投资",
                tags: ["0"],
              },
              {
                text: "石油和天然气开采业投资",
                href: "#search/result/石油和天然气开采业投资",
                tags: ["0"],
              },
              {
                text: "石油加工及炼焦业投资",
                href: "#search/result/石油加工及炼焦业投资",
                tags: ["0"],
              },
              {
                text: "焦炭生产量",
                href: "#search/result/焦炭生产量",
                tags: ["0"],
              },
              {
                text: "原油生产量",
                href: "#search/result/原油生产量",
                tags: ["0"],
              },
              {
                text: "汽油生产量",
                href: "#search/result/汽油生产量",
                tags: ["0"],
              },
              {
                text: "煤油生产量",
                href: "#search/result/煤油生产量",
                tags: ["0"],
              },
              {
                text: "柴油生产量",
                href: "#search/result/柴油生产量",
                tags: ["0"],
              },
              {
                text: "燃料油生产量",
                href: "#search/result/燃料油生产量",
                tags: ["0"],
              },
              {
                text: "天然气生产量",
                href: "#search/result/天然气生产量",
                tags: ["0"],
              },
              {
                text: "水力发电量",
                href: "#search/result/水力发电量",
                tags: ["0"],
              },
              {
                text: "火力发电量",
                href: "#search/result/火力发电量",
                tags: ["0"],
              },
              {
                text: "煤炭消费量",
                href: "#search/result/煤炭消费量",
                tags: ["0"],
              },
              {
                text: "焦炭消费量",
                href: "#search/result/焦炭消费量",
                tags: ["0"],
              },
              {
                text: "原油消费量",
                href: "#search/result/原油消费量",
                tags: ["0"],
              },
              {
                text: "汽油消费量",
                href: "#search/result/汽油消费量",
                tags: ["0"],
              },
              {
                text: "煤油消费量",
                href: "#search/result/煤油消费量",
                tags: ["0"],
              },
              {
                text: "燃料油消费量",
                href: "#search/result/燃料油消费量",
                tags: ["0"],
              },
            ]
          },
          {
            text: "制造业",
            nodes: [
              {
                text: "出入境货物检验检疫批次",
                href: "#arch/result/出入境货物检验检疫批次",
                tags: ["0"],
              },
              {
                text: "数码激光视盘出版出版种数",
                href: "#arch/result/数码激光视盘出版出版种数",
                tags: ["0"],
              },
            ],
          },
          {
            text: "建筑业",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
        ],
      },
      {
        text: "第三产业",
        nodes: [
          {
            text: "批发和零售业",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "交通运输、仓储和邮政业",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "住宿和餐饮业",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "金融服务业",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "租赁和商贸服务业",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "社会公共服务",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "文化、体育、娱乐业",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "信息传输、软件和信息技术服务业",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "卫生公共服务",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "科研研究与技术服务业",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "教育服务业",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "旅游业",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "房地产",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
        ],
      },
      {
        text: "国民经济核算指标",
        nodes: [
          {
            text: "人口就业与产业结构",
            nodes: [
              {
                text: "人口就业与产业结构",
                href: "#arch/result/111",
                tags: ["0"],
              },
              {
                text: "Grandchild 2",
                href: "#grandchild2",
                tags: ["0"],
              },
            ],
          },
          {
            text: "专利类",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "创新类",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "金融服务业",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "产业类",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "居民消费类",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "人口统计指标类",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "投资与财证类",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "城市",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "农村",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "自然资源",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "环境",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
        ],
      },
      {
        text: "政府和社会公共服务",
        nodes: [
          {
            text: "社会管理领域",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "社会福利领域",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
          {
            text: "社会保障领域",
            nodes: [
              {
                text: "建筑业企业自有施工机械设备年末总台数",
                href: "#arch/result/建筑业企业自有施工机械设备年末总台数",
                tags: ["0"],
              },
              {
                text: "国有建筑业总产值",
                href: "#arch/result/国有建筑业总产值",
                tags: ["0"],
              },
            ],
          },
        ],
      },
    ];

    // $(function () {
    //   var defaultData = [
    //     {
    //       text: "Parent 1",
    //       nodes: [
    //         {
    //           text: "Child 1",
    //           nodes: [
    //             {
    //               text: "地区生产总值",
    //               href: "#/search/result/地区生产总值",
    //               tags: ["0"],
    //             },
    //             {
    //               text: "Grandchild 2",
    //               href: "#grandchild2",
    //               tags: ["0"],
    //             },
    //           ],
    //         },
    //         {
    //           text: "Child 2",
    //           href: "#child2",
    //           tags: ["0"],
    //         },
    //       ],
    //     },
    //     {
    //       text: "Parent 2",
    //       href: "#parent2",
    //       tags: ["0"],
    //     },
    //     {
    //       text: "Parent 3",
    //       href: "#parent3",
    //       tags: ["0"],
    //     },
    //     {
    //       text: "Parent 4",
    //       href: "#parent4",
    //       tags: ["0"],
    //     },
    //     {
    //       text: "Parent 5",
    //       href: "#parent5",
    //       tags: ["0"],
    //     },
    //   ];
    // @ts-ignore
    $("#treeview1").treeview({
      levels: 1, //显示一层
      data: defaultData,
      enableLinks: true, //允许使用链接
    });
  });
});
</script>

<template>
  <div class="container-fluid pt-25">
    <!-- Row -->
    <div class="row">
      <!-- <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12"> -->
      <div class="col-lg-4">
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
      <div class="col-lg-8 col-md-7 col-sm-12 col-xs-12">
        <router-view></router-view>
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
