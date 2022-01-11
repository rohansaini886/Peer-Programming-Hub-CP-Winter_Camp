a = list(input().split())
b = list(input().split())

t = 0

for i in range(3):
  if a[i] == b[i]:
    t += 1

if t > 0:
  print("YES")
else:
  print("NO")
