class Vehicle :
    def __init__(self,name,max_speed,mileage):
        self.name = name 
        self.max_speed = max_speed
        self.mileage = mileage

car1 = Vehicle("Honda",180,15000)
print(car1.name)
print(car1.max_speed)
print(car1.mileage)

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    

School_Bus = Bus("School Volve" , 180 , 12)
print(f"Name: {School_Bus.name} ,Speed : {School_Bus.max_speed} , mileage: {School_Bus.mileage}")


class Parent1:
    def method1(self):
        print('Method from Parent 1 ')

class Parent2:
    def method2(self):
        print('Method from Parent 2 ')

class Child(Parent1,Parent2):
    pass

c = Child()
c.method1()
c.method2()