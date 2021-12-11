n = [6,4,24,6,3,63, 63]
n = set(n)
n.discard(max(n))
print(max(n))

x = {5,}
print(min(x))

b = [1, 2, 3]
b = tuple(b)
print(hash(b))