
def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    
    remainders = []

    original_num = decimal_num

    while decimal_num > 0:
        remainder = decimal_num % 2
        remainders.append(remainder)

        decimal_num = decimal_num // 2
    binary_num = "".join(map(str, remainders[::-1]))
    return binary_num, original_num

try:
    input_num = input("Enter decimal number: ")
    decimal_number = int(input_num)
    
    binary_result, original = decimal_to_binary(decimal_number)
    print(f"\n{original}(10) = {binary_result}(2)")

except ValueError:
    print("Invalid input. Please enter a natural number.")
except Exception as e:
    print(f"An error occurred: {e}")