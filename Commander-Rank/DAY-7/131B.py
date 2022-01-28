d={}
input()
k=0
for i in map(int,input().split()):k+=d.get(-i,0);d[i]=d.get(i,0)+1
print(k)
