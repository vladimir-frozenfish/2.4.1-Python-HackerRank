"""In this challenge, you will be given 2 integers, n and m.
There are n words, which might repeat, in word group A.
There are m words belonging to word group B.
For each m words, check whether the word has appeared in group A or not.
Print the indices of each occurrence of m in group A.
If it does not appear, print -1."""

from collections import defaultdict

n, m = map(int, input().split())

n_dict = defaultdict(list)
for i in range(n):
    n_dict[input()].append(i+1)

m_list = []
for i in range(m):
    m_list.append(input())

for i in m_list:
    if n_dict[i]:
        print(*n_dict[i])
    else:
        print(-1)
