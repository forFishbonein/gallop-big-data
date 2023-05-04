import httpRequest from "@/request";
export function getBubbleInfoApi(str) {
  return httpRequest({
    url: "/singlequery/alldata/" + str,
    method: "get",
    // loading: false,
  });
}
export function getLineInfoApi(str) {
  return httpRequest({
    url: "/singlequery/avgdata/" + str,
    method: "get",
    // loading: false,
  });
}

export function getAllProvinces() {
  return httpRequest({
    url: "/query/provincelist",
    method: "get",
    // loading: false,
  });
}
export function getMapInfoApi(str, year) {
  return httpRequest({
    url: "/singlequery/year/" + str + "/" + year,
    method: "get",
    // loading: false,
  });
}
export function getLineInfoByAreaApi(str, area) {
  return httpRequest({
    url: "/singlequery/pro/" + str + "/" + area,
    method: "get",
    // loading: false,
  });
}
