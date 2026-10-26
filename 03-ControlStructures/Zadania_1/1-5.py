###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
tasks_ok = int(input("Enter properly completed tasks: "))
test_passed = False

if tasks_ok / total_tasks >= 0.5 :
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')


def f(tasks_completed):
    all_tasks = 20
    test_is_passed = False

    if tasks_completed / all_tasks >= 0.5:
        test_is_passed = True

    if test_is_passed:
        return "You passed"
    else:
        return "You failed"


if __name__ == "__main__":
    print(f(20))
    print(f(11))
    print(f(10))
    print(f(9))
    print(f(0))