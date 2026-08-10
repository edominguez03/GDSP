movie = {"title": "Star Wars",
         "year": 1977,
         "director": "George Lucas"}

print(movie.get("title"))
print(movie.get("genre"))
print(movie.get("genre", "genre unknown"))

movie["genre"] = "Science Fiction"
print(movie.get("genre", "genre unknown"))
