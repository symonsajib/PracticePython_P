
def get_the_interger():
    return int(input("Enter the number: "))

Number = get_the_interger()
list_divisors = []

for elements in range(1,Number+1):
    if Number % elements == 0:
        list_divisors.append(elements)
    else:
        pass

print("Divisors of the numbers are " + str(list_divisors) + " and ")

if len(list_divisors) > 2:
    print("it's not a prime")
else:
    print("It is a prime number!!")





