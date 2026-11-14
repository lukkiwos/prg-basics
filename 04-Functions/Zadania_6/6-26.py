def f(text):
    string = ""
    count = 0
    for letter in text:
        if count == len(text) - 1:
            string += letter
        else:
            string += letter + "-"
        
        count += 1
    return string


if __name__ == "__main__":
    print(f("University"))
    print(f("UE"))
    print(f("x"))
    print(f(""))