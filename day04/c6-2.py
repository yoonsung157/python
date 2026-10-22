 
# 예외객체 : 발생한 예외의 정보를 갖는 객체
# 예외클래스 : Exception(예외 최상위 클래스)
# except 예외클래스명 as 변수명 :
# as 키워드 : 클래스의 객체변수 생성
# 그 외 모든 예외 처리 : 여러 개 except에서 Exception은 항상 마지막에 위치
# 주의할 점 : Exception이 앞에 위치하면 아래 예외가 작동을 안함
# raise : 강제로 예외발생, 주로 CRUD 실패 의미
# p.383
list_number = [52, 273, 32, 72, 100]
try :
    number_input = int(input("정수 입력> "))    # 타입 예외 가능성
    print( list_number[ number_input ] )        # 인덱스 예외 가능성
except ValueError as e :
    print(e)
except IndexError as e :
    print(e)