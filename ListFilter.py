def filter_even(lst):
    even = []

    for num in lst:
        if num % 2 == 0:
            even.append(num)

    return even

n = list(map(int, input("Enter the elements: ").split()))

print("The entered list is: ", n)

print("The even elements in the list are: ", filter_even(n))