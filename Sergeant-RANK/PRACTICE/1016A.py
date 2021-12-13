n, m = map(int, input().split(" "))
l = list(map(int, input().split(" ")))
total = 0
for i in l:
    total += i
    print(int(total // m), end  = " ")
    total = total % m
