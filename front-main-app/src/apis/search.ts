import httpRequest from "@/request";
export function getPageListInfo(str, size, number) {
  return httpRequest({
    url: "/query/listpage/" + str + "/" + size + "/" + number,
    method: "get",
    // loading: false,
  });
}
export function getAllListInfo(str) {
  return httpRequest({
    url: "/query/list/" + str,
    method: "get",
    // loading: false,
  });
}
