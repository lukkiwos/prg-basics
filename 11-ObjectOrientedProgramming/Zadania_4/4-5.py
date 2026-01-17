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
            if 1 <= self.channel_no <= len(self.channels):
                channel_name = self.channels[self.channel_no - 1]
                print(f"TV is on, channel {self.channel_no} ({channel_name})")
            else:
                print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")


def main():
    my_tv = TV()            
    
    my_tv.set_channels([
        "TVP1",
        "TVP2",
        "Polsat",
        "TVN", 
        "Filmbox",
        "Discovery",
        "National Geographic"
])
    my_tv.turn_on()

    my_tv.set_channel(1)
    my_tv.show_status()
    
    my_tv.set_channel(2)
    my_tv.show_status()

    my_tv.set_channel(3)
    my_tv.show_status()

    my_tv.set_channel(4)
    my_tv.show_status()

    my_tv.set_channel(5)
    my_tv.show_status()

    my_tv.set_channel(6)
    my_tv.show_status()

    my_tv.set_channel(7)
    my_tv.show_status()

    my_tv.set_channel(10)
    my_tv.show_status()

    my_tv.turn_off()
    my_tv.show_status()


if __name__ == "__main__":
    main()
