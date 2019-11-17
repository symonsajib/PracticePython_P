
import random
import string
letters = string.ascii_letters
digits = string.digits
others = string.punctuation
d = letters + digits + others
long = input("How long: ")
p = random.sample(d, int(long))
password = "".join(p)
print(password)