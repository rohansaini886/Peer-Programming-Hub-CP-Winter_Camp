n = int(input())
l = []
for i in range(n):
    t = input().split(" ")
    if t in l:
        continue
    else:
        l.append(t)
        
print(len(l))
