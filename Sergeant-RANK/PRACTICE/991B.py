n = int(input())
l = list(map(int, input().split(" ")))
count = 0
for i in range(n):
    if len(l) == 1:
        if l[i] == 5:
            print(0)
        else:
            print(1)
    elif sum(l) / n >= 4.5:
        print(count)
        break
    else:
        l[l.index(min(l))] = 5
        count += 1
