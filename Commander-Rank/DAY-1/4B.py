d, s = map(int, input().split())
a, b = [0] * d, [0] * d
for i in range(d):
    a[i], b[i] = map(int, input().split())
A, B = sum(a), sum(b)
if A > s or s > B: print('NO')
else:
    s -= A
    i = 0
    while s > 0:
        s += a[i] - b[i]
        a[i] = b[i]
        i += 1
    a[i - 1] += s
    print('YES')
    print(' '.join(str(i) for i in a))
