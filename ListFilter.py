def filter_even(L1):
    even = []

    for num in L1:
        if num % 2 ==0:
            even.append(num)

    return even


n = int(input("Enter the number of elements in the list: "))

L1 = []

for i in range(n):

    value = int(input(f"Enter elements {i + 1}: "))

    L1.append(value)

print("Even elements in the list are: ", filter_even(L1))