

Number = float(input("What's your number: "))
Modulus = Number%2
Modulus_four = Number%4
if Modulus == 0:
    print("Even Number.")
    if Modulus_four == 0:
        print("It's also multiple of 4 !!")
else:
    print("Odd")



