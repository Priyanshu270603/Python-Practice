age = int (input("Enter your age: "))

if age < 0:
    print("Invalid age.")
elif age <=12:
    print("Children : Price for the ticket is $5")

elif 12 <= age <= 17:
    print("Teenager : Price for ticket is $8.")

elif 18 <= age <= 64:
    print("Adults : Price for ticket is $12.")

elif age >= 65:
    print("Seniors : Price for ticket is $6.")

else:
    print("Error")