def f(text):
    result = "-".join(text)

    return result



if __name__ == "__main__":
    print(f("Univesity"))           # returns "U-n-i-v-e-r-s-i-t-y"
    print(f("UE"))                  # returns "U-E"
    print(f("x"))                   # returns "x"
    print(f(""))                    # returns ""