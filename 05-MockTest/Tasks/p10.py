def f(sentence):

    suma = 0

    for x in sentence:
        x = ord(x)
        suma += x

    if suma % 3 == 0:
        return True
    else:
        return False




if __name__ == "__main__":
    print(f("hello world"))
    print(f("university"))
    print(f("student"))



# UDAŁO mi się zrobić samemu