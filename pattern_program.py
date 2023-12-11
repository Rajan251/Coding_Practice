# # for i in range(5+1,0,-1):
# #     for j in range(0,i-1):
# #         print("*",end =" ")
# #     print()

# # * * * * * 
# # * * * * 
# # * * *
# # * *
# # *
# num = int(input("Enter number:"))
# for i in range(0,num):
#     for j in range(0,num-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()

# n= int(input(""))
# for i in range(n-1):
#     print("e"," "*(n),"@"*)

# for i in range(3):
#     print("e"," "*2,"*"*(i+1)) this line is use for only colum value
# print("e"*(3+1),"*"*4) #this is use to print indiviual in the end 

# n=5
# a=0
# for i in range(n-1):
#     print(" "n,"*"*(n+1))

n=int(input("Enter number of rows: "))
for i in range (n,0,-1):
    print((n-i)*' '+i*"*")