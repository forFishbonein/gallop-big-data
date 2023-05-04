import httpRequest from "@/request";
export function getPeopleSexApi() {
  return httpRequest({
    url: "/visualization/people/peoplesex",
    method: "get",
    // loading: false,
  });
}
export function getFourCityInfoApi() {
  return httpRequest({
    url: "/visualization/financial/consumpution",
    method: "get",
    // loading: false,
  });
}
