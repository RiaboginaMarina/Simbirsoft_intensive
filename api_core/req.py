import requests


class Session(requests.Session):
    # Status codes
    OK = 200
    NO_CONTENT = 204

    def get(self, url, **kwargs):
        return super().get(url, **kwargs)

    def patch(self, url, **kwargs):
        return super().patch(url, **kwargs)

    def delete(self, url, **kwargs):
        return super().delete(url, **kwargs)

    def post(self, url, **kwargs):
        return super().post(url, **kwargs)
