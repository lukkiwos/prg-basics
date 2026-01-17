class Phone():
    def __init__(self, brand, battery_level):
        self.brand = brand
        self.battery_level = battery_level
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Phone is now ON")

    def charge(self):
        self.battery_level = 100
        print("Phone is fully charged")

    def make_call(self, number):
        if self.is_on and self.battery_level > 0:
            print(f"Calling {number}...")
            self.battery_level -= 10
        else:
            print('Cannot make a call')


def main():
    my_phone = Phone("Xiaomi", 80)

    print(f"Brand: {my_phone.brand}")
    print(f"Battery level: {my_phone.battery_level}")
    print(f"Is on: {my_phone.is_on}")

    my_phone.turn_on()
    my_phone.make_call("342-531-684")
    my_phone.charge()

    print(f"Batter level after charging: {my_phone.battery_level}")


if __name__ == "__main__":
    main()