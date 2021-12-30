r,g,b=map(int,input().split())
f=lambda x:(0--x//2-1)*3
print(max(f(r),1+f(g),2+f(b))+30)
