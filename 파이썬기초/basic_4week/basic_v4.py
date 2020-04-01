# 함수
def english():
    print("영어과 입니다.")
english()

##################################
def stock(student_name):
    print(student_name)
stock("토마스")
##################################

##################################
def stock(student_name1, student_name2, student_name3):
    print(student_name1)
    print(student_name2)
    print(student_name3)

stock("토마스", "에디슨", "빌리")
##################################

##################################
def english(help):
    help()

def stock():
    print("도와주러 왔습니다.")
english(stock)
##################################

##################################
def math():
    name = "광수"
    return name

who = math()
print(who)
##################################

##################################
def multi():

    return "a", "b"

a, b = multi()
result = multi()
print(result)
##################################


#클래스
class B_school():
    def __init__(self):
        print("b대학교 초기화")

B_school()


##################################
class A_school():
    def __init__(self):
        print("초기화, 생성자")
        self.student1_name = None
        self.student2_name = None

        print(dir(self))

A_school()
##################################

##################################
class A_school():
    def __init__(self):
        print("초기화, 생성자")
        self.student1_name = None

        b = self.math()
        print("수학과 학생 %s" % b)

    def math(self):
        self.student1_name = "영수"
        name = self.student1_name

        return name
##################################


##################################
class B_school():
    def __init__(self):
        print("b대학교 초기화")

        self.school_name = "b학교"


class A_school():
    def __init__(self):
        print("초기화, 생성자")
        self.student1_name = None

        b = self.math()
        print("수학과 학생 %s" % b)

        b_school = B_school()
        print(b_school.school_name)


    def math(self):
        self.student1_name = "영수"
        name = self.student1_name

        return name

A_school()
##################################

##################################
class Parent():
    def __init__(self):
        print("부모입니다.")

        self.money = 50000000

    def home(self):
        return "부모의 집"


class ChildA(Parent):
    def __init__(self):
        print("자식A")

        print("부모의 돈을 물려받을 수 없습니다.")
        print("%s을 물려 받았습니다." % self.home())


class ChildB(Parent):
    def __init__(self):
        super().__init__()
        print("자식B")

        print("부모의 돈 %s" % self.money)
        print("%s을 물려 받았습니다." % self.home())

ChildA()
ChildB()
##################################
