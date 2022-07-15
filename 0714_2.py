# class 정의
class Student:#클래스 명은 대문자
    #생성자 정의
    def __init__(self,hackbun,dept):
        self.hackbun = hackbun
        self.dept = dept

    #메소드
    def printAll(self):
        print('학생학번: ',self.hackbun)
        print('학생학과: ',self.dept)


#학생 객체 생성
student1=Student(2022071,'컴퓨터공학과')
student1.printAll()
student2=Student(2011111,'정보보안학과')
student2.printAll()


# student1 = Student(2022071,'컴퓨터공학과') #생성자 호출: 객체 생성역할
# print('학생학번: ',student1.hackbun)
# print('학생학과: ',student1.dept)

# student2 = Student()
# student2.hackbun = 20111111
# student2.dept = '정보보안학'
# print('학생학번: ',student1.hackbun)
# print('학생학과: ',student2.dept)



