logged_in = input("Are you logged in?.")
if logged_in == "yes":
    
    subscription = input("Do you have a subscription? ")
    if subscription == "yes":
        print("Access granted.")
    else:
        print("Subscription required.")

else:
    print("Please log in first.")
    
