def f(sentence):
    result = ""

    for x in sentence:
        if x != " ":
            result += x
    
    return result







if __name__ == "__main__":
    print(f("integrated development environment"))                                                 # returns "integrateddevelopmentenvironment"
    print(f("A programming language is a system of notation for writing computer programs"))       # returns "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms"
