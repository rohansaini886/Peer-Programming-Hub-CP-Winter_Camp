n, x, y = map(int, input().split())
n //= 2
print('NO' if n <= x <= n + 1 and n <= y <= n + 1 else 'YES')
