try:
    numerator = eval(input("Enter the numerator: "))

    denominator = eval(input("Enter the denominator: "))

    division = numerator / denominator
except ZeroDivisionError:
    print("You cannot divide by zero")

except ValueError:
    print("Please enter valid number only")
