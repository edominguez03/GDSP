shopping = ["Milk", "Bread", "Eggs"]

print(shopping)
 
shopping.append("cheese")
print(shopping)

shopping[1] = "butter"
print(shopping)

shopping.remove("Eggs")
print(shopping)

for groceries in shopping:
    print(groceries)