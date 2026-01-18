employees = [
    "SMITH Lucy",
    "JONES Janet",
    "LEE Jerry",
    "JACKSON Peter",
    "JOHNSON Rick",
    "LEWIS Terry",
    "CLARKE Robin"
]

emp = list(filter(lambda x: x[0] == "J", employees))

print("People whose surnames start with the letter 'J': ")
for employee in emp:
    print(employee)