###
# Character code conversion
# 67, 111, 111, 108, 33

print(chr(67), chr(111), chr(111), chr(108), chr(33))
print()



def f(code):
    x = chr(code)
    return x


if __name__ == "__main__":
    print(f(67), f(111), f(111), f(108), f(33))
