import random

#generate a random 4 digit secret number
list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
number = random.sample(list1, 4)

# count how many times user are guessing

guess_number = 0
while guess_number < 50:

    # ask user for a 4 digit number

    your_number = input("What's your 4 digit number: ")

    #make a list of two numbers for convinience
    number = list(number)
    your_number = list(your_number)
    print("Secret number is " + str(number))
    print("You entered " + str(your_number))

    #find how many numbers overlap between these two numbers, not position specific

    overlaps = []
    for k in number:
        for l in your_number:
            if k == l and k not in overlaps:
                overlaps.append(l)
            else:
                pass
    #print(overlaps)
    number_overlaps = len(overlaps)
    #find how many numbers overlaps between these two numbers, position specific (cow number)

    cow_counts = 0

    for i in range(len(your_number)):
        if your_number[i] == number[i]:
            cow_counts += 1

    # Find the bull number from (non-position specific overlaps - position specific overlaps)

    bull_counts = int(number_overlaps) - int(cow_counts)
    guess_number += 1

    # print the result, Hurray!
    print(str(cow_counts) + " cows, " + str(bull_counts) + " bulls.")

    if number == your_number:
        break
    else:
        pass


print("You tried " + str(guess_number) + " times")




















