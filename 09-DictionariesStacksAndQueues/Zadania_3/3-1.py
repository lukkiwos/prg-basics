import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put('King of Hearts \u2665')    
cards.put('Queen of Diamonds \u2666')  
cards.put('Jack of Spades \u2660')     

## prints number of elements of the stack
print('Number of stack elements: ', cards.qsize())

# removes and prints elements from the top of the stack
while not cards.empty():
    card = cards.get()
    print(card)

"""
Note the order of the printed elements.
The last added element is printed first.
"""
print()
print()

# create a stack
stack = queue.LifoQueue()

# put numbers on the stack
stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

# sum the last two numbers
last = stack.get()
second_last = stack.get()
last_two_sum = last + second_last
print("Sum of last two numbers: ", last_two_sum)

# sum remaining elements using while loop
remaining_sum = 0

while not stack.empty():
    remaining_sum += stack.get()

print("Sum of remaining stack elements: ", remaining_sum)
