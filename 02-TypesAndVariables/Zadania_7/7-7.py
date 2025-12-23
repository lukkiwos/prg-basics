import random

random_number = random.randint(5,10)
print(random_number)
print()


def f(number):
    random_number = random.randint(1,10)
    print(random_number)
    result = number == random_number
    return result


if __name__ == "__main__":
    print(f(6))