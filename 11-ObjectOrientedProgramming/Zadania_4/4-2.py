# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channel = 1


    def turn_off(self):
        self.is_on = False


    def turn_on(self):
        self.is_on = True
        
    
    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel}")
        else:
            print("TV is off")


def main():
    my_tv = TV()            # 1

    my_tv.show_status()     # 2
    my_tv.turn_on()         # 3
    my_tv.show_status()     # 4
    my_tv.turn_off()        # 5
    my_tv.show_status()     # 6


if __name__ == "__main__":
    main()
