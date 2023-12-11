
from collections import defaultdict

def beauty(n, m, s, x, y):
    letter_count = defaultdict(int)
    for letter in s:
        letter_count[letter] += 1

    path_max_count = defaultdict(int)
    for i in range(m):
        max_letter_count = 0
        for j in range(x[i], y[i]+1):
            if letter_count[s[j-1]] > max_letter_count:
                max_letter_count = letter_count[s[j-1]]
        path_max_count[max_letter_count] += 1

    max_beauty = max(path_max_count.keys())

    if path_max_count[max_beauty] > 1:
        return -1
    else:
        return max_beauty


n = int(input("Enter the number of nodes: "))
m = int(input("Enter the number of edges: "))
s = input("Enter the string of letters: ")
x = list(map(int, input("Enter the starting nodes for the edges: ").split()))
y = list(map(int, input("Enter the ending nodes for the edges: ").split()))


result = beauty(n, m, s, x, y)


print("The maximum beauty value is:", result)