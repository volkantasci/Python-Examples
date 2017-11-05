a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a > b:
    if a > c:
        if b > c:
            print("c < b < a")
        elif b == c:
            print("c = b < a")
        else:
            print("b < c < a")
    elif a == c:
        print("b < c = a")
    else:
        print("b < a < c")

elif a == b:
    if a > c:
        print("c < b = a")
    elif a == c:
        print("a = b = c")
    else:
        print("a = b < c")

else:
    if a > c:
        print("c < a < b")
    elif a == c:
        print("a = c < b")
    else:
        if b > c:
            print("a < c < b")
        elif b == c:
            print("a < b = c")
        else:
            print("a < b < c")
