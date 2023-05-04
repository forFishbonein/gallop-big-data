getPeopleSexApi;
import httpRequest from "@/request";
export function getPeopleSexApi() {
  return httpRequest({
    url: "/visualization/people/peoplesex",
    method: "get",
    // loading: false,
  });
}
