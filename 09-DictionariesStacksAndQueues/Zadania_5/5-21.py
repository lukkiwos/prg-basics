import json

# Dictionary describing the favorite movie
favourite = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "genre": "Science Fiction",
    "rating": 8.8
}

# Write dictionary to JSON file
with open("favourite.json", "w", encoding="utf-8") as file:
    json.dump(favourite, file, indent=4)

print("Favourite movie data saved to: favourite.json")