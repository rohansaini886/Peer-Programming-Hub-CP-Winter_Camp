import sys
sys.stdin=open('input.txt', 'r')
sys.stdout=open('output.txt', 'w')
I=lambda:map(int,input().split())
n,k=I()
print(sum(max(x%k,x-3*k)for x in I()))
