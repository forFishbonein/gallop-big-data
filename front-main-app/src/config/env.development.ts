// 本地环境配置
export default {
  env: "development",
  mock: true,
  title: "开发",
  baseUrl: "", // 项目地址
  // baseApi: "http://localhost:8080", // 本地api请求地址,注意：如果你使用了代理，请设置成'/'
  baseApi: "http://127.0.0.1:5000", // 本地api请求地址,注意：如果你使用了代理，请设置成'/'
};
