def f(binary_number):
    for digit in binary_number:
        if digit not in ('0', '1'):
            return False
    return True

if __name__ == "__main__":
    bin_1 = "101101"
    result_1 = f(bin_1)
    print(result_1)

    bin_2 = "1311a10100"
    result_2 = f(bin_2)
    print(result_2)