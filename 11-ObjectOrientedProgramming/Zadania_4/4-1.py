# class definition
class TV:
    def __init__(self):
        self.is_on = False


    def turn_off(self):
        self.is_on = False


    def turn_on(self):
        self.is_on = True
        
    
    def show_status(self):
        if self.is_on:
            print("TV is on")
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


# from tv.py import TV