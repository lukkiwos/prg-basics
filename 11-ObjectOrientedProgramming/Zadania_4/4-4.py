# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []


    def turn_off(self):
        self.is_on = False


    def turn_on(self):
        self.is_on = True
 

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no


    def set_channels(self, channels_list):
        self.channels = channels_list


    def show_channels(self):
        if not self.channels:
            print("No channels available")
        else:
            print("Channel list: ")
            for i, channel in enumerate(self.channels, start=1):
                print(f"{i}. {channel}")


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
    my_tv.show_channels()   # 5
    
    my_tv.set_channels([    # 6
        "TVP1",
        "TVP2",
        "Polsat",
        "TVN", 
        "Filmbox",
        "Discovery"
])
    
    my_tv.show_channels()   # 7
    my_tv.show_status()     # 8
    my_tv.turn_off()        # 9


if __name__ == "__main__":
    main()
