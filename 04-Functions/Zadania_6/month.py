def month_name(n):
    month_map = {
        1: "Styczeń",
        2: "Luty",
        3: "Marzec",
        4: "Kwiecień",
        5: "Maj",
        6: "Czerwiec",
        7: "Lipiec",
        8: "Sierpień",
        9: "Wrzesień",
        10: "Padziernik",
        11: "Listopad",
        12: "Grudzień"
    }
    return month_map.get(n, "Niepoprawny numer miesiąca")


if __name__ == "__main__":
    print(f"Miesiąc 7 to: {month_name(7)}")