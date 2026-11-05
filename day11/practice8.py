# Practice8: API 데이터 수집
# 1. 개요 및 대상 API 정보
# API 이름: 행정안전부_착한가격업소 현황
# API URL: https://www.data.go.kr/data/3045247/fileData.do 

# 목표: httpx를 통해 공공데이터 API를 호출하고, pandas를 활용해 업소명, 주소, 가격 데이터를 구조화한 뒤 통계 분석을 수행합니다.
# 2. 상세 요구사항
# 2-1 (API 호출 및 파라미터 설정):
# 지정된 API URL에 인증키(serviceKey)를 포함하여 요청합니다.
# 임의의 100건의 데이터를 수집
service_key = "14acc8e83a6341080aad0f011b0d5898c1d422cde9a1fdf913779e81293ab066"
# 2-2 (데이터프레임 적재):
# 응답받은 JSON 데이터 중 실제 행 목록인 data 배열을 추출하여 pandas.DataFrame으로 변환합니다.

# 2-3 (데이터 전처리 및 분석):
# 가격1 컬럼의 데이터를 숫자형(pd.to_numeric)으로 변환합니다.
# 수집된 100건 데이터 기준 가격1의 평균값을 산출하여 출력합니다.

# 2-4 (업종별 평균 가격 집계 및 시각화):
# groupby('업종')을 사용하여 업종별 가격1의 평균 가격을 계산합니다.
# seaborn의 barplot 및 matplotlib을 활용하여 업종별 평균 가격 비교 막대그래프를 시각화합니다.

# 1] 라이브러리 호출
import httpx                        
import pandas as pd                 
import matplotlib.pyplot as plt     
import seaborn as sns               

# 2] 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
sns.set_theme(font='Malgun Gothic', rc={'axes.unicode_minus': False}, style='whitegrid')

def 실습8() :
    # 2-1
    url = "https://api.odcloud.kr/api/3045247/v1/uddi:0d236000-b33f-41ad-9227-ee0efa3ec6c8"
    url += "?page=1"
    url += "&perPage=100"
    url += f"&serviceKey={service_key}"
    
    response = httpx.get( url )         
    response_json = response.json()

    # 2-2
    df = pd.DataFrame( response_json['data'] )
    df = df[ ['업소명' , '주소' , '업종' , '가격1'] ]   
    print( df.head() )
    df.info()

    # 2-3
    df['가격1'] = pd.to_numeric( df['가격1'] , errors='coerce' )
    가격평균 = df['가격1'].mean()
    print( f"수집 {len(df)}건 가격1 평균 : {가격평균:,.0f}원" )

    # 2-4
    업종별평균 = df.groupby('업종')['가격1'].mean().reset_index()
    업종별평균 = 업종별평균.sort_values( '가격1' , ascending=False )   
    print( 업종별평균 )

    plt.figure( figsize=( 10 , 5 ) )
    bars = sns.barplot( data=업종별평균 , x='업종' , y='가격1' , hue='업종' , palette='Set2' , legend=False )
    for container in bars.containers :
        bars.bar_label( container , fmt='%.0f' , padding=3 , fontsize=8 )   # 막대 값 레이블
    plt.title( "업종별 평균 가격 비교 (착한가격업소 100건)" )
    plt.xlabel( "업종" )
    plt.ylabel( "평균 가격(원)" )
    plt.xticks( rotation=30 )
    plt.tight_layout()
    plt.show()
실습8()
