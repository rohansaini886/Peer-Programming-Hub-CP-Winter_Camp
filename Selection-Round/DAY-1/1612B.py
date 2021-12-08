for i in range(int(input())):
    n, a, b = map(int, input().split())
    p = [a]
    for j in range(n, 0, -1):
        if j != a and j != b:
            p.append(j)
    p.append(b)
    if(len(p) == n and min(p[0:n//2]) == a and max(p[n//2:n]) == b):
        print(*p)
    else:
        print(-1)
