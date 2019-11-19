

number1 = int(input("What's number 1: "))
number2 = int(input("What's number 2: "))
number3 = int(input("What's number 3: "))

def highest(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        print(str(number1) + " is highest")
    elif number2 > number1 and number2 > number3:
        print(str(number2) + " is highest")
    else:
        print(str(number3) + " is highest")

highest(number1, number2, number3)

