# 웹 크롤링 : 웹페이지 존재하는 데이터들을 수집하는 기술
# HTML/CSS 기초 지식
# 파이썬 크롤링 라이브러리 :
    # 정적( request/Beautifulsoup )
    # 동적( selenium, Playwright )
# 확인
    # 1. 크롤링할 페이지의 도메인주소/robots.txt
    # 2. 개발자도구(F12) -> ctrl + shift + c

# 설치 : pip install requests
# 설치 : pip install BeautifulSoup

# 1) 네이버 검색 정보 크롤링( 정적 )
# 1. 크롤링 주소 가져오기, *파라미터 정리*
url = "https://search.naver.com/search.naver?&query=안양날씨"
# 2. requsts 라이브러리로 해당 주소 요청하기
import requests                     # URL 요청 라이브러리
response = requests.get( url ) # requests.get("요청할 주소")
print( response )              # 
print( response.text )         # 요청한 주소의 HTML 문자로 반환

# 3. 요청 성공했으면 요청한 페이지의 HTML 파싱하기
from bs4 import BeautifulSoup       # 요청된 URL의 HTML 파싱 라이브러리
# BeautifulSoup( response.text, "html.parser" )
soup = BeautifulSoup( response.text, "html.parser" ) # 요청한 URL 결과 문자열들을 HTML 형식으로 반환
print( soup )

# 4. 파싱한 이유 : 특정한 식별자(마크업)의 텍스트/정보 추출
# soup.select( 선택자 ) : 여러개 추출 # soup.select_one( 선택자 ) : 한개 추출
text = soup.select_one(".temperature_text > span")
print(text)

# 5. 마크업 사이의 텍스트 추출
# 추출한DOM.get_text()
print( text.get_text() )