
# def funcation_1(name,age,rollno):
    
#     print("The name of the student is ",name,"and age is ",age,"and rollno is ",rollno)

# funcation_1("Rajan", 21,88)

# def funcation_2(*arg):
#     print(type(arg))
#     if(len(arg)==3):
#         print("The name of the student is",arg[0],"and age is ",arg[1],"and roll no is",arg[2])
#     else:
#         print("The name of the student",arg[0],"and age is",arg[1])

# funcation_2("Raje",24,88)

def printmarks(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)

marklist = {"Harry" : 100,"Rohan das" : 97,"Aman Bhateja" :91,"The Programmer" :80, "Mani Verma":89}

printmarks(**marklist)