import requests
from typing import Dict


class CrawlerClient:
    """
    This crawler accesses the extratoclube website and retrieves benefits using a given CPF.
    It handles the login process, authentication token retrieval and usage, and benefit requests
    to obtain the desired data.
    """

    LOGIN_ENDPOINT = "login"
    BENEFITS_ENDPOINT = "offline/listagem/"

    def __init__(self, app_config: Dict, login_user: str, login_password: str):
        """
        Initializes the CrawlerClient.

        :param app_config: A dictionary with application configurations.
        :param login_user: The username used for logging in.
        :param login_password: The password used for logging in.
        """
        self.base_url = app_config.CRAWLER_BASE_URL
        self.origin = app_config.CRAWLER_ORIGIN
        self.referer = app_config.CRAWLER_REFERER
        self.login_user = login_user
        self.login_password = login_password
        self.auth_token = ""

    def request_login(self) -> None:
        """
        Requests login to the website and retrieves the authentication token.
        """
        url = f"{self.base_url}{self.LOGIN_ENDPOINT}"
        headers = {
            "Origin": self.origin,
            "Referer": self.referer,
        }
        data = {
            "login": self.login_user,
            "senha": self.login_password,
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise Exception(f"Failed to log in to the website: {err}")

        self.auth_token = response.headers["Authorization"]

    def request_benefits(self, cpf: str) -> Dict:
        """
        Requests benefits from the website for a given CPF.

        :param cpf: The CPF to retrieve benefits for.
        :return: A dictionary with the benefits for the given CPF.
        """
        url = f"{self.base_url}{self.BENEFITS_ENDPOINT}{cpf}"
        headers = {
            "Origin": self.origin,
            "Referer": self.referer,
            "Authorization": self.auth_token,
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise Exception(f"Failed to retrieve benefits from the website: {err}")

        return response.json()

    def get_benefits(self, cpf: str, complete: bool = False) -> Dict:
        """
        Retrieves the benefits for a given CPF.

        :param cpf: The CPF to retrieve benefits for.
        :param complete: Whether to return the complete response or just the number of the first benefit.
        :return: A dictionary with the benefits for the given CPF, or the number of the first benefit.
        """
        self.request_login()

        if not self.auth_token:
            raise Exception("Failed to log in to the website")

        response = self.request_benefits(cpf)

        if complete:
            return response
        else:
            return response["beneficios"][0]["nb"]
