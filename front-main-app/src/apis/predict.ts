import httpRequest from "@/request";
export function getLinePredictInfoApi(str) {
  return httpRequest({
    url: "/prediction/indicator/" + str,
    method: "get",
    // loading: false,
  });
}
