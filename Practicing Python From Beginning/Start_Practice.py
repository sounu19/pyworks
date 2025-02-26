'''class Parent:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class Child(Parent):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.BornYear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the world in", self.BornYear)
x = Child("Mazhar", "Farid", 1991)
x.welcome()'''


'''class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x =self.a
        self.a += 1
        return x
MyClass = MyNumbers()
MyIter = iter(MyClass)

print(next(MyIter))
print(next(MyIter))'''

'''class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a<=10:
            x=self.a
            self.a +=1
            return x
        else:
            raise StopIteration

MyClass = MyNumbers()
MyIter = iter(MyClass)

for x in MyIter:
    print(x)'''

'''class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive...!!!")
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail...!!!")

class Plane(Vehicle):
    def move(self):
        print("Fly...!!!")

Car1 = Car("Suzuki", "Mehran")
Boat1 = Boat("Ibiza","Touring 20")
Plane1 = Plane ("Boeing", "747")

for x in (Car1, Boat1, Plane1):
    print(x.brand)
    print(x.model)
    x.move()'''


'''import datetime

x = datetime.datetime(2025, 12, 18)
print(x.strftime("%B"))'''
