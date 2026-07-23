age = int(input("What is your age? "))
ticket = input("Do you have a ticket? ")
if age >= 18 and ticket == "yes":
    print("You may enter.")
else:
    print("Entry denied")
