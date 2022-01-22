n, vb, vs = map(int, input().split())
x = list(map(int, input().split()))
xu, yu = map(int, input().split())
xv, dv, tv = 0, 10 ** 6, 10 ** 6
for i in range(1, n):
    d = ((xu - x[i]) ** 2 + yu ** 2) ** 0.5
    t = x[i] / vb + d / vs
    if t < tv or (t == tv and d < dv):
        xv, dv, tv = i + 1, d, t
print(xv)
