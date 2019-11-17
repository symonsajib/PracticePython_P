
import random
number =  random.randint(1,9)
print(number)
guess = (input("Guess the number: "))
count = 0

if guess != "exit":
    if int(number) == int(guess):
       print ("Gotcha right")

    elif int(number) < int(guess):
       print ("too high")

    else:
       print ("too low")


else:
    print ('bye')




