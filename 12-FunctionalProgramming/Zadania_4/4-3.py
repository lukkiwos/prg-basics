grades = [3.0, 5.0, 2.0, 3.5, 4.0, 4.0, 3.5, 2.0, 4.0, 2.0]

condition = list(filter(lambda grade: grade != 2.0, grades))

arithmetic_mean = sum(map(lambda grade: grade / len(condition), condition))


print(f"Grades: {', '.join(map(str, grades))}")
print()
print(f"Arithmetic mean for grades (except 2.0 grades) is: {arithmetic_mean:.2f}")