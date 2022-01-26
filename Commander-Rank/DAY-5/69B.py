n, m = map(int, input().split())
v, w = [None] * n, []
for i in range(m):
    l, r, t, c = map(int, input().split())
    w.append(c)
    for j in range(l - 1, r):
        if not v[j] or t < v[j][0]:
            v[j] = (t, i)
print(sum(w[x[1]] for x in v if x))
