
def fibonacci():
    Number = int(input("Enter Number: "))
    Initial1 = 0
    Initial2 = 1
    for index in range(0,Number):
        Initial3 = Initial2 + Initial1
        Initial1 = Initial2
        Initial2 = Initial3
        print(Initial3)

fibonacci()






