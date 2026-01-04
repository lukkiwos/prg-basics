###
# Generates and prints a random number between 1 and 6,
# similar to rolling a dice
#
import random

x = random.randint(1,6)
print(x)
print()



def f():
    import random

    y = random.randint(1,6)
    
    return y


if __name__ == "__main__":
    print(f())