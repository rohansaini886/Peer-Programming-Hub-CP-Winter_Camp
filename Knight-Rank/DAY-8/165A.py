n=int(input())
x=[list(map(int,input().split()))for i in range(n)]
a=0
for i in range(n):
 l,r,u,d=[0]*4
 for j in range(n):
  if i==j:continue
  if x[i][0]==x[j][0]:
   if x[i][1]<x[j][1]:u=1
   else:d=1
  if x[i][1]==x[j][1]:
   if x[i][0]<x[j][0]:l=1
   else:r=1
 a+=l+r+u+d==4
print(a)
