def f(student1, student2):

    student1 = student1.split(",")
    student2 = student2.split(",")

    sum_1 = 0
    sum_2 = 0

    count_1 = 0
    count_2 = 0

    for x in student1:
        x = int(x)
        sum_1 += x
        count_1 += 1
    for x in student2:
        x = int(x)
        sum_2 += x
        count_2 += 1

    average_1 = sum_1 / count_1
    average_2 = sum_2 / count_2

    if average_1 > average_2:
        return 1
    elif average_1 < average_2:
        return 2
    else:
        return 0
    



if __name__ == "__main__":
    print(f("3,4,5", "4,3"))
    print(f("3,4,5", "5,5,4,5"))


# NIE udało mi się zrobić  (na początku nie wiedziałem, reszta moja więc sukces częściowy)