# tv_show.py file
# main program

import tv

def main():
   # object creation
   tv_set = tv.TV()        # 1

   # object usage
   tv_set.show_status()    # 2
   tv_set.turn_on()        # 3
   tv_set.show_status()    # 4
   tv_set.turn_off()       # 5
   tv_set.show_status()    # 6


if __name__ == "__main__":
   main() 