import csv

province_count = {}

province_letters = {}

with open("province.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        letter = row["Letter"]
        name = row["Name"]
        province_letters[letter] = name
        province_count[name] = 0  



with open("vehicle.txt", encoding="utf-8") as file:
    for line in file:
        plate = line.strip()
        if plate:  
            first_letter = plate[0]
            if first_letter in province_letters:
                province = province_letters[first_letter]
                province_count[province] += 1



for province, count in province_count.items():
    print(province, ":", count)