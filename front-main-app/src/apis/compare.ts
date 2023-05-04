import httpRequest from "@/request";
import httpRequest from "@/request";
export function getAreaInfoApi() {
  return httpRequest({
    url: "/contrast/province",
    method: "get",
    // loading: false,
  });
}
