with open('C:\\Users\\Symon\\Desktop\\practicepython\\happynumbers.txt', 'r') as happy:
    happy_numbers = happy.read().split('\n')
    print(happy_numbers)


with open('C:\\Users\\Symon\\Desktop\\practicepython\\primenumbers.txt', 'r') as prime:
    prime_numbers = prime.read().split('\n')
    print(prime_numbers)

overlap = []
for i in happy_numbers:
    for k in prime_numbers:
        if i == k:
            overlap.append(i)
print(overlap)



