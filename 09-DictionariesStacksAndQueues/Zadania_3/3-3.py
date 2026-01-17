import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"               # brackets not correct


def brackets_ok(expression):
    stack = queue.LifoQueue()

    for char in expression:
        # if opening bracket, put on stack
        if char in "([{":
            stack.put(char)

        # if closing bracket
        elif char in ")]}":
            # no matching opening bracket
            if stack.empty():
                return False

            top = stack.get()

            # check if brackets match
            if (char == ")" and top != "(") or \
               (char == "]" and top != "[") or \
               (char == "}" and top != "{"):
                return False

    # if stack is empty, brackets are correct
    return stack.empty()


# tests
if brackets_ok(expression1):
    print("Expression 1: brackets OK")
else:
    print("Expression 1: brackets NOT correct")

if brackets_ok(expression2):
    print("Expression 2: brackets OK")
else:
    print("Expression 2: brackets NOT correct")

if brackets_ok(expression3):
    print("Expression 3: brackets OK")
else:
    print("Expression 3: brackets NOT correct")
