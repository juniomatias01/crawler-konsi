import json
import requests
from typing import Dict


class CrawlerClient:
    """
This crawler accesses the extratoclube website and retrieves benefits using a given CPF.
It handles the login process, authentication token retrieval and usage, and benefit requests
to obtain the desired data.
    """

    def __init__(self, app_config: Dict,login_user: str, login_password: str):
        self.base_url = app_config.CRAWLER_BASE_URL
        self.origin = app_config.CRAWLER_ORIGIN
        self.referer = app_config.CRAWLER_REFERER
        self.login_user = login_user
        self.login_password = login_password

        self.auth_token = ""
        self.request_headers = {}

    def request_login(self) -> None:
        request_url = self.base_url + "login"

        payload = json.dumps(
            {
                "login": self.login_user,
                "senha": self.login_password,
            }
        )
        headers = {
            "Origin": self.origin,
            "Referer": self.referer,
        }

        response = requests.request("POST", request_url, headers=headers, data=payload)
        if response.status_code != 200:
            raise Exception(
                f"The website login has failed, server responded with a {response.status_code} status code"
            )

        auth_token = response.headers["Authorization"]
        self.auth_token = auth_token

    def request_benefits(self, cpf: str) -> Dict:
        request_url = self.base_url + f"offline/listagem/{cpf}"
        headers = {
            "Origin": self.origin,
            "Referer": self.referer,
            "Authorization": self.auth_token,
        }

        response = requests.request("GET", request_url, headers=headers, data={})
        if response.status_code != 200:
            raise Exception(
                f"The website benefits endpoint has failed, server responded with a {response.status_code} status code"
            )

        return json.loads(response.text)

    def get_benefits(self, cpf: str, complete: bool = False) -> Dict:
        self.request_login()
        if not self.auth_token:
            raise Exception(
                "The website login has failed, the authorization token was not saved"
            )

        response = self.request_benefits(cpf)
        if complete:
            return response
        else:
            # The number of the benefit its inside the beneficios key and its named nb
            return response["benefits"][0]["nb"]
