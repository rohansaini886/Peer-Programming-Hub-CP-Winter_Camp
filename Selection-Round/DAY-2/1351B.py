for _ in range(int(input())):
    a, b = map(int, input().split(" "))
    x, y = map(int, input().split(" "))
    
    if a > b:
        t = a
        a = b
        b = t
    if x > y:
        t = x
        x = y
        y = t
    
    if a + x == b and a + x == y:
        print("YES")
    else:
        print("NO")
