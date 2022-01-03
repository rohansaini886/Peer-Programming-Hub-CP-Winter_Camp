n=int(input())

l=list(map(int,input().split()))

i=0
while n>l[i]:
     n-=l[i]
     i=(i+1)%7
print(i+1)
