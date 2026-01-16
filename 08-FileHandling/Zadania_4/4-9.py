import csv

file_name = "it_company.csv"

print("GRAPHIC DESIGNERS")
print("=================")

with open(file_name, 'r', encoding="utf-8") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        last_name = row[0]
        first_name = row[1]
        job_title = row[2]
        email = row[3]

        if job_title == "Graphic Designer":
            print(f"{last_name} {first_name}, {email}")