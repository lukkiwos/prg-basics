def f(sentence):

    samogloski = "aeiouy"
    count = 0

    for x in sentence:
        if x in samogloski:
            count += 1
    
    return count



if __name__ == "__main__":
    print(f("water"))
    print(f("hello world"))



# UDAŁO mi się zrobić samemu