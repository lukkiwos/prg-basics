###
# Sums numbers entered by user
#
total_sum = 0
arithmetic_mean = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    count += 1
    arithmetic_mean = total_sum / count
    

print(f"The total sum of numbers is: {total_sum}")
print(f"The arithmetic mean of numbers is: {arithmetic_mean}")
print()


def f():
    total_sum = 0
    arithmetic_mean = 0
    count = 0

    while True:
        number = int(input("Enter a number (0 to stop): "))

        if number == 0:
            break
        total_sum += number
        count += 1
        arithmetic_mean = total_sum / count
    return f"Całkowita suma to: {total_sum} oraz średnia to: {arithmetic_mean}"
    

if __name__ == "__main__":
    print(f())