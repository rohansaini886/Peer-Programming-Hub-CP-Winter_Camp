input()
x=list(map(int,input().split()))
k=set(x);c=0
for i in k:
    c+=x.count(i)//2
print(c//2)
