administrator = input("Are you an Administrator? ")
manager = input("Are you a manager? ")

if administrator == "yes" or manager == "yes":
    print("Access granted.")
else:
    print("Access denied")