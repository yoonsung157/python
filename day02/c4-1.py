# p.192
# 리스트란? 대괄호[]에 자료를 쉼표로 구분하여 여러 자료들을 저장
# [요소, 요소, 요소 ], 요소=element
# 인덱스란? 리스트내 요소들이 저장된 순서번호, 0번시작.

# 리스트
list_a = [273, 32, 103, "문자열", True, False]
print( list_a[ 2 ] )    # 인덱싱 # 103
print( list_a[ 1:3 ] )  # 1~2 # [32, 103] # 슬라이싱
list_a[2] = 7 # 요소 값 수정/변경
print( list_a[2] ) # 7
print( list_a[-2] ) # True # 파이썬에서는 인덱싱 음수로 가능
print( list_a[3][1]) # 자 # 문자열도 리스트/배열 # 문자=리터럴
# print( list_a[1][1] ) # 오류 # 리터럴/1차원값
list_1 = [1, 2, 3] # 1차원
list_2 = [ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ] ] # 2차원
list_3 = [ [ [  1, 2 ], [ 3, 4 ] ] , [ 5, 6 ] ] # 3차원
print( list_2[1][0]) # 3
# 고차원 배열 = 판다스/데이터프레임워크 = RGB

# p.196 , + 연결, * 반복, len( ) 길이
list_a = [ 1, 2, 3 ]
list_b = [ 4, 5, 6 ]
print( list_a + list_b ) # 리스트 + 리스트 -> 연결
print( list_a * 3 ) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print( len(list_a) ) # 3
list_aa = [ [1], [2], [3] ]
print( list_a + list_aa) # [1, 2, 3, [1], [2], [3] ]
list_a.append( 4 ) # 요소 추가
print( list_a ) # [1, 2, 3, 4]
list_a.insert( 0, 5 ) # 특정 인덱스에 요소 삽입 # .insert( 위치, 값 )
print( list_a )# [5, 1, 2, 3, 4] 
# 주의할 점
list_c = [ 1, 2 ]
list_c + [3]           # 방법1) [ 1, 2, 3 ] 새로운리스트 생성, list_c 변화 없다.
list_c.append(3)        # 방법2) [ 1, 2, 3 ] 기존 리스트 포함, list_c 변화 있다.
print( list_c )

# p.202 요소 삭제하기
list_a = [ 1, 2, 3, 4, 5 ]
del list_a[1] # 1번 인덱스 삭제
print(list_a) # [1, 3, 4, 5]

list_a.pop(2) # 2번 인덱스 삭제
print(list_a) # [1, 3, 5]
del list_a[ 0 : 2 ] # del 키워드 이용한 슬라이싱 삭제
print( list_a ) # [5]
# 리스트명.remove( 값 ) # 값 삭제
list_a.remove( 5 )
print( list_a ) # [ ]
# 리스트명.clear()
list_a.clear()

list_a = [0, 1, 2, 3, 4, 5, 6, 7]
print(list_a)
list_a.clear()
print(list_a)