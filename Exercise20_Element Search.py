
list = [5,7,9,12,13,15,17,19,21,24,25,27,33,34,37,39]

number = int(input("What's the number: "))

if number in list:
    print("Its in the list")
    print(list)
else:
    print("It's not in the list")
    list.append(number)
    list.sort()
    print(list)


