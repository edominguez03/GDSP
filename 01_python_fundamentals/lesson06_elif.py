score = int(input("Enter your score: "))

if score >= 90:
    print("Excellent")
elif score <= 89 and score >= 70:
    print("Pass")
else:
    print("Needs Improvement")