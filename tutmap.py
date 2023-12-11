
from functools import reduce
h1 = [1,2,3,4,6,5,7]
sq = []

for item in h1:
    sq.append(item**2)

print(sq)

def square(n):
    return n**2
# it will print the genrated location of the functions
s = map(square,h1) 
s = list(map(square,h1))
print(s)
# this filter function is used to filter value from list and and data to check in program
def greater_than_2(n):
    if n>2:
        return True
    else:
        return False

greater_th_2  = list(filter(function(greater_th_2,h1)))
print(greater_th_2)


def sum_num(a,b):
    return a + b


lil = reduce(sum_num,[1,2,3,4,5])
print(lil)