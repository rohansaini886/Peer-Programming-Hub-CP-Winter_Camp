n, a = int(input()), list(map(int, input().split()))
s, o = sum(a), [x for x in a if x % 2]
if s % 2:
    print(s)
elif o:
    print(s - min(o))
else:
    print(0)
