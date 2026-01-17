import json

# Read the contents of the json file
try:
    with open("voting.json", "r") as file:
        votes = json.load(file)
except FileNotFoundError:
    votes = {}

# Vote for a person
person_name = input("Name of the person you are voting for: ")

if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1

# Save voting data to json file
with open("voting.json", "w") as file:
    json.dump(votes, file, indent=4)

print("Vote recorded.")
