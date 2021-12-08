for _ in range(int(input())):
    a, b = map(int, input().split(" "))
    if a == 1 and b == 1:
        print(0)
    elif a == 1 or b == 1:
        print(1)
    else:
        print(2)
