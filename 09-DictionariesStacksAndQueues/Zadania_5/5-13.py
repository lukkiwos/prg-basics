import queue

# create an empty stack
stack = queue.LifoQueue()

print("Enter numbers, operators (+ - * /) or '=' to calculate.")
print("Type 'exit' to quit.")

while True:
    token = input("Enter value: ")

    if token.lower() == "exit":
        break

    elif token == "=":
        if not stack.empty():
            result = stack.get()
            print("Result:", result)
        else:
            print("Stack is empty, nothing to calculate.")

    elif token in "+-*/":
        if stack.qsize() < 2:
            print("Not enough operands in the stack.")
        else:
            b = stack.get()
            a = stack.get()

            if token == "+":
                stack.put(a + b)
            elif token == "-":
                stack.put(a - b)
            elif token == "*":
                stack.put(a * b)
            elif token == "/":
                if b == 0:
                    print("Error: division by zero")
                    stack.put(a)
                    stack.put(b)
                else:
                    stack.put(a / b)

    else:
        # try to convert to number
        try:
            num = float(token)
            stack.put(num)
        except ValueError:
            print("Invalid input, enter a number or operator.")
