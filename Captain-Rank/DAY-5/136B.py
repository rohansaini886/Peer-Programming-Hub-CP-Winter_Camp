a,b = map(int,input().split())
ans=0
k=1
while a or b:
    ans+=k*(((b%3)-(a%3))%3)
    a//=3
    b//=3
    k*=3
print(ans)
