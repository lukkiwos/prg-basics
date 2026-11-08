facebook = True
twitter = False
instagram = True

outcome = facebook + twitter + instagram

if outcome >= 2:
    print("Good influencer")
else:
    print("Bad influencer")
print()


def f(f,t,i):
    sum = f + t + i

    if sum >= 2:
        return True
    else:
        return False


if __name__ == "__main__":
    print(f(True, False, True))
    print(f(False, False, True))