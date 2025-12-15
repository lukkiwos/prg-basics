person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}


print(f"\n1 - {person['name']}\n")                      # 1

print(f"2 - {person['hobby']}\n")                       # 2

for key,value in person.items():                        # 3
    print(f"\n3 - {key} - {value}\n")

person["surname"] = "Nowak"                             # 4

person["married"] = False                               # 5

person["gender"] = "Male"                               # 6

person["hobby"].append('bicycle')                       # 7

person["phone"]["work"] = ('313131444')                 # 8

print(person)                                           # 9