
class Student:
    def __init__(self): # convert into constructor do not need to call it
    # def setdata(self): # need to call in program
        self.name=input("Enter Name:")
        self.roll=int(input("Enter Roll:"))
        self.per=float(input("Enter Percentage:"))
    
    def display(self):
        print(f"Name:{self.name}")
        print(f"Name:{self.roll}")
        print(f"Name:{self.per}")

a = Student()
#a.setdata()
a.display()


# class Student:
#     def __init__(self,x,y,a):
#         self.name = x
#         self.roll = y
#         self.per = a
#     def display(self):
#         print(f"name:{self.name}")
#         print(f"name:{self.roll}")
#         print(f"name:{self.per}")

# a =Student("Rajan", 9003, 70)
# a.display()

