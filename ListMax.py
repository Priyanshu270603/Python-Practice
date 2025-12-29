def find_max(L1):
    max = L1[0]

    for num in L1:
        if num > max:
            max = num

    return max

n = list(map(int, input("Enter the elements of the list: ").split()))



print("Max value is:", find_max(n))

