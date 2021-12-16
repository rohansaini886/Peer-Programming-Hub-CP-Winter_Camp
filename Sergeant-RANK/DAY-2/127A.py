import math 
n, k = map(int, input().split(" "))
x_sum = 0
x_prev = 0
y_sum = 0
y_prev = 0
l = []
for i in range(n):
    if i == 0:
        x_prev, y_prev = map(int, input().split(" "))
    else:
        x, y = map(int, input().split(" "))
        x_sum = x_prev - x
        y_sum = y_prev - y
        d = math.sqrt((x_sum ** 2) + (y_sum ** 2))
        l.append(d)
        x_prev = x
        y_prev = y
print(round((sum(l) / 50) * k, 9))
