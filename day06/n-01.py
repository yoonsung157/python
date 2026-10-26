# 1. 넘파이 설치, 터미널 : pip install numpy
# 2. 넘파이 불러오기
# import 라이브러리 이름
# import 라이브러리 이름 as 별칭
import numpy as np
print( np.__version__ ) # 2.5.4
# 3. 넘파이 학습하는 이유 : 1) 데이터분석(수치계산) 2) ML/DL 라이브러리들이 사용

# 1) 배열 생성
x = np.array( [1, 2, 3, 4] ) # 1차원 배열
print( x )
x = np.array( [ [1, 2, 3], [4, 5, 6] ]) # 2차원 배열
print( x )
# 특징 1: 동적타입은 느리고, 넘파이(정적타입)는 빠르다.
x = np.array( [ 1, True, "안녕" ])
print( x )

# 2) 0으로 배열 초기화, .zeros( 행 개수, 열 개수 )
x = np.zeros( (2, 3) ) 
print( x )

# 3) 1으로 채워진 배열로 초기화
x = np.ones( (2, 3) )
print( x )

# 4) arange( 시작인덱스, 끝인덱스, 단계 )
x = np.arange(0, 10, 2)
print( x )

# 5) 
x = np.linspace(0, 1, 5)
print( x )

# 6) 배열 길이 확인
x = np.array( [ [1, 2, 3], [4, 5, 6] ] ) # 2차원
print( x.shape ) # (2, 3) 2행 3열

# 7) 배열 타입 확인
x = np.array( [1.0, 2.0, 3.0] )
print( x.dtype ) # float64

# 8) 배열 차원 개수 확인
x = np.array( [ [ [1], [2] ], [ [2], [3] ], [ [3], [4] ] ] )
print( x.size ) # 요소/자료 개수
print( x.ndim ) # 차원수

# 9) 배열의 데이터 타입, np.array( 리스트/튜플, dtype=np.타입명)
# np.타입명(비트수), 32bit --> 4byte
# np.bool_ : 언더바 주의( 파이썬 bool vs 넘파이 bool_)
# np.bytes : 영문 또는 일부 특수문자(아스키코드) 1바이트, 한글(UTF-8) 3바이트
x = np.array( [1, 2, 3], dtype=np.int32 )
print( x.dtype )
x = np.array( [1.0, 2.0, 3.0 ], dtype=np.float32 )
print( x.dtype ) 
x = np.array( [True, False, True ], dtype=np.bool_)
print( x.dtype )
x = np.array( ['apple', 'banana', 'cherry'], dtype=np.bytes_)

# 10) 타입변환 .astype( np.새로운타입 )
x = np.array( [1.5, 2.5, 3.5], dtype= np.float32 )
y = x.astype( np.int32 )
print( y )

# * 타입 지정한 이유 : 1) 메모리 효율성/속도 2) 텐서플로우/파이토치 라이브러리 