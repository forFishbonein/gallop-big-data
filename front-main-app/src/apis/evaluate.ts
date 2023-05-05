import httpRequest from "@/request";
export function getEvaluateInfoApiProvince(str) {
  return httpRequest({
    url: "/evaluation/pro/" + str,
    method: "get",
    // loading: false,
  });
}
export function getEvaluateInfoApiYear(str) {
  return httpRequest({
    url: "/evaluation/year/" + str,
    method: "get",
    // loading: false,
  });
}
