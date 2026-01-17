import queue

# create a queue for customers
customer_queue = queue.Queue()

# ticket counter
ticket_number = 1

while True:
    print("1. Add new customer")
    print("2. Serve next customer")
    print("0. Quit")
    choice = input("Select an option: ")

    if choice == "1":
        # assign ticket and add to queue
        print(f"Customer added with ticket number: {ticket_number}")
        customer_queue.put(ticket_number)
        ticket_number += 1

    elif choice == "2":
        if customer_queue.empty():
            print("No customers in the queue.")
        else:
            next_customer = customer_queue.get()
            print(f"Serving customer with ticket number: {next_customer}")

    elif choice == "0":
        print("Exiting the program.")
        break

    else:
        print("Invalid option.")

    print()
