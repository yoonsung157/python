
# 구문오류 : 실행 전 오류, 실행 자체 불가능
# 런타임오류 : 실행 중 오류, 예외
# 예외 처리 : 예외를 해결하는 모든 것

# 조건문 또는 try
# 예1) 조건문 예외
input_a = input('정수입력 : ')
#int( input a ) # ValueError # int( ) 정수로 변환 함수
if input_a.isdigit() : #문자열.isdigit() : 문자열타입의 값이 숫자이면 true
    int(input_a)
else :
    print('정수가 아님')
# 예2) try 예외
try :
    int (input_a ) # 예외가 발생할 것 같은 코드
except :
    print('정수가 아님')
# 예3) pass 키워드, 예외 어떻게 처리할지 모르는경우 일단 넘어가기
try :
    int( input_a )
except :
    pass
# 예4) else, 예외가 발생하지 않았을 때.
try :
    int( input_a )
except :
    print("정수가 아님")
else :
    print( "정수임" )
# 예5) finally, 예외가 발생하든 발생하지 않든 무조건 실행되는 코드
try :
    int( input_a )
except :
    print('정수아님')
else :
    print('정수임')
finally : 
    print('코드 끝')

# 예6) finally 활용 예
try :
    file = open( "info.txt", "w" ) 
    # open( 파일명, 옵션 ) # w옵션 : 파일이 없으면 생성
    예외.발생해라( ) # 일부러 예외 발생
    
except :
    print( "예외 발생" )
finally :
    file.close( ) # 파일.close( ) : 파일닫기

print( file.closed )
# finally 사용 : return 함수 종료, break 반복문 종료