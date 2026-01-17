class Statistics():
    def __init__(self):
        self.numbers = []


    def add_number(self, number):
        self.numbers.append(number)


    def show_numbers(self):
        print("Numbers: ", end=" ")
        for n in self.numbers:
            print(n, end=" ")
        print()


    def get_min(self):
        return min(self.numbers)


    def get_max(self):
        return max(self.numbers)


    def arithmetic_mean(self):
        suma = 0
        for n in self.numbers:
            suma += n

        return suma / len(self.numbers)


    def median(self):
        sorted_numbers = sorted(self.numbers)
        n = len(sorted_numbers)
        middle = n // 2

        if n % 2 == 1:
            return sorted_numbers[middle]
        else:
            return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
        

    def print_statistic(self):
        print(f"Minimum number: {self.get_min()}")
        print(f"Maximum number: {self.get_max()}")
        print(f"Arithmetic mean: {self.arithmetic_mean():.2f}")
        print(f"Median: {self.median()}")


def main():
    stats = Statistics()

    numbers = [12, 37, 6, 9, 17]

    for n in numbers:
        stats.add_number(n)

    stats.show_numbers()
    stats.print_statistic()


if __name__ == "__main__":
    main()