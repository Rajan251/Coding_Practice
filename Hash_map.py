# def get_hash(key):
#     sum = 0
#     for c in key:
#         sum +=ord(c)
#     return sum % 100
# get_hash('march 9')

a=input("Enter your file name :")

v=a.split(".")
print(repr(v[-1]))
