for x in range(4, 0, -1):
    for y in range(1, x +1):
        print("  ",end=" ")
    for z in range(5, x, -1):
        print("* ",end=" ")
    for a in range(x, 4 - 0):
        print("* ",end=" ")
    print()
for b in range(4):
    for c in range(-2, b,  +1):
        print("  ",end=" ")
    for d in range(3, b, -1):
        print("* ",end=" ")
    for e in range(2, b, -1):
        print("* ",end=" ")
    print()