n,x0=[int(s) for s in input().split()]
left=[0]*n
right=[0]*n
for i in range(n):
    a=[int(s) for s in input().split()]
    a.sort()
    left[i],right[i]=a
a=max(left)
b=min(right)
if a>b:
    print(-1)
else:
    if a<=x0<=b:
        print(0)
    else:
        print(min(abs(a-x0),abs(b-x0)))
