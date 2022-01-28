I =lambda : list(map(int, input().split()))
n,m = I()
G = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    inp = I()
    G[inp[0]-1][inp[1]-1] = 1
    G[inp[1]-1][inp[0]-1] = 1
kicked = 0
while 1:
    candidates = [i for i in range(n) if sum(G[i]) == 1]
    if len(candidates) == 0:
        break
    for i in range(n):
        for c in candidates:
            G[i][c],G[c][i] = 0,0
    kicked += 1
print(kicked)
