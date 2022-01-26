from collections import Counter
n, k = map(int, input().split())
c, v = Counter(map(int, input().split())), 0
while c[k] < n:
    for i in range(k - 1, 0, -1):
        if c[i]:
            c[i] -= 1
            c[i + 1] += 1
    v += 1
print(v)
