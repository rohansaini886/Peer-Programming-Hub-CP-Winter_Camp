import math
n = int(input())
l = list(map(int, input().split(" ")))
k = []
for i in l:
    y = str(i)
    if y[0] == "-":
        k.append(i)
        continue
    z = math.pow(i, 0.5)
    z = str(z)
    if z[-1] != "0":
        k.append(i)
print(max(k))
