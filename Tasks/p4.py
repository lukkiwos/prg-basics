def f(dictionary):
    
    best_avg = 0
    best_subject = None

    for subject, grades in dictionary.items():
        avg = sum(grades) / len(grades)
        print(f"Subject: {subject}")
        print(f"Grades: {grades}")
        print()
        if avg > best_avg:
            best_avg = avg
            best_subject = subject
            print(f"Average: {avg}")
            print(f"Best average: {best_avg}")
            print(f"Best subject: {best_subject}")
            print()
    
    return best_subject #, best_avg




if __name__ == "__main__":
    x = {"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}

    result = f(x)

    if result == 'comp':
        print("Sukces")

    else:
        print("Failure")

    print(result)