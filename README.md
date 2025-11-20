# NAVER 지도 프로토타입

이 저장소는 Python을 사용하여 NAVER 지도 API와 상호작업하는 방법을 보여주는 간담한 프로토타입입니다. API 자격 증명 처리와 지오코디드 정보를 가져오는 기본 엔드포인트 호출 예제가 포함되어 있습니다.

## 사전 준비 상황

- Python 3.7 이상
- NAVER 클럽 플랫폼 계정 및 지도 API 활성화
- NAVER 지도 API 자격 증명 (Client ID 와 Client Secret)

## 설정 방법

1. 저장소를 클로드합니다:  
   ```bash
   git clone https://github.com/geonryunghan/naver-maps-prototype.git
   cd naver-maps-prototype
   ```

2. (선택 사항) 가상환경을 생성하고 활성화합니다:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # 위너우에서는 `venv\Scripts\activate`
   ```

3. 필요한 패키지를 설치합니다:  
   이 프로토타입은 HTTP 호출을 위해 `requests` 라이브러리를 사용합니다. 다음 명령으로 설치할 수 있습니다:  
   ```bash
   pip install requests
   ```  
   `requirements.txt` 파일을 사용하고 싶다면, `requests` 패키지를 적어 파일을 만들고 다음과 같이 설치할 수 있습니다:  
   ```bash
   pip install -r requirements.txt
   ```

4. 스크립트를 실행하기 전에 NAVER 지도 API 자격 증명을 환경 변수로 설정합니다:  
   Unix/macOS:
   ```bash
   export NAVER_CLIENT_ID=여러분의_client_id
   export NAVER_CLIENT_SECRET=여러분의_client_secret
   ```  
   Windows 명령 프롬프트:
   ```cmd
   set NAVER_CLIENT_ID=여러분의_client_id
   set NAVER_CLIENT_SECRET=여러분의_client_secret
   ```

## 빠른 시작

의존성을 설치하고 API 자격 증명을 설정한 후, 지오코디 요청을 수행하기 위해 샘플 스크립트를 실행할 수 있습니다:

```bash
python naver_maps_example.py
```

이 스크립트는 기본 주소(“서울특별시청”)의 위치를 열린 후 JSON 응답을 출력합니다. 다른 주소를 텍스트해보려면 `naver_maps_example.py` 파일의 `address` 변수를 수정하세요.

## 다음 단계

- 역지오코디드, 길찾기, 장소 검색 등 NAVER 지도 API의 다른 엔드포인트를 탐색해 보세요.  
- API 호출을 자동화하기 위해 재사용 가능한 함수나 클래스로 몰려 구성을 개선하세요.  
- API 문서에 따른 오류 처리와 요청 제한을 지열하세요.

## 라이선스

이 프로토타입은 예제로 제공되며 MIT 라이선스로 배포됩니다.
