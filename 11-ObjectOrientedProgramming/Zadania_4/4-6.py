# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0


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


    def volume_up(self):
        if self.volume < 10:
            self.volume += 1
        else:
            print("Volume is already at maximum")


    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume is already at minimum")


    def show_status(self):
        if self.is_on:
            if 1 <= self.channel_no <= len(self.channels):
                channel_name = self.channels[self.channel_no - 1]
                print(f"TV is on, channel {self.channel_no} ({channel_name}), volume {self.volume}")
            else:
                print(f"TV is on, channel {self.channel_no}, volume {self.volume}")
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
    my_tv.show_status()
    
    my_tv.set_channel(3)
    my_tv.show_status()

    for i in range(5):
        my_tv.volume_up()
    my_tv.show_status()  

    my_tv.volume_up()     
    my_tv.show_status()

    for _ in range(7):
        my_tv.volume_up()
    my_tv.show_status() 

    for i in range(3):
        my_tv.volume_down()
    my_tv.show_status()   # volume 7

    my_tv.turn_off()
    my_tv.show_status()





if __name__ == "__main__":
    main()
