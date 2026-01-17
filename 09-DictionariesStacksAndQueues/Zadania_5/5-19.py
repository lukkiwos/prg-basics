import json


def load_reservations(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["reservations"]


def total_rooms(reservations):
    return len(reservations)


def count_paid_unpaid(reservations):
    paid = sum(1 for r in reservations if r["paid"])
    unpaid = sum(1 for r in reservations if not r["paid"])
    return paid, unpaid


def total_values(reservations):
    total_paid = sum(r["nights"] * r["price_per_night"] for r in reservations if r["paid"])
    total_unpaid = sum(r["nights"] * r["price_per_night"] for r in reservations if not r["paid"])
    return total_paid, total_unpaid


def main():
    reservations = load_reservations("reservations.json")

    print("Number of rooms:", total_rooms(reservations))

    paid_count, unpaid_count = count_paid_unpaid(reservations)
    print("Number of paid reservations:", paid_count)
    print("Number of unpaid reservations:", unpaid_count)

    total_paid, total_unpaid = total_values(reservations)
    print("Total value of paid reservations:", total_paid)
    print("Total value of unpaid reservations:", total_unpaid)

# Run the program
if __name__ == "__main__":
    main()