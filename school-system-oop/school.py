class Person :
    def __init__(self,name):
        self.name = name 

    def show(self):
        print(f"The person is {self.name}")

class Teacher(Person):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject = subject

    def teach(self):
        print(f"The teacher is {self.name} and the subject they teach is {self.subject}")

class Student(Person):
    def __init__(self, name,grade):
        super().__init__(name)
        self.grade = grade
    

    def study(self):
        print(f"The student is {self.name} and studies in grade {self.grade}")

teacher1 = Teacher("Ketki","Python")

Student1 = Student("Mrunmai",9)

teacher1.show()
teacher1.teach()