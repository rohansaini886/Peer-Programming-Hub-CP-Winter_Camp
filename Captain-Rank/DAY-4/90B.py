n, m = map(int, input().split())

C = []

rows = [[0]*(ord('z')+1) for _ in range(n)]
cols = [[0]*(ord('z')+1) for _ in range(m)]

for _ in range(n):
    C += [list(input())]

for i in range(n):
    for j in range(m):
        rows[i][ord(C[i][j])] += 1
        cols[j][ord(C[i][j])] += 1

for i in range(n):
    for j in range(m):
        if rows[i][ord(C[i][j])] > 1 or cols[j][ord(C[i][j])] > 1:
            C[i][j] = 0

result = []

for i in range(n):
    for j in range(m):
        if C[i][j] != 0:
            result += [C[i][j]]

print("".join(result))
