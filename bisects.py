import bisect
number = 5


a = [1,2,3,4,6,7,8,9,122]

print(bisect.bisect(a,number)) # fot check the value of the list
bisect.insort(a,number)
print(a)