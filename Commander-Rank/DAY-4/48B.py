n,m=map(int,input().split())

f = []
for i in range(n):
    f.append(list(map(int,input().split())))

a,b=map(int,input().split())


d=[[0 for i in range(m+1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        d[i][j] = d[i-1][j] + d[i][j-1] + f[i-1][j-1] - d[i-1][j-1]

res = n*m
for j in range(a,m+1):
    for i in range(b, n+1):
        v = d[i][j] + d[i-b][j-a] - d[i-b][j] - d[i][j-a]
        res = min(v, res)

for i in range(a, n+1):
    for j in range(b,m+1):
        v = d[i][j] + d[i-a][j-b] - d[i-a][j] - d[i][j-b]
        res = min(v, res)

print(res)
