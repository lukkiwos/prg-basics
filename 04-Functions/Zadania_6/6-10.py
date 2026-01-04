def f(x, y):
    count = 0
    
    for z in range(x, y + 1):
        if z < 0:
            if z % 2 == 0:
                count += 1
    return count



if __name__ == "__main__":
    print(f(-7, 8))
    print(f(-1, 11))