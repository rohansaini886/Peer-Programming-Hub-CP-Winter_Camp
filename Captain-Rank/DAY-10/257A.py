n, m, k = map(int, input().split())
for i, a in enumerate(sorted(map(int, input().split()), reverse=True)):
    if k >= m:
        print(i)
        exit()
    k += a - 1
print(n if k >= m else -1)
