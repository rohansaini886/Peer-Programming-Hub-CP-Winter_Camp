a,b=map(int,input().split())
print(a+b-1)
for i in range(1,a+b):
    print (max(1,i-b+1),min(i,b))
