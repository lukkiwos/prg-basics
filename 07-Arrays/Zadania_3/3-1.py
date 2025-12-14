integer_numbers = [34,7,19,4,21,8]

number_of_even = 0
index = 0

while index < len(integer_numbers):
    number = integer_numbers[index]
    if number % 2 == 0:
        number_of_even += 1

    index += 1


print(f"Tablica wejściowa: {integer_numbers}")
print(f"Liczba elementów parzystych w tablicy wynosi: {number_of_even}")