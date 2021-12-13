for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split(" ")))
    is_true = False
    for i in range(1, n):
        if l[i] >= l[i-1]:
            is_true = True
            break
    if is_true:
        print("YES")
    else:
        print("NO")
