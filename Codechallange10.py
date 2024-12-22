for x in range(6, 0, -1):
    for y in range(0, x +1):
        print("  ",end=" ")
    for z in range(6, x, -1):
        print("* ",end=" ")
    for a in range(x, 6 - 0):
        print("* ",end=" ")
    print()
for b in range(6):
    for c in range(-1, b +1):
        print("  ",end=" ")
    for d in range(5, b, -1):
        print("^ ",end=" ")
    for e in range(5, b, -1):
        print("^ ",end=" ")
    print()