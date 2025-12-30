###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
sum_even = 0
i = 1

# Calculate the sum of even numbers
while i <= N:
    if i % 2 == 0:
        sum_even += i
    i += 1

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")
print()



def f(number):
    sum_even = 0
    i = 1
    
    while i <= number:
        if i % 2 == 0:
            sum_even += i
        i += 1
    return f"Suma liczb parzystych od 1 do {number} to: {sum_even}"


if __name__ == "__main__":
    print(f(15))