import sys

def valid(n):
    return len(set(str(n))) == len(str(n))

a,b = list(map(int,input().split()))

for i in range(a,b+1):
    if valid(i):
        print(i)
        sys.exit(0)

print(-1)
