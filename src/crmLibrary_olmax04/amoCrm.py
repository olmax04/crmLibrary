import os
import requests
from .database import *


class AmoCrm:
    db = api
    url = "https://grandre.kommo.com/"
    client_id = os.environ.get("INTEGRATION_ID")
    client_secret = os.environ.get("SECRET_KEY")

    @staticmethod
    def refresh():
        record = AmoCrm.db.find_one()
        data = {
            "client_id": AmoCrm.client_id,
            "client_secret": AmoCrm.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": record['refresh_token'],
            "redirect_uri": "https://google.com/"
        }
        result = requests.post(f"{AmoCrm.url}/oauth2/access_token", data).json()
        api.update_one({"token_type": 'Bearer'}, {
            "$set": {
                'expires_in': result['expires_in'],
                'access_token': result['access_token'],
                'refresh_token': result['refresh_token']
            }
        })
        return result['access_token']

    @staticmethod
    def request(func):
        def wrapper(*args, **kwargs):
            params = func(*args, **kwargs)
            access_token = AmoCrm.refresh()
            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {access_token}"
            }
            if 'headers' in params:
                headers.update(params['headers'])
                params.pop("headers")
            url = AmoCrm.url + params['url']
            params.pop("url")
            return requests.request(**params, headers=headers, url=url)

        return wrapper