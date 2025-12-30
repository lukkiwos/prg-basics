facebook = True
twitter = False
instagram = True

result = facebook + twitter + instagram

if result >= 2:
    print("You are a good influencer!")
else:
    print("You are a BAD influencer")

print()






def f(facebook, twitter, instagram):
    result = facebook + twitter + instagram

    if result >= 2:
        return "Jesteś dobrym influencerem"
    else:
        return "Jesteś kiepskim influencerem"
    


if __name__ == "__main__":
    print(f(True, False, True))