import httpRequest from "@/request";
export function getLinePredictInfoApi(str) {
  return httpRequest({
    url: "/prediction/indicator/" + str,
    method: "get",
    // loading: false,
  });
}
export function getLinePredictInfoApiCity(str) {
  return httpRequest({
    url: "/prediction/citygdp/" + str,
    method: "get",
    // loading: false,
  });
}
export function getLinePredictInfoApiProvince(str) {
  return httpRequest({
    url: "/prediction/prvincegdp/" + str,
    method: "get",
    // loading: false,
  });
}
