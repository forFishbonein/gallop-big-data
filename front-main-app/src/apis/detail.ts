import httpRequest from "@/request";
export function getBubbleInfoApi(str) {
  return httpRequest({
    url: "/singlequery/alldata/" + str,
    method: "get",
    // loading: false,
  });
}
