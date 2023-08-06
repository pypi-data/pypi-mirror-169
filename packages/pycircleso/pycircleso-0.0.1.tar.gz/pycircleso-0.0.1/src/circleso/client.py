from typing import Sequence
import requests


class CircleSo:
    def __init__(self, api_url: str, api_key: str):

        self.api_url = api_url.rstrip("/")
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Token {self.api_key}",
            "user-agent": "pycircleso/0.0.1",
        }

    def __get(self, path: str, data: dict = None):
        return self.__method(method="GET", path=path, data=data)

    def __post(self, path: str, data: dict = None):
        return self.__method(method="POST", path=path, data=data)

    def __put(self, path: str, data: dict = None):
        return self.__method(method="PUT", path=path, data=data)

    def __method(self, method: str, path: str, data: dict = None):
        url = f"{self.api_url}{path}"
        request_params = {
            "method": method,
            "url": url,
            "headers": self.headers,
        }
        if data:
            request_params["data"] = data
        return requests.request(**request_params).json()

    def me(self) -> dict:
        return self.__get("/api/v1/me")

    def communities(self) -> dict:
        return self.__get("/api/v1/communities")

    def community(self, community_id: str) -> dict:
        return self.__get(f"/api/v1/communities/{community_id}")

    def space_groups(self, community_id: str):
        return self.__get(f"/api/v1/space_groups?community_id={community_id}")

    def space_group(self, community_id: str, space_group_id: str):
        return self.__get(
            f"/api/v1/space_groups/{space_group_id}?community_id={community_id}"
        )

    def spaces(
        self,
        community_id: str,
        sort: str = "active",
        per_page: int = 100,
        page: int = 1,
    ):
        return self.__get(path="/api/v1/spaces")

    def members(self):
        return self.__get("/api/v1/community_members")

    def member_invite(
        self,
        email: str,
        community_id: str,
        password: str = None,
        name: str = None,
        space_ids: Sequence = None,
        space_group_ids: Sequence = None,
        member_tag_ids: Sequence = None,
        bio: str = None,
        headline: str = None,
        facebook_url: str = None,
        twitter_url: str = None,
        instagram_url: str = None,
        linkedin_url: str = None,
        website_url: str = None,
        avatar: str = None,
        skip_invitation: bool = False,
        location: str = None,
    ):
        kwargs = vars()
        params = {}
        for item in kwargs:
            if item == "self":
                continue
            if kwargs[item] is None:
                continue
            params[item] = kwargs[item]
        return self.__post(path="/api/v1/community_members", data=params)
