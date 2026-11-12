# 1. import
import uvicorn
from fastapi import FastAPI
# 2. fastapi 객체
app = FastAPI()
# 3. 서버 실행 함수
if __name__ == "__main__" :
    uvicorn.run( "f-02:app", host="127.0.0.1", port=8000, reload=True)
# 4. 서버 실행: 현재파일py 실행 # 여러번 실행 불가
# 5. REST: 지원 주고받는 상태구조, REST API : HTTP로 REST 구현한 것

# 1) FastAPI 객체 내 get/post/put/delete 메소드 지원
@app.get("/") # @app.get("/매핑주소")
async def index() : # async def 함수명() : 비동기 함수 선언
    return " 안녕 파이썬 웹" # 반환값 # ResponseBody

# 2) 쿼리스트링 : HTTP URL 경로상에 ? 뒤로 정의된 변수들
@app.get("/user")
async def user( name, age:int) : # 파이썬은 동적 타입이지만 "변수명:타입명" 정적 타입 가능
    info = { 'name' : name, 'age' : age, 'msg' : '*쿼리통신 성공*'}
    return info # 딕셔너리가 JSON 타입으로 자동반환

# 3) 경로파라미터 : HTTP URL 경로상에 / 구분하여 변수들
@app.get("/item/{name}/{age}")
async def item( name: str, age : int | None = None ) :
    return { name : name, age: age, 'msg' : "*경로통신성공*" }

# 4) 본문 , HTTP GET/DELETE -> 쿼리/경로, HTTP POST/PUT -> 쿼리/경로/본문BODY
@app.post("products")
async def products( product : dict ) :
    product['msg'] = "본문통신성공"
    return product