n = eval(input("Enter the number: "))
for i in range(1, n):
    for sep in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        print("*", end="")
    print()
