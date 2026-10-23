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
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
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
print( student[0] == student[1] )   # == 대신에 __eq__함수가 실행됨, True
print( student[0] != student[1])    # False 
print( student[0] > student[1])
print( student[0] >= student[1])
print( student[0] < student[1])
print( student[0] <= student[1])
