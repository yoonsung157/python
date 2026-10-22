# 함수 : 코드의 집합 
    # 값 저장 = 변수, 실행코드 저장 = 함수
    # 값 여러개 저장 = 리스트/딕셔너리/튜플 
# 매개변수 : 한수를 호출할 때 괄호 내부에 여러가지를 넣는 변수
# 리턴값 : 함수를 호출해서 최종적으로 나오는 결과
# def 함수명( 매개변수명 ) :
    # 실행문

# 값 재사용 = 변수, 코드 재사용 = 함수/반복문
# "안녕하세요" 3번 출력 반복해야한다.

# 1. 기본적인 함수
def print_3_time() :    # 함수 정의
    print("하이")
    print("하이")
    print("하이")
print_3_time()      # 함수 사용/호출

# vs 식별자란? p.71 변수/함수명
for i in range(0,3,1) : # 
    print("하이")
# 2. 매개변수란? 매개(서로 다른 곳에서 연결)
# 파이썬은 { }가 아닌 탭(들여쓰기) 이용하여 구역 구분
def print_n_times( value, n ) :
    for i in range( n ) :
        print( value )

print_n_times( "안녕하세요", 5 ) # 인수/인자값 : 함수 호출할 때 매개변수에 전달하는 값

# p.278 가변 매개변수
# 조건 1 : 가변매개변수를 가장 뒤에 정의
# 조건 2 : 1번만 사용
# def 함수명( 매개변수, 매개변수, *가변매개변수 ) 

def print_n_times2( n, *values ) :
    for i in range(n) :
        for value in values :
            print(value)
        print()

print_n_times2(3, "안녕", "즐거운", "파이썬" )
print_n_times2(2, "하이", "즐거운")

# p.279 기본 매개변수, 매개변수에 기본값 대입 형태, 인수/인자 값 생략 시 기본 값 적용
def print_n_times3( value, n = 2 ) :
    for i in range( n ) :
        print( value )
print_n_times3("하이")

# p.280 
# 기본 매개변수가 가변 매개변수보다 앞에 올때, 오류
# 가변 매개변수가 기본 매개변수보다 앞에 올때, 기본 매개변수 인자값 없다.
# 해결방안 : 키워드 매개변수
print("안녕하세요") # 안녕하세요 출력 코드
print("안녕하세요", end = "\n") # end매개변수 : 출력 후 할 행동
print("안녕하세요", end = "") # 키워드매개변수랑? 인수 대입시 매개변수명 지정
def print_n_times4( *values, n = 2 ) :
    for i in range( n ) :
        for value in values :
            print( value )
        print()
print_n_times4("하이","파이썬", n = 4) # 인수 전달시 매개변수명 지정 3번 반복
print_n_times4("하이","파이썬", 10) # 2번 반복

# p.285
# 1. 자료 없는 리턴하기 , java void
def return_test() :
    print("a")
    return
    print("b")
return_test()
# 2. 자료와 함께 리턴하기
def return_test2( ) :
    return 100
value = return_test2()
print( value )

def sum_all(start, end) :
    output = 0
    for i in range(start, end + 1) :
        output += i
        return output
print("0 to 100: ", sum_all(0,100))
print("0 to 1000: ", sum_all(0,1000))
print("50 to 100: ", sum_all(50,100))
print("500 to 1000: ", sum_all(500,1000))

def sum_all2(start=0, end=100, step=1) :
    output = 0
    for i in range( start, end + 1, step ) :
        output += i
        return output
print("A.", sum_all2(0, 100, 10))
print("B.", sum_all2(end = 100))
print("C.", sum_all2(end = 100, step = 2))

# p.293 재귀함수, 재귀란 자기자신을 호출하는 것
# 1) 팩토리얼 반복문
def factorial1(n) :
    output = 1
    for i in range( 1, n+1 ) :
        output *= i
    return output

# 2) 팩토리얼 재귀
def factorial2( n ) :
    if n == 0 :
        return 1
    else :
        return n * factorial2(n-1)

