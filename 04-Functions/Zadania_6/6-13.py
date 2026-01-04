def f(n):
    result = ""

    for x in range(1, n + 1):
        x = str(x)
        result += x
        
    return result



if __name__ == "__main__":
    print(f(11))
    print(f(4))