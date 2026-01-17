import random

class Thermometer():

    def __init__(self):
        self.is_on = False
        self.temperature = None

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def measure_temperature(self):
        if not self.is_on:
            print("Cannot measure. Thermometer is OFF")
            return
        
        self.temperature = round(random.uniform(34.0, 42.0), 1)
        print(f"Temperature: {self.temperature}C", end="")

        if self.temperature >= 41:
            print(f" CRITICAL TEMPERATURE!!!")
        elif self.temperature >= 37:
            print(f" (fever)")
        else:
            print()


    def display_info(self):
        if self.temperature is None:
            print("No temperature measured yet.")
        else:
            print(f"Current temperature: {self.temperature}")
        


def main():
    my_temp = Thermometer()

    my_temp.turn_on()
    my_temp.measure_temperature()
    my_temp.display_info()
    my_temp.turn_off()


if __name__ == "__main__":
    main()