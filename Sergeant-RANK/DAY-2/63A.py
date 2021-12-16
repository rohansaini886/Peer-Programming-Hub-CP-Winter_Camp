n = int(input())
l = []
for i in range(n):
    l.append(input().split(" "))
queue = []  
for i in range(n):
    if l[i][1] == "rat":
        queue.append(l[i][0])
for i in range(n):
    if l[i][1] == "woman" or l[i][1] == "child":
        queue.append(l[i][0])
for i in range(n):
    if l[i][1] == "man":
        queue.append(l[i][0])
for i in range(n):
    if l[i][1] == "captain":
        queue.append(l[i][0])

for i in queue:
    print(i)
