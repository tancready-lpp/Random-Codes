import string
import random

# takes only the number of characters
def pass_gen(n):
    low = string.ascii_lowercase
    upp = string.ascii_uppercase
    spec = string.punctuation
    num = string.digits
    tot = low+upp+spec+num
    return "".join([random.choice(tot) for i in range(n)])

print(pass_gen(n=12))