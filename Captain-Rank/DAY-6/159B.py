n,m=tuple(map(int,input().split()))
 
cap1=[0]*1001
cap2=[0]*1001
cnt=[[0]*1001 for y in range(1001)]
for k in range(n):
    x,y=tuple(map(int,input().split()))
    cap1[y]+=1
    cnt[x][y]+=1
ans=0
for k in range(m):
    x,y=tuple(map(int,input().split()))
    cap2[y]+=1
    if cnt[x][y] > 0:
        cnt[x][y]-=1
        ans +=1
 
print(sum(min(cap1[y],cap2[y]) for y in range(1001)),ans)
