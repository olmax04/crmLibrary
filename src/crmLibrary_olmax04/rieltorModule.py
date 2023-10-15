import os

import requests


class RieltorModule:
    url = "https://api.amorealtor.ru/"
    api_key = os.environ.get("RIELTOR_API_KEY")

    @staticmethod
    def request(func):
        def wrapper(*args, **kwargs):
            params = func(*args, **kwargs)
            headers = {
                'Accept': 'application/json',
                'Authorization': f'Api {RieltorModule.api_key}'
            }
            if 'headers' in params:
                headers.update(params['headers'])
                params.pop("headers")
            url = RieltorModule.url + params['url']
            params.pop("url")
            return requests.request(**params, headers=headers, url=url)

        return wrapper
