import queue

number = 18
stack = queue.LifoQueue()

n = number

print("Division\tRemainder")

# divide number and push remainders onto stack
while n > 0:
    remainder = n % 2
    print(f"{n} / 2 = {n // 2}\t{remainder}")
    stack.put(remainder)
    n = n // 2

# pop from stack to get binary number
binary = ""

while not stack.empty():
    binary += str(stack.get())

print()
print("Natural number:", number)
print("Binary number:", binary)
