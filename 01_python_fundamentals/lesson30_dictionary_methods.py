Book = {"title": "El Principito", "author": "Antoine de Saint-Exupéry", "year": 1942, "language": "French"}

for  key in Book.keys():
    print(key)

print()

for value in Book.values():
    print(value)

print()

for key, value in Book.items():
    print(key, ":", value)