summa = 0

X = int(input())
N = [int(i) for i in input().split()]
value = int(input())

for i in range(value):
    shoes = [int(i) for i in input().split()]
    if shoes[0] in N:
        summa += shoes[1]
        N.remove(shoes[0])

print(summa)