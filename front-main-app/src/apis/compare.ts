import httpRequest from "@/request";
export function getAreaInfoApi() {
  return httpRequest({
    url: "/contrast/province",
    method: "get",
    loading: true,
  });
}

export function getThreeIndustry() {
  return httpRequest({
    url: "/contrast/primary",
    method: "get",
    loading: true,
  });
}

export function getTimeInfo() {
  return httpRequest({
    url: "/contrast/time",
    method: "get",
    loading: true,
  });
}
