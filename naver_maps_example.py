import os
import requests


def get_coordinates(address: str):
    """
    주어진 주소에 대해 NAVER 지도 지오코딩 API를 호출하여 좌표를 반환합니다.
    """
    # 환경 변수에서 클라이언트 ID와 시크립을 불러온다.
    client_id = os.environ.get("NAVER_CLIENT_ID")
    client_secret = os.environ.get("NAVER_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise ValueError("NAVER_CLIENT_ID과 NAVER_CLIENT_SECRET 환경 변수를 설정하세요.")
    # API 엔드포인트 URL
    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    # 요청 파라미터; query에 주소를 지정
    params = {"query": address}
    # 인증 헤더 구성
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
    }
    # GET 요청을 보내고 응답을 반환합니다
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # 기본 테스트 주소
    address = "서울특별시청"
    result = get_coordinates(address)
    print(result)
