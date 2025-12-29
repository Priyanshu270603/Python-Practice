def rotate_list(lst, k):
    if not lst:
        return lst

    k = k % len(lst)
    return lst[-k:] + lst[:-k]


l1 = list(input("Enter the elements of the list: ").split())
k = int(input("Enter the number to rotate the list: "))

print("The rotated list is:", rotate_list(l1, k))
