
print("\n\n========== 예제 2.38 ==========")
def english():
    print("영어과입니다.")
english()


print("\n\n========== 예제 2.39 ==========")
def math(student_name):
    print(student_name)
math("토마스")


print("\n\n========== 예제 2.40 ==========")
def academy(student_name1, student_name2, student_name3):
    print(student_name1)
    print(student_name2)
    print(student_name3)

academy("토마스", "에디슨", "빌리")


print("\n\n========== 예제 2.41 ==========")
def english(help):
    help()

def help():
    print("도와주러 왔습니다.")

english(help)


print("\n\n========== 예제 2.42 ==========")
def math():
    name = "광수"
    return name

who = math()
print(who)


print("\n\n========== 예제 2.43 ==========")
def multi():
    return "a", "b"

a, b = multi()
result = multi()
print(result)


print("\n\n========== 예제 2.44 ==========")
class B_school():
    def __init__(self):
        print("b대학교 초기화")

B_school()


print("\n\n========== 예제 2.45 ==========")
class A_school():
    def __init__(self):
        print("초기화, 생성자")
        self.student1_name = None
        self.student2_name = None

        print(dir(self))

A_school()


print("\n\n========== 예제 2.46 ==========")
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


print("\n\n========== 예제 2.47 ==========")
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


print("\n\n========== 예제 2.48 ==========")
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
        print("%s을 물려받았습니다." % self.home())

class ChildB(Parent):
    def __init__(self):
        super().__init__()
        print("자식B")

        print("부모의 돈 %s" % self.money)
        print("%s을 물려받았습니다." % self.home())

ChildA()
ChildB()
