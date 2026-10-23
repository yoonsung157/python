# 상속이란? 어떤 클래스를 기반으로 그 속성과 기능을 물려받아 새로운 클래스 만드는 것
# isinstance( 인스턴스, 클래스명 )
# 예1)
class Student :
    def __init__(self):
        pass
class Human :
    def __init__(self):
        pass
student = Student()
print( isinstance( student, Student) ) # True
print( isinstance( student, Human))    # False

# 예2)  c8-1.py 클래스 코드 가져와서 이어서 작성
class Student2 :
    # p.484 클래스변수 ? 인스턴스없이 사용 가능한 변수
    # 클래스변수명 = 초기값
    count = 0
    students = []
    # p.486 클래스함수
    @classmethod # 클래스 함수 정의하는 데코레이터
    def print( cls ) : # 매개변수에 cls 관례적으로 선언
        for student in cls.students :
            print(str( student ) ) 
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student2.count += 1
    def get_sum( self ) :
        return self.korean + self.math + self.english + self.science
    def get_average( self ) :
        return self.get_sum() / 4
    def to_string( self ) :
        return "{} \t {} \t {}".format( self.name, self.get_sum(), self.get_average())
    # 특수한 이름의 메소드 # 보조기능 재정의(오버라이딩)
    def __str__(self):
        return "{} \t {} \t {}".format( self.name, self.get_sum(), self.get_average())
    # 특수한 이름의 메소드 / 비교 메소드
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        return  self.get_sum >= value.get_sum()
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()
students = [
    Student2("윤인성", 87, 98, 88, 85),
    Student2("윤인성", 87, 98, 88, 85),
    Student2("윤인성", 87, 98, 88, 85),
    Student2("윤인성", 87, 98, 88, 85),
    Student2("윤인성", 87, 98, 88, 85),
    Student2("윤인성", 87, 98, 88, 85)
]

# 특수한 이름의 메소드 호출
print( str( students[0] ) )         # __str__ 함수 실행된다.
print( students[0] == students[1] )   # == 대신에 __eq__함수가 실행됨, True
print( students[0] != students[1])    # False 

# 클래스명.변수명 : 클래스변수 값 호출
print( Student2.count ) # 6

# p.491 프라이빗 변수
class Circle :
    def __init__(self, radius) :
        self.__radius = radius # 프라이빗 변수
        self.__radius2 = radius # 프라이빗 변수
    def get_circumference( self ) :
        return 2* self.__radius
    def get_radius( self ) :
        return self.__radius # 프라이빗 변수 반환하는 getter 함수
    def set_radius( self, radius ) :
        self.__radius = radius # 매개변수 값을 프라이빗 변수에 저장하는 setter 함수
    # setter and getter 자동생성
    @property
    def radius2( self ) :
        return self.__radius2
    @radius2.setter
    def radius2( self, value ) :
        self.__radius2 = value
circle = Circle( 10 ) 
# print( circle.__radius ) # 클래스 외부에서 프라이빗 변수 사용 안됨
print( circle.get_radius() ) # 10
circle.set_radius( 20 )
print (circle.get_radius() ) # 20

print( circle.radius2 )

# p.497 상속의 활용
class Parent :
    def __init__(self):
        self.value = "테스트"
        print("init 메소드 호출")
    def test( self ) :
        print("test()메소드 호출")

class Child( Parent ) : 
    def __init__(self):
        super().__init__()      # super() : 부모 인스턴스를 가리킴.
        print( 'child init 메소드 호출')
    def test( self ) :
            print("test()메소드 호출")
child = Child() 
child.test()
