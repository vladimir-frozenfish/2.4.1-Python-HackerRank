import math

complex_number = input()[:-1]
minus = complex_number[1:].find('-') + 1
if minus:
    X = float(complex_number[0:minus])
    Y = float(complex_number[minus:])
else:
    plus = complex_number[1:].find('+') + 1
    X = float(complex_number[0:plus])
    Y = float(complex_number[plus:])

R = (X ** 2 + Y ** 2) ** 0.5

if R == 0: alpha = None

if X > 0 and Y > 0: alpha = math.atan2(Y, X)
if X < 0 and Y > 0: alpha = math.pi - math.atan2(Y, X)
if X < 0 and Y < 0: alpha = math.atan2(Y, X)
if X > 0 and Y < 0: alpha = math.atan2(Y, X)

if X == 0 and Y > 0: alpha = math.pi / 2
if X == 0 and Y < 0: alpha = - math.pi / 2
if X > 0 and Y == 0: alpha = 0
if X < 0 and Y == 0: alpha = math.pi

print(R)
print(alpha)
