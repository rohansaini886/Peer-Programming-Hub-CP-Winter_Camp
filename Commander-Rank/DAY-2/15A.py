n, t = map(int, input().split())
k = 2 * n
p = [0] * k
for i in range(0, k, 2):
    a, b = map(int, input().split())
    p[i] = a - b / 2
    p[i + 1] = p[i] + b
p.sort()
p = [p[i + 1] - p[i] for i in range(1, k - 1, 2)]
s = 2
for i in p:
    if i > t: s += 2
    elif i == t: s += 1
print(s)
