# 1. 클래스 만들기
# class 클래스명 :
class Student :
    pass
student = Student()
students = {
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
}

# 2. 생성자 / 메소드
class Student2 :
    # def __init__(self, 멤버변수1, 멤버변수2, 멤버변수3 ) :
    #     self.멤버변수1 = 멤버변수1
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    # def 메소드명(self, 매개변수)
    def get_sum( self ) :
        return self.korean + self.math + self.english + self.science
    def get_average( self ) :
        return self.get_sum() / 4
    def to_string( self ) :
        return "{} \t {} \t {}".format( self.name, self.get_sum, self.get_average)
# 생성자 이용한 인스턴스 생성, py : 클래스명( 인수, 인수, 인수 )
# Student2 s = new Student("유재석", 10, 20, 30, 40 ) <- JAVA
students = [
    Student2("윤인성", 87, 98, 88, 85),
    Student2("윤인성", 87, 98, 88, 85),
    Student2("윤인성", 87, 98, 88, 85),
    Student2("윤인성", 87, 98, 88, 85),
    Student2("윤인성", 87, 98, 88, 85),
    Student2("윤인성", 87, 98, 88, 85)
]
# 인스턴스내 멤버변수 호출
print( students[0].korean )     # 87
print( students[1].get_sum())