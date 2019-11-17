
Number = int(input("Enter your number: "))

New_list = []

for elements in range(1,Number+1):
    if Number % elements == 0:
        New_list.append(elements)
    else:
        pass

print(New_list)