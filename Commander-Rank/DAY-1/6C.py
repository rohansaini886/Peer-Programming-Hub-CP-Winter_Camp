n = int(input())
bars = list(map(int, input().split()))
ta = 0
tb = 0
a = 0
b = 0
for cont in range(0,n):
    if ta <= tb:
        ta += bars[a]
        a += 1
    else:
        tb += bars[-b-1]
        b += 1
print(a, b)
