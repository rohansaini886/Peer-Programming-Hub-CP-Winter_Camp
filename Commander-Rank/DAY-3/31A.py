n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        for k in range(n):
            if j != k and a[j] + a[k] == a[i]:
                print(i + 1, j + 1, k + 1)
                exit()
print(-1)
