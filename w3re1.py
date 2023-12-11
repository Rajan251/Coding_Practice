# # # import math
# # # # import sys
# # # # import datetime
# # # # print(sys.version)

# # # # print(sys.version_info)

# # # # now = datetime.datetime.now()
# # # # print ("Current date and time : ")
# # # # print (now.strftime("%Y-%m-%d %H:%M:%S"))

# # # print("Enter your radius:")
# # # r = int(input())
# # # area =  3.14 * r**2
# # # print(area)
 
# #  # take name and reverse print name


# # #Python: Generate a list and tuple with comma-separated numbers

# # # value = input("input some comma seprated numbers :")
# # # list = value.split()
# # # tuple = tuple(list)
# # # print('list : ' ,list)
# # # print('tuple : ' , tuple)

# # #Python: File extension

# # a = input("Enter the file name:")
# # f_extension= a.split('.')
# # print("File extension " + repr(f_extension[-1]))

# Python: Display the first and last colors from a given list

# col = ["red","Green","white","blue"]
# print("%s %s " % (col[0],col[-1]))


# Python: Display a sample examination schedule

# examdate = (11,12,2014)
# print("Exam date is:%i/%i/%i "%examdate)

#Python: Input an integer (n) and computes the value of n+nn+nnn

# a = input("enter the integer value :")
# n1= int("%s"% a)
# n2=int("%s%s"% (a,a))
# n3=int("%s%s%s"% (a,a,a))
# print(n1+n2+n3)


def my_function(a):
  return a[::-1]


m = input("Enter your name:")
# v=my_function("I am the king")
v=my_function(m)


print(v)


