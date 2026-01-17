class TaxiRide:
    def __init__(self, distance, rate):
        self.rate = rate # value in € (e.g. €2)
        self.distance = distance
        self.fare = 0


    def calculate_fare(self):
        self.fare = self.distance * self.rate
        
        return self.fare


    def print_receipt(self):
        print("----- TAXI RECEIPT -----")
        print(f"Distance: {self.distance} km")
        print(f"Rate: {self.rate} per km")
        print(f"Fare: {self.fare}")
        print("------------------------")


def main():
    
    ride1 = TaxiRide(12, 3.50)
    ride1.calculate_fare()
    ride1.print_receipt()

    
    ride2 = TaxiRide(7.5, 4.00)
    ride2.calculate_fare()
    ride2.print_receipt()



if __name__ == "__main__":
    main()
