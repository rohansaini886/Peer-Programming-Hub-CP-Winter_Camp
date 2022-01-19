n=int(input())
l=[int(x) for x in input().split()]
d={}
for i in range(n):
  d[l[i]]=i+1
m=int(input())
qs=[int(x) for x in input().split()]
lt=rt=0
for q in qs:
  lt+=d[q]
  rt+=n+1-d[q]
print(lt,rt)
  
