class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"The distance was: {self.distance}, rate was: {self.rate_per_km} and fare is: {self.fare}")

def main():
    # your program
    taxi_1 = TaxiRide(2)
    taxi_2 = TaxiRide(3)

    taxi_1.calculate_fare(24)
    taxi_2.calculate_fare(32)

    taxi_1.print_receipt()
    taxi_2.print_receipt()

if __name__ == "__main__":
    main()