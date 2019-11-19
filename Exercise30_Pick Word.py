
import random
r = random.randrange(267749)
print(r)


with open("C:\\Users\\Symon\\Desktop\\practicepython\\sowpods.txt", "r") as f:
    line = f.readline()
    i = 0
    while line:
        i += 1
        line = f.readline()
        if i == r:
            print(line)
            print(i)

