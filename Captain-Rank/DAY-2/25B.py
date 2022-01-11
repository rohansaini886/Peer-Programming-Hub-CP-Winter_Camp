n=int(input())
s=input()
if n%2==0:
  l=[s[i:i+2] for i in range(0,n,2)]
  print('-'.join(l))
elif n%2!=0:
  l=[s[i:i+2] for i in range(0,n-3,2)]
  l.append(s[n-3:])
  print('-'.join(l))
