# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1


    def turn_off(self):
        self.is_on = False


    def turn_on(self):
        self.is_on = True
        

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no


    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")


def main():
    my_tv = TV()            # 1

    my_tv.show_status()     # 2
    my_tv.turn_on()         # 3
    my_tv.show_status()     # 4
    my_tv.set_channel(5)    # 5
    my_tv.show_status()     # 6
    my_tv.turn_off()        # 7
    my_tv.show_status()     # 8


if __name__ == "__main__":
    main()
