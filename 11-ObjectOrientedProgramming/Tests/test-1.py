class Car:
    def __init__(self, brand, model, year):
        self.brand = brand      # Object attribute
        self.model = model      # Object attribute
        self.year = year        # Object attribute

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")


car1 = Car("BMW","F90",2022)
car2 = Car("Polonez","Karo",2003)


car1.display_info()
print( car1.brand )
