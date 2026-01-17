import json

# load saved json data
with open("euro.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# print header
print(f"{'Date':<15}{'Buying Rate':<15}{'Selling Rate'}")
print("=" * 45)

# loop through each rate entry
for item in data["rates"]:
    date = item["effectiveDate"]
    bid = item["bid"]
    ask = item["ask"]
    print(f"{date:<15}{bid:<15}{ask}")
