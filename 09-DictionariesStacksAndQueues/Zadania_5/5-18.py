import json

with open("dogs.json", 'r', encoding="utf-8") as file:
    data = json.load(file)


for dogs in data:
    if dogs["age"] < 5:
        for key, value in dogs.items():
            print(f"{key} : {value}")
        print()