def remove_duplicates(lst):
    different = []

    for i in lst:
        if i not in different:
            different.append(i)
    return different


n = list(input("Enter the elements of the list: ").split())

print("List without duplicates are: ", remove_duplicates(n))