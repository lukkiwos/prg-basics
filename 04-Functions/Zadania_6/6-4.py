def f(letter, text):
    count = 0
    for x in range(len(text)):
        if letter in text[x]:
            count += 1
    return count


if __name__ == "__main__":
    text = "You never get a second chance to make a first impression"
    letter = "e"
    print(f"The number of letter '{letter}': {f(letter, text)}")


# def f(letter, text):
    # count = 0
    # for x in text:
        # if x == letter:
            # count += 1
    # return count