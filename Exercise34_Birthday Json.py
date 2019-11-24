
import json

birthdays = {
    "Symon": "11-11-11",
    "Sam":"12-12-12",
    "Sai": "01-13-13",
    "Sevanosky": "14-14-14",
    "Salam": "06-15-15"
}

with open('C:\\Users\\Symon\\Desktop\\practicepython\\birthdays.json', 'w') as f:
    json.dump(birthdays, f)

with open('C:\\Users\\Symon\\Desktop\\practicepython\\birthdays.json', 'r') as f:
    data = f.read()
    print("Here are the list I have: " + str(list(birthdays.keys())))
    name = input("Who's birthday you want to know: ")
    print(birthdays[name])