# lst = []

# n = int(input("Enter number of elements : "))

# for i in range(0,n):
#     ele = int(input())
    
    
#     lst.append(ele)
    

# a1 = lst.Reverse()

# print(sum(a1+lst))


l1 = list(map(int,input().split()))
a=l1[::-1]
s =[str(i) for i in l1]
res = int("".join(s))
s2=[str(i) for i in a ]
res1 = int("".join(s2))
sum = res + res1
ans =[int(i) for i in str(sum)]
print(ans)
