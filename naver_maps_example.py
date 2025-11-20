import os
import requests


def get_coordinates(address: str):
    """
    Call NAVER Maps geocode API to get coordinates for a given address.
    """
    client_id = os.environ.get("NAVER_CLIENT_ID")
    client_secret = os.environ.get("NAVER_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise ValueError("Set environment variables NAVER_CLIENT_ID and NAVER_CLIENT_SECRET.")
    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    params = {"query": address}
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    address = "Seoul City Hall"
    result = get_coordinates(address)
    print(result)
