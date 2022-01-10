m,n,c=input().split()
m,n=int(m),int(n)
a=['']*m
for i in range(m):a[i]=input()
ans=set()
for i in range(m):
   for j in range(n): 
      if a[i][j]==c:
         for x,y in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
            if x in range(m) and y in range(n) and a[x][y]!='.':ans.add(a[x][y])
print(len(ans-{c}))
