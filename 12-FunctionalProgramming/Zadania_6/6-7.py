ratings = [
    (17,15,16,17,15),
    (16,18,19,17,19),
    (19,15,15,19,18),
    (18,17,19,15,16)
]

results = list(map(lambda number: sum(number) - min(number) - max(number), ratings))

print(results)