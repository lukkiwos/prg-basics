def f(detector):
    current = 0

    for x in detector:
        if x == "+":
            current += 1
            if current >= 3:
                return True
        else:
            current -= 1

    return False









if __name__ == "__main__":
    print(f("+-+++-+---"))      # returns True
    print(f("+-+-+-+-"))        # returns False
    print(f("+-++-+--"))        # returns False
    print(f("+-++-++-+---"))    # returns True