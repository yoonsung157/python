# 1) 배열의 인덱싱
import numpy as np
x = np.array( [10, 20, 30, 40] )
print( x[0] ) # 10
print( x[-2] ) # 40
print( x[ [0, 2] ] ) # [ [특정인덱스, 특정인덱스 ] ] , [10 30]
print( x[ x > 20 ] )
# 2) 2차원 인덱싱 
x = np.array( [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] )
print( x[ 0, 0 ] ) # 1
print( x[ 1, 2 ] ) # 6
print( x[-1, -1] ) # 마지막행 마지막열 # 9
print( x[ x > 5] ) # [6 7 8 9]

# 3) 슬라이싱
x = np.array( [10, 20, 30, 40, 50] )
print( x[ 1 : 4 ] ) # [20 30 40]
print( x[ : 3 ] ) # 시작 인덱스 생략시 0
print( x[ -3 : ] ) # 끝 인덱스 생략시 마지막 인덱스 # [30 40 50]
print( x[ : : 2 ] ) # 2칸씩 이동, [10 30 50]
# 4) 
x = np.array( [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] )
# print( x[ 행슬라이싱, 열슬라이싱 ] )
print( x[ : , 1] ) # 행 : 전체, 열 : 1 # [2 5 8]
print( x[ 1, : ] ) # 행 : 1, 열 : 전체 # [4 5 6]
print( x[ 0:2, 1:3 ] ) # [ [2 3] [5 6] ] 
print( x[x[ :, 1] > 5])
# 5) 슬라이싱 주의할 점 :
x = np.array( [10, 20, 30, 40, 50] )
y = x[ 1:4 ] #[20 30 40] # 주소참조
y[0] = 100
print( x ) # 원본도 같이 변경됨

# 6) 배열의 연산
x = np.array( [1, 2, 3] )
y = np.array( [4, 5, 6] )
print( x + y ) # 같은 위치끼리 더함 
print( x * y )
print( x ** 2 )
print( np.sqrt( x ) ) # 제곱근/루트
print( x > 2 ) # [False False True]
print( (x > 1) & (x < 3) ) # [False  True False]
print( (x == 1 ) | ( x == 3) ) # [True False  True]
print( x > y ) # [False False False]

