n = int(input())
u = 7 - int(input())

def f():
    for i in range(n):
        x, y = map(int, input().split())
        if u in [x, y, 7 - x, 7 - y]: return 1
    return 0
print('YNEOS'[f() :: 2])
