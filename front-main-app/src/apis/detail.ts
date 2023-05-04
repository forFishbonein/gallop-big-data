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
