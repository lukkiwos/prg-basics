person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone": {"landline": "123444321", "mobile": "777888999"}
}

print(f"1. {person["name"]}")                   # 1
print()

print(f"2. {', '.join(person["hobby"])}")       # 2
print()
                                                
for key,value in person.items():                # 3
    print(f"{key} : {value}")
print()

person["surname"] = "Nowak"                     # 4

person["married"] = False                       # 5

person["gender"] = "male"                       # 6

person["hobby"].append("bicycle")               # 7

person["phone"]["work"] = ("313131444")         # 8
print()
print()

for key,value in person.items():
    print(f"{key} : {value}")