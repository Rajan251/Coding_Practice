class Rectangle():
    def __init__(self):
        
        self.length = int(input("enter the length :"))
        self.width = int(input("enter the length:"))

    def rectangle_area(self):
        self.Area = self.length*self.width
        # return self.length*self.width
        print(self.Area)
        

newRectangle = Rectangle()
newRectangle.rectangle_area()

# print(newRectangle.rectangle_area())

