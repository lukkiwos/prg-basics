def f(sentence):
    sentence1 = ""
    for x in sentence:
        if x != " ":
            sentence1 += x
        
    return sentence1


if __name__ == "__main__":
    print(f("integrated development environmen"))
    print(f("A programming language is a system of notation for writing computer programs"))
