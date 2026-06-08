class Student:
    def __init__(self,name,age,student_no,course):
       self.name = name
       self.age = age
       self.student_no = student_no
       self.course = course

    def study(self,unit):
        print(f"{self.name} studies {unit}")


    def exam(self,time):
        print(f"{self.name} passes exams {grade}")

    def pursue(self,course):
        print(f"{self.name} Pursue Two courses{course}")

    def eats(self,food):
        print(f"{self.name}eats {food}")

    def get_details(self):
        print("User Details")
        print(f"Name:{self.name}-Student No:{self.student_no} -Course:{self.course}")
        print("---------------")

#object 1
student1=Student("John","12","T56","Criminology")
print(type(student1))
print(student1)
print(student1.name)
print(student1.student_no)
print(student1.course)
student1.study()
student1.exam()
student1.pursue()
student1.eats()
student1.get_details()


#object 2
student2=Student("Alice","25","T78","Cosmetology")
print(type(student2))
print(student2)
print(student2.name)
print(student2.student_no)
print(student2.course)
student2.study()
student2.exam()
student2.pursue()
student2.eats()
student2.get_details()
