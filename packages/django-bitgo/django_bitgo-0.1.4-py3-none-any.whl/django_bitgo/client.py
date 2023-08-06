from re import L
import requests
import os
from django.conf import settings

from django_bitgo.exceptions import BitGoException


class BitGoClient(object):
    def __init__(self, access_token: str = "") -> None:
        """
        Initializes the BitGo Client

        :param str access_token: Access Token to authenticate with
        """

        self.access_token = access_token or os.getenv("BITGO_ACCESS_TOKEN")

        if not self.access_token:
            raise BitGoException("Access token is required to create a BitGoClient")

    def request(self, method="GET", headers={}, path="", payload={}):
        headers["Authorization"] = f"Bearer {self.access_token}"

        return requests.request(
            method=method,
            url=f"{self.get_api_url()}{settings.BITGO_API_VERSION}{path}",
            headers=headers,
            data=payload,
        )

    def get_api_url(self):
        return settings.BITGO_API_URL

    def get_api_version(self):
        return settings.BITGO_API_VERSION
