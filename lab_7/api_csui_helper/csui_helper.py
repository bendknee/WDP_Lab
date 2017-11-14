import requests
import os
import environ

root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')
API_MAHASISWA_LIST_URL = "https://api.cs.ui.ac.id/siakngcs/mahasiswa-list/"

class CSUIhelper:
    class __CSUIhelper:
        def __init__(self):
            self.username = env("SSO_USERNAME")
            self.password = env("SSO_PASSWORD")
            self.client_id = 'X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG'
            self.access_token = self.get_access_token(self.username, self.password)

        def get_access_token(self, username, password):
            try:
                url = "https://akun.cs.ui.ac.id/oauth/token/"

                payload = "username=" + username + "&password=" + password + "&grant_type=password"
                headers = {
                    'authorization': "Basic WDN6TmtGbWVwa2RBNDdBU05NRFpSWDNaOWdxU1UxTHd5d3U1V2VwRzpCRVFXQW43RDl6a2k3NEZ0bkNpWVhIRk50Ymg3eXlNWmFuNnlvMU1uaUdSVWNGWnhkQnBobUU5TUxuVHZiTTEzM1dsUnBwTHJoTXBkYktqTjBxcU9OaHlTNGl2Z0doczB0OVhlQ3M0Ym1JeUJLMldwbnZYTXE4VU5yTEFEMDNZeA==",
                    'cache-control': "no-cache",
                    'content-type': "application/x-www-form-urlencoded"
                }

                response = requests.request("POST", url, data=payload, headers=headers)

                return response.json()["access_token"]
            except Exception:
                raise Exception("username atau password sso salah, input : [{}, {}] {}".format(username, password, os.environ.items()))

        def get_client_id(self):
            return self.client_id

        def get_auth_param_dict(self):
            dict = {}
            access_token = self.get_access_token(self.username, self.password)
            client_id = self.get_client_id()
            dict['access_token'] = access_token
            dict['client_id'] = client_id

            return dict

        def get_mahasiswa_list(self):
            response = requests.get(API_MAHASISWA_LIST_URL,
                                    params={"access_token": self.access_token, "client_id": self.client_id})
            mahasiswa_list = response.json()["results"]
            return mahasiswa_list

    instance = None

    def __init__(self):
        if not CSUIhelper.instance:
            CSUIhelper.instance = CSUIhelper.__CSUIhelper()
