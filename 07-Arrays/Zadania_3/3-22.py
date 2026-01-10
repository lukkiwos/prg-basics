import random

def rand_elem(array):

    index = random.randint(0, len(array) - 1)

    return array[index]


if __name__ == "__main__":
    print(rand_elem([5,4,7,2,8]))