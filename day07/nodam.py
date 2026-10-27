import numpy as np
data = np.genfromtxt('./day07/nodam.csv', delimiter=',', skip_header=1)
print(f"데이터 형태: {data.shape}")
# 지역코드 
# 서울특별시 1
# 부산광역시 2
# 대구광역시 3
# 인천광역시 4
# 광주광역시 5
# 대전      6
# 울산      7
# 세종      8
# 경기도    9
# 강원도    10
# 충청북도  11
# 충청남도  12
# 전북      13
# 전남      14
# 경상북도  15
# 경상남도  16
# 제주도    17
print( data[ : , 3] )
# 평균 흡연율
print(np.mean(data[ :, 3]))
# 흡연율 최댓값
print(np.max(data[ : , 3 ]))
# 금연 6개월 성공률
print( np.mean(data[ : , 23]))

# 집중 관리 대상
warning = data[(data[ : , 3] >= 19.32) & (data[ : , 23 ] <= 34.38 )]
hs = np.sum(warning[ :, 2])
print(hs)

# 집중 관리 지수
smoke = data[ :, 3] / data[ :, 23]
x = np.argmax(smoke)
print( data[107,0] )
print( (hs / np.sum(data[ : , 2]) ) * 100 )

print( np.mean(data[ : , 23]))
print( np.mean(data[ : , 14]))