import queue

def reverse_text(text):
    stack = queue.LifoQueue()

    # push each character onto the stack
    for char in text:
        stack.put(char)

    # pop characters to build reversed string
    reversed_text = ""
    while not stack.empty():
        reversed_text += stack.get()

    return reversed_text


text = input("Enter text to reverse: ")
result = reverse_text(text)
print("Reversed text:", result)