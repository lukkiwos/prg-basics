def f(detector):
    count = 0
    index = 0
    while index < len(detector):
        if detector[index] == "+":
            count += 1
        elif detector[index] == "-":
            count -= 1

        index += 1

        if count >= 3:
            return True
        else:
            continue
    return False
        

if __name__ == "__main__":
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))
    print(f("+-++-+--"))
    print(f("+-++-++-+---"))