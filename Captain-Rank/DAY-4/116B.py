n, m = map(int, input().split())
s, a, b = 0, '.' * (m + 2), '.' + input() + '.'

def f(a, b, c):
    return sum(b[i] == 'W' and 'P' in [a[i], c[i], b[i - 1], b[i + 1]] for i in range(1, m + 1))

for i in range(1, n):
    c = '.' + input() + '.'
    s += f(a, b, c)
    a, b = b, c
print(s + f(a, b, '.' * (m + 2)))
